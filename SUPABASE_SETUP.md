# Supabase Setup Guide

## Step 1: Create Supabase Project

1. **Go to Supabase**
   - Visit: https://app.supabase.com
   - Sign in with GitHub or email

2. **Create New Project**
   - Click "New Project"
   - **Organization**: Select or create one
   - **Project Name**: `ain-bandhu`
   - **Database Password**: Generate a strong password (SAVE THIS!)
   - **Region**: Choose closest to Bangladesh (Singapore or Mumbai recommended)
   - Click "Create new project"
   - Wait 2-3 minutes for provisioning

## Step 2: Get API Credentials

1. **Go to Project Settings**
   - Click the ⚙️ gear icon (Settings) in the left sidebar
   - Go to "API" section

2. **Copy These Values:**
   ```
   Project URL: https://xxxxxxxxxx.supabase.co
   anon/public key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```

3. **Add to .env File**
   ```bash
   SUPABASE_URL=https://xxxxxxxxxx.supabase.co
   SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```

## Step 3: Create Database Tables

### Option A: Using SQL Editor (Recommended)

1. **Go to SQL Editor**
   - Click "SQL Editor" in the left sidebar
   - Click "+ New query"

2. **Run This SQL:**

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create conversations table
CREATE TABLE IF NOT EXISTS conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Indexes for fast queries
    INDEX idx_conversations_session_id (session_id),
    INDEX idx_conversations_created_at (created_at)
);

-- Create query_analytics table
CREATE TABLE IF NOT EXISTS query_analytics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id TEXT NOT NULL,
    user_query TEXT NOT NULL,
    intent_detected TEXT,
    tools_used JSONB DEFAULT '[]'::jsonb,
    sections_retrieved INTEGER DEFAULT 0,
    tokens_used INTEGER DEFAULT 0,
    response_time_ms INTEGER DEFAULT 0,
    model TEXT,
    success BOOLEAN DEFAULT TRUE,
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    -- Indexes for analytics queries
    INDEX idx_analytics_session_id (session_id),
    INDEX idx_analytics_intent (intent_detected),
    INDEX idx_analytics_created_at (created_at),
    INDEX idx_analytics_success (success)
);

-- Create sessions table (optional - for session metadata)
CREATE TABLE IF NOT EXISTS sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id TEXT UNIQUE NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_activity TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

    INDEX idx_sessions_session_id (session_id),
    INDEX idx_sessions_last_activity (last_activity)
);

-- Enable Row Level Security (RLS)
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE query_analytics ENABLE ROW LEVEL SECURITY;
ALTER TABLE sessions ENABLE ROW LEVEL SECURITY;

-- Create policies (allow all operations for now - tighten in production)
CREATE POLICY "Enable all operations for conversations"
ON conversations FOR ALL
USING (true);

CREATE POLICY "Enable all operations for query_analytics"
ON query_analytics FOR ALL
USING (true);

CREATE POLICY "Enable all operations for sessions"
ON sessions FOR ALL
USING (true);

-- Create a function to get intent analytics
CREATE OR REPLACE FUNCTION get_intent_analytics()
RETURNS TABLE (
    intent TEXT,
    total_queries BIGINT,
    avg_response_time NUMERIC,
    avg_tokens NUMERIC,
    success_rate NUMERIC
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        intent_detected::TEXT,
        COUNT(*)::BIGINT as total_queries,
        ROUND(AVG(response_time_ms)::NUMERIC, 2) as avg_response_time,
        ROUND(AVG(tokens_used)::NUMERIC, 2) as avg_tokens,
        ROUND((COUNT(*) FILTER (WHERE success = true)::NUMERIC / COUNT(*)::NUMERIC * 100), 2) as success_rate
    FROM query_analytics
    WHERE intent_detected IS NOT NULL
    GROUP BY intent_detected
    ORDER BY total_queries DESC;
END;
$$ LANGUAGE plpgsql;
```

3. **Click "Run"** (bottom right)
4. **Verify Success**: You should see "Success. No rows returned"

### Option B: Using Table Editor (Visual)

If you prefer a visual interface:

1. **Go to Table Editor**
2. **Create "conversations" table:**
   - Click "+ New table"
   - Name: `conversations`
   - Add columns:
     - `id` (uuid, primary key, default: uuid_generate_v4())
     - `session_id` (text, not null)
     - `role` (text, not null)
     - `content` (text, not null)
     - `created_at` (timestamptz, default: now())

3. **Create "query_analytics" table:**
   - Same process, follow the schema above

## Step 4: Verify Tables Created

1. **Go to Table Editor**
2. **You should see:**
   - ✅ conversations
   - ✅ query_analytics
   - ✅ sessions

3. **Click on each table** to verify columns exist

## Step 5: Test Connection

### Using Python Script

Create a test file:

```bash
cat > test_supabase.py << 'EOF'
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

# Get credentials
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print(f"Testing Supabase connection...")
print(f"URL: {url[:30]}..." if url else "URL: NOT SET")
print(f"Key: {key[:30]}..." if key else "Key: NOT SET")

if not url or not key:
    print("\n❌ SUPABASE_URL or SUPABASE_KEY not set in .env")
    exit(1)

try:
    # Create client
    client = create_client(url, key)
    print("\n✓ Supabase client created")

    # Test insert into conversations
    result = client.table("conversations").insert({
        "session_id": "test-session",
        "role": "user",
        "content": "Test message"
    }).execute()

    print("✓ Insert successful")
    print(f"  Inserted ID: {result.data[0]['id']}")

    # Test query
    result = client.table("conversations").select("*").eq("session_id", "test-session").execute()
    print(f"✓ Query successful: {len(result.data)} rows returned")

    # Cleanup
    client.table("conversations").delete().eq("session_id", "test-session").execute()
    print("✓ Cleanup successful")

    print("\n🎉 Supabase connection working perfectly!")

except Exception as e:
    print(f"\n❌ Error: {e}")
    exit(1)
EOF

python test_supabase.py
```

### Expected Output:
```
Testing Supabase connection...
URL: https://xxxxxxxxxx.supabase...
Key: eyJhbGciOiJIUzI1NiIsInR5cCI...

✓ Supabase client created
✓ Insert successful
  Inserted ID: 12345678-1234-1234-1234-123456789abc
✓ Query successful: 1 rows returned
✓ Cleanup successful

🎉 Supabase connection working perfectly!
```

## Step 6: Restart Server with Supabase

```bash
# Kill existing server
kill $(cat /tmp/server.pid) 2>/dev/null

# Restart with Supabase credentials
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > /tmp/server.log 2>&1 &
echo $! > /tmp/server.pid
sleep 3

# Check logs - should see "✓ Supabase connected"
tail -20 /tmp/server.log
```

## Step 7: Test End-to-End

```python
import requests

# Create session
response = requests.post("http://localhost:8000/chat/new", json={})
session_id = response.json()["session_id"]
print(f"Session created: {session_id}")

# Send message
response = requests.post(
    "http://localhost:8000/chat",
    json={
        "session_id": session_id,
        "message": "আমার স্বামী আমাকে মারে। আমি কি করতে পারি?"
    }
)

data = response.json()
print(f"Response received: {data.get('intent')}")
print(f"Tools used: {data.get('tools_used')}")

# Check Supabase - go to Table Editor
# conversations table should have 2 rows (user + assistant)
# query_analytics table should have 1 row
```

## Troubleshooting

### Error: "relation 'conversations' does not exist"
**Fix**: Tables weren't created. Go back to Step 3 and run the SQL again.

### Error: "Invalid API key"
**Fix**:
- Double-check you copied the **anon/public** key (not service_role)
- Make sure no extra spaces in .env file
- Restart server after updating .env

### Error: "Permission denied"
**Fix**: RLS policies might be too restrictive
```sql
-- Disable RLS temporarily for testing
ALTER TABLE conversations DISABLE ROW LEVEL SECURITY;
ALTER TABLE query_analytics DISABLE ROW LEVEL SECURITY;
```

### Connection timeout
**Fix**:
- Check your internet connection
- Verify Supabase project is running (check dashboard)
- Try different region if Asia regions are slow

## Optional: View Data in Supabase

1. **Go to Table Editor**
2. **Click "conversations"** → See all chat messages
3. **Click "query_analytics"** → See query statistics
4. **Run Analytics Query:**
   ```sql
   SELECT * FROM get_intent_analytics();
   ```

## Next Steps

Once Supabase is working:
- ✅ Conversations persist across sessions
- ✅ Analytics data collected
- ✅ Can build dashboards on top of analytics
- ✅ Ready for production deployment

## Cost Estimate

**Supabase Free Tier:**
- 500MB database storage
- 2GB bandwidth
- Unlimited API requests
- **Good for**: 10,000-50,000 queries/month

**Paid Tier** ($25/month):
- 8GB database storage
- 50GB bandwidth
- **Good for**: 100,000+ queries/month

For MVP, **free tier is perfect**.
