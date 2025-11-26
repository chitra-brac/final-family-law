-- Ain Bandhu Database Schema for Supabase (2025)
-- Run this in: Supabase Dashboard > SQL Editor > "New query"

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ========================================
-- TABLE: conversations
-- ========================================
CREATE TABLE IF NOT EXISTS conversations (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id text NOT NULL,
    role text NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content text NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Indexes for fast queries
CREATE INDEX IF NOT EXISTS idx_conversations_session_id ON conversations(session_id);
CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at DESC);

-- ========================================
-- TABLE: query_analytics
-- ========================================
CREATE TABLE IF NOT EXISTS query_analytics (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id text NOT NULL,
    user_query text NOT NULL,
    intent_detected text,
    tools_used jsonb DEFAULT '[]'::jsonb,
    sections_retrieved integer DEFAULT 0,
    tokens_used integer DEFAULT 0,
    response_time_ms integer DEFAULT 0,
    model text,
    success boolean DEFAULT true,
    error_message text,
    created_at timestamptz DEFAULT now()
);

-- Indexes for analytics queries
CREATE INDEX IF NOT EXISTS idx_analytics_session_id ON query_analytics(session_id);
CREATE INDEX IF NOT EXISTS idx_analytics_intent ON query_analytics(intent_detected);
CREATE INDEX IF NOT EXISTS idx_analytics_created_at ON query_analytics(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_analytics_success ON query_analytics(success);

-- ========================================
-- TABLE: sessions (optional)
-- ========================================
CREATE TABLE IF NOT EXISTS sessions (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id text UNIQUE NOT NULL,
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamptz DEFAULT now(),
    last_activity timestamptz DEFAULT now()
);

-- Indexes for sessions
CREATE INDEX IF NOT EXISTS idx_sessions_session_id ON sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_sessions_last_activity ON sessions(last_activity DESC);

-- ========================================
-- ROW LEVEL SECURITY (RLS)
-- ========================================

-- Enable RLS on all tables
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE query_analytics ENABLE ROW LEVEL SECURITY;
ALTER TABLE sessions ENABLE ROW LEVEL SECURITY;

-- Drop existing policies if any
DROP POLICY IF EXISTS "Allow all access to conversations" ON conversations;
DROP POLICY IF EXISTS "Allow all access to query_analytics" ON query_analytics;
DROP POLICY IF EXISTS "Allow all access to sessions" ON sessions;

-- Create policies for anon/authenticated access (MVP - open access)
-- NOTE: For production, you should restrict these based on user authentication

CREATE POLICY "Allow all access to conversations"
ON conversations
FOR ALL
TO anon, authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Allow all access to query_analytics"
ON query_analytics
FOR ALL
TO anon, authenticated
USING (true)
WITH CHECK (true);

CREATE POLICY "Allow all access to sessions"
ON sessions
FOR ALL
TO anon, authenticated
USING (true)
WITH CHECK (true);

-- ========================================
-- HELPER FUNCTIONS
-- ========================================

-- Function to get intent analytics
CREATE OR REPLACE FUNCTION get_intent_analytics()
RETURNS TABLE (
    intent text,
    total_queries bigint,
    avg_response_time numeric,
    avg_tokens numeric,
    success_rate numeric
) 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        intent_detected::text,
        COUNT(*)::bigint as total_queries,
        ROUND(AVG(response_time_ms)::numeric, 2) as avg_response_time,
        ROUND(AVG(tokens_used)::numeric, 2) as avg_tokens,
        ROUND((COUNT(*) FILTER (WHERE success = true)::numeric / COUNT(*)::numeric * 100), 2) as success_rate
    FROM query_analytics
    WHERE intent_detected IS NOT NULL
    GROUP BY intent_detected
    ORDER BY total_queries DESC;
END;
$$;

-- ========================================
-- VERIFICATION
-- ========================================

-- Show created tables
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
AND table_name IN ('conversations', 'query_analytics', 'sessions');
