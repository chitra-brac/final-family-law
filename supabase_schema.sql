-- Supabase Schema for Ain Bandhu Legal Chatbot
-- Run this in your Supabase SQL Editor

-- Table: conversations
-- Stores conversation messages for each user session
CREATE TABLE IF NOT EXISTS conversations (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system', 'tool')),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Index for fast session lookups
CREATE INDEX IF NOT EXISTS idx_conversations_session_id
    ON conversations(session_id);

-- Index for time-based queries
CREATE INDEX IF NOT EXISTS idx_conversations_created_at
    ON conversations(created_at DESC);


-- Table: query_analytics
-- Logs analytics data for each query
CREATE TABLE IF NOT EXISTS query_analytics (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    session_id TEXT NOT NULL,
    user_query TEXT NOT NULL,
    intent_detected TEXT,
    tools_used JSONB DEFAULT '[]'::jsonb,
    sections_retrieved INTEGER DEFAULT 0,
    tokens_used INTEGER DEFAULT 0,
    response_time_ms INTEGER,
    model TEXT,
    success BOOLEAN DEFAULT true,
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for session-based analytics
CREATE INDEX IF NOT EXISTS idx_analytics_session_id
    ON query_analytics(session_id);

-- Index for intent analysis
CREATE INDEX IF NOT EXISTS idx_analytics_intent
    ON query_analytics(intent_detected);

-- Index for time-based analytics
CREATE INDEX IF NOT EXISTS idx_analytics_created_at
    ON query_analytics(created_at DESC);

-- Index for success/failure tracking
CREATE INDEX IF NOT EXISTS idx_analytics_success
    ON query_analytics(success);


-- Optional: Row Level Security (RLS) policies
-- Uncomment if you want to enable RLS

-- ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE query_analytics ENABLE ROW LEVEL SECURITY;

-- Allow anonymous read/write for MVP (adjust for production)
-- CREATE POLICY "Allow anonymous access" ON conversations FOR ALL USING (true);
-- CREATE POLICY "Allow anonymous access" ON query_analytics FOR ALL USING (true);


-- View: Recent conversations summary
CREATE OR REPLACE VIEW recent_conversations AS
SELECT
    session_id,
    COUNT(*) as message_count,
    MIN(created_at) as started_at,
    MAX(created_at) as last_message_at
FROM conversations
GROUP BY session_id
ORDER BY MAX(created_at) DESC
LIMIT 100;


-- View: Intent analytics
CREATE OR REPLACE VIEW intent_analytics AS
SELECT
    intent_detected,
    COUNT(*) as query_count,
    AVG(tokens_used) as avg_tokens,
    AVG(response_time_ms) as avg_response_time_ms,
    AVG(sections_retrieved) as avg_sections,
    SUM(CASE WHEN success THEN 1 ELSE 0 END)::FLOAT / COUNT(*) * 100 as success_rate
FROM query_analytics
WHERE intent_detected IS NOT NULL
GROUP BY intent_detected
ORDER BY query_count DESC;


-- Function: Get conversation history
CREATE OR REPLACE FUNCTION get_conversation_history(p_session_id TEXT, p_limit INTEGER DEFAULT 50)
RETURNS TABLE(role TEXT, content TEXT, created_at TIMESTAMP WITH TIME ZONE) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.role,
        c.content,
        c.created_at
    FROM conversations c
    WHERE c.session_id = p_session_id
    ORDER BY c.created_at ASC
    LIMIT p_limit;
END;
$$ LANGUAGE plpgsql;


-- Function: Log query analytics
CREATE OR REPLACE FUNCTION log_query_analytics(
    p_session_id TEXT,
    p_user_query TEXT,
    p_intent_detected TEXT,
    p_tools_used JSONB,
    p_sections_retrieved INTEGER,
    p_tokens_used INTEGER,
    p_response_time_ms INTEGER,
    p_model TEXT,
    p_success BOOLEAN,
    p_error_message TEXT DEFAULT NULL
) RETURNS UUID AS $$
DECLARE
    v_id UUID;
BEGIN
    INSERT INTO query_analytics (
        session_id,
        user_query,
        intent_detected,
        tools_used,
        sections_retrieved,
        tokens_used,
        response_time_ms,
        model,
        success,
        error_message
    ) VALUES (
        p_session_id,
        p_user_query,
        p_intent_detected,
        p_tools_used,
        p_sections_retrieved,
        p_tokens_used,
        p_response_time_ms,
        p_model,
        p_success,
        p_error_message
    ) RETURNING id INTO v_id;

    RETURN v_id;
END;
$$ LANGUAGE plpgsql;


-- Sample queries for testing:

-- Get all conversations for a session
-- SELECT * FROM get_conversation_history('test-session-123');

-- Get intent analytics
-- SELECT * FROM intent_analytics;

-- Get recent conversations
-- SELECT * FROM recent_conversations;
