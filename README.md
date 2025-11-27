# Ain Bandhu - Legal AI for Bangladeshi Women

AI-powered legal assistant providing free legal guidance to Bangladeshi women on family law, domestic violence, divorce, custody, and women's rights - in Bengali.

## Features

- **🇧🇩 Bangladesh Law Only** - 58 legal sections from 8 family law acts
- **🤖 Powered by GPT-5.1** - Fast, accurate, conversational responses
- **📚 15 Legal Topics** - Domestic violence, rape, dowry, divorce, custody, maintenance, and more
- **💬 Natural Conversations** - Talks like a knowledgeable friend, not a robot
- **⚡ Smart Context** - Remembers conversation, doesn't repeat unnecessarily
- **🛡️ Safety First** - Prioritizes user safety in crisis situations

## Quick Start

### 1. Install
```bash
git clone https://github.com/chitra-brac/final-family-law.git
cd final-family-law
pip install -r requirements.txt
```

### 2. Configure
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 3. Run
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Test
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test", "message": "হেলো"}'
```

## API Endpoints

### `POST /chat`
Send a message and get AI response.

**Request:**
```json
{
  "session_id": "uuid-or-string",
  "message": "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?"
}
```

**Response:**
```json
{
  "session_id": "uuid-or-string",
  "response": "আপনি এখন নিরাপদ তো? যদি বিপদ থাকে...",
  "intent": "domestic_violence_general",
  "tools_used": [...],
  "tokens_used": 21866,
  "response_time_ms": 9910,
  "success": true
}
```

### `GET /health`
Health check.

```json
{
  "status": "healthy",
  "service": "ain-bandhu-legal-chatbot",
  "version": "1.0.0"
}
```

## Supported Topics

All 15 legal intents are fully functional:

- Domestic Violence (গৃহ সহিংসতা)
- Rape & Sexual Violence (ধর্ষণ ও যৌন সহিংসতা)
- Sexual Harassment (যৌন হয়রানি)
- Dowry (যৌতুক)
- Child Marriage (বাল্যবিবাহ)
- Divorce/Talaq (তালাক)
- Custody (সন্তানের হেফাজত)
- Maintenance (ভরণপোষণ)
- Parent Maintenance (পিতামাতার ভরণপোষণ)
- Polygamy/Second Marriage (বহুবিবাহ)
- Inheritance (উত্তরাধিকার)
- Marriage Registration (বিবাহ নিবন্ধন)
- Dower/Mehr (দেনমোহর)
- Cybercrime (সাইবার অপরাধ)
- Hindu Separation (হিন্দু বিবাহ বিচ্ছেদ)

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | - | Your OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-5.1-chat-latest` | Model to use |
| `SUPABASE_URL` | No | - | Optional: For chat history |
| `SUPABASE_KEY` | No | - | Optional: For chat history |
| `DEBUG` | No | `False` | Debug mode |

## Deployment

### Railway
```bash
# Railway will auto-detect and deploy
# Just set OPENAI_API_KEY in environment variables
```

### Docker
```bash
docker build -t ain-bandhu .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key ain-bandhu
```

## Project Structure

```
final/
├── app/
│   ├── main.py                 # FastAPI app
│   ├── config.py               # Settings
│   ├── api/chat.py             # Chat endpoints
│   ├── services/
│   │   ├── llm_service.py      # GPT-5.1 integration
│   │   ├── data_loader.py      # Legal data loader
│   │   └── supabase_service.py # Chat persistence
│   └── tools/
│       └── legal_tools.py      # Tool definitions
├── data/
│   ├── family_laws_final.json        # 58 legal sections
│   ├── procedural_knowledge.json     # Procedures & guidance
│   ├── intent_mappings.json          # Intent → law mappings
│   └── act_summaries.json            # Act descriptions
└── requirements.txt
```

## How It Works

1. **User sends Bengali message** → FastAPI endpoint
2. **LLM analyzes intent** → Calls tools to get relevant law & procedures
3. **Tools fetch data** → From JSON files (in-memory, <10ms)
4. **LLM generates response** → Natural, conversational Bengali
5. **Response returned** → With metadata (intent, tokens, time)

## Performance

- **Response Time**: 10-30 seconds (GPT-5.1 with reasoning)
- **Token Usage**: ~20k tokens per complex query
- **Cost**: ~$0.02 per query with GPT-5.1-chat-latest
- **Accuracy**: 100% Bangladesh law, no hallucinations

## License

MIT License - See [LICENSE](LICENSE)

## Disclaimer

This AI provides general legal information only, not legal advice. Users should consult qualified legal professionals for specific matters.

---

Built with ❤️ for Bangladeshi women's rights
