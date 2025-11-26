-- Ain Bandhu Database Schema - Profile-Based Architecture
-- Run this in: Supabase Dashboard > SQL Editor > "New query"

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ========================================
-- TABLE: user_profiles
-- Anonymous but persistent user tracking
-- ========================================
DROP TABLE IF EXISTS user_profiles CASCADE;
CREATE TABLE user_profiles (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    profile_id text UNIQUE NOT NULL,

    -- Gradually collected context
    inferred_context jsonb DEFAULT '{}'::jsonb,

    -- Timestamps
    created_at timestamptz DEFAULT now(),
    last_active timestamptz DEFAULT now()
);

CREATE INDEX idx_user_profiles_profile_id ON user_profiles(profile_id);
CREATE INDEX idx_user_profiles_last_active ON user_profiles(last_active DESC);

-- ========================================
-- TABLE: conversations
-- All messages for a profile
-- ========================================
DROP TABLE IF EXISTS conversations CASCADE;
CREATE TABLE conversations (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    profile_id text NOT NULL REFERENCES user_profiles(profile_id) ON DELETE CASCADE,

    -- Message data
    role text NOT NULL CHECK (role IN ('user', 'assistant', 'system', 'tool')),
    content text NOT NULL,

    -- Metadata (optional)
    metadata jsonb DEFAULT '{}'::jsonb,

    -- Timestamp
    created_at timestamptz DEFAULT now()
);

CREATE INDEX idx_conversations_profile_id ON conversations(profile_id);
CREATE INDEX idx_conversations_profile_created ON conversations(profile_id, created_at ASC);

-- ========================================
-- TABLE: query_analytics
-- Analytics for each query
-- ========================================
DROP TABLE IF EXISTS query_analytics CASCADE;
CREATE TABLE query_analytics (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    profile_id text NOT NULL,

    -- Query data
    user_query text NOT NULL,
    intent_detected text,

    -- Tool usage
    tools_used jsonb DEFAULT '[]'::jsonb,
    sections_retrieved integer DEFAULT 0,

    -- Performance metrics
    tokens_used integer DEFAULT 0,
    response_time_ms integer DEFAULT 0,
    model text,

    -- Success tracking
    success boolean DEFAULT true,
    error_message text,

    -- Timestamp
    created_at timestamptz DEFAULT now()
);

CREATE INDEX idx_analytics_profile_id ON query_analytics(profile_id);
CREATE INDEX idx_analytics_intent ON query_analytics(intent_detected);
CREATE INDEX idx_analytics_created_at ON query_analytics(created_at DESC);

-- ========================================
-- ROW LEVEL SECURITY (RLS)
-- ========================================

-- Enable RLS
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE query_analytics ENABLE ROW LEVEL SECURITY;

-- Allow all access for MVP (open access)
CREATE POLICY "Allow all access to user_profiles"
ON user_profiles FOR ALL TO anon, authenticated
USING (true) WITH CHECK (true);

CREATE POLICY "Allow all access to conversations"
ON conversations FOR ALL TO anon, authenticated
USING (true) WITH CHECK (true);

CREATE POLICY "Allow all access to query_analytics"
ON query_analytics FOR ALL TO anon, authenticated
USING (true) WITH CHECK (true);

-- ========================================
-- HELPER FUNCTIONS
-- ========================================

-- Get or create user profile
CREATE OR REPLACE FUNCTION get_or_create_profile(p_profile_id text)
RETURNS TABLE (
    id uuid,
    profile_id text,
    inferred_context jsonb,
    created_at timestamptz,
    last_active timestamptz
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id uuid;
    v_profile_id text;
    v_context jsonb;
    v_created timestamptz;
    v_active timestamptz;
BEGIN
    -- Try to find existing profile
    SELECT
        user_profiles.id,
        user_profiles.profile_id,
        user_profiles.inferred_context,
        user_profiles.created_at,
        user_profiles.last_active
    INTO v_id, v_profile_id, v_context, v_created, v_active
    FROM user_profiles
    WHERE user_profiles.profile_id = p_profile_id;

    -- If not found, create new profile
    IF v_id IS NULL THEN
        INSERT INTO user_profiles (profile_id)
        VALUES (p_profile_id)
        RETURNING
            user_profiles.id,
            user_profiles.profile_id,
            user_profiles.inferred_context,
            user_profiles.created_at,
            user_profiles.last_active
        INTO v_id, v_profile_id, v_context, v_created, v_active;
    ELSE
        -- Update last_active
        UPDATE user_profiles
        SET last_active = now()
        WHERE user_profiles.profile_id = p_profile_id
        RETURNING
            user_profiles.id,
            user_profiles.profile_id,
            user_profiles.inferred_context,
            user_profiles.created_at,
            user_profiles.last_active
        INTO v_id, v_profile_id, v_context, v_created, v_active;
    END IF;

    -- Return the profile
    RETURN QUERY SELECT v_id, v_profile_id, v_context, v_created, v_active;
END;
$$;

-- Get conversation history
CREATE OR REPLACE FUNCTION get_conversation_history(
    p_profile_id text,
    p_limit integer DEFAULT 50
)
RETURNS TABLE (role text, content text, created_at timestamptz)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.role, c.content, c.created_at
    FROM conversations c
    WHERE c.profile_id = p_profile_id
    ORDER BY c.created_at ASC
    LIMIT p_limit;
END;
$$;

-- Get intent analytics
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
        COUNT(*)::bigint,
        ROUND(AVG(response_time_ms)::numeric, 2),
        ROUND(AVG(tokens_used)::numeric, 2),
        ROUND((COUNT(*) FILTER (WHERE success = true)::numeric / COUNT(*)::numeric * 100), 2)
    FROM query_analytics
    WHERE intent_detected IS NOT NULL
    GROUP BY intent_detected
    ORDER BY COUNT(*) DESC;
END;
$$;
