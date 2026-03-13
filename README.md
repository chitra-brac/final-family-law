# Ain Bandhu — Legal AI for Bangladeshi Women

AI-powered legal assistant providing free legal guidance to Bangladeshi women on family law, domestic violence, divorce, custody, and women's rights — in Bengali.

## Architecture

```
User (Bengali) ──► FastAPI ──► GPT-5.1 (reasoning)
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
             get_legal_     get_procedural_  search_legal_
             knowledge      guidance         sections
             (JSON lookup)  (JSON lookup)    (gpt-4o-mini)
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                          GPT-5.1 response
                          (Bengali, conversational)
```

All three tools are called **in parallel** on every legal question. The two lookup tools return in <10ms; the search tool uses a lightweight model for act/section discovery across the full corpus.

## Data

| File | Records | Size | Description |
|------|---------|------|-------------|
| `family_laws_final.json` | 1,512 sections | 3.3 MB | Full text of all sections across 58 Bangladesh acts |
| `intent_mappings.json` | 15 intents | 7 KB | Maps intents to mandatory legal sections + notes |
| `procedural_knowledge.json` | 15 intent-specific + 8 general | 133 KB | Step-by-step procedures, definitions, punishments, timelines |
| `act_summaries.json` | 58 acts | 38 KB | Act titles + summaries for search-stage act discovery |

## Tools

| Tool | Source | Latency | Cost | Sections accessible |
|------|--------|---------|------|-------------------|
| `get_legal_knowledge` | intent_mappings.json → family_laws_final.json | <10ms | $0 | 31 (curated per intent) |
| `get_procedural_guidance` | procedural_knowledge.json | <10ms | $0 | — (procedures, not sections) |
| `search_legal_sections` | GPT model → family_laws_final.json | ~1s | ~0.8c | 1,512 (full corpus) |

The 15 intents cover 12 acts with 31 curated sections. The remaining 46 acts and 1,481 sections are accessible only through `search_legal_sections`.

## Request flow

1. User sends Bengali message via `POST /chat`
2. GPT-5.1 analyzes the question and calls all 3 tools in parallel
3. Lookup tools return curated sections + procedures from JSON (<10ms)
4. Search tool discovers relevant sections from the full 1,512-section corpus (~1s, runs in parallel)
5. GPT-5.1 synthesizes all tool results into a conversational Bengali response
6. Response returned with metadata (tools used, token count, timing)

## Quick start

```bash
git clone https://github.com/chitra-brac/final-family-law.git
cd final-family-law
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY to .env
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Test:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test", "message": "আমার স্বামী আমাকে মারধর করে"}'
```

## API

### `POST /chat`

```json
// Request
{"session_id": "uuid", "message": "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?"}

// Response
{
  "session_id": "uuid",
  "response": "আপনি এখন নিরাপদ তো? ...",
  "tools_used": [...],
  "tokens_used": 21866,
  "response_time_ms": 9910,
  "success": true
}
```

### `GET /health`

Returns `{"status": "healthy", "service": "ain-bandhu-legal-chatbot", "version": "1.0.0"}`.

## Supported intents

Domestic violence, rape/sexual violence, sexual harassment, dowry, child marriage, divorce/talaq, custody, maintenance, parent maintenance, polygamy/second marriage, inheritance, marriage registration, dower/mehr, cybercrime, Hindu separation.

## Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-5.1-chat-latest` | Main reasoning model |
| `SEARCH_MODEL` | No | `gpt-4o-mini` | Model for semantic search |
| `SUPABASE_URL` | No | — | Chat history persistence |
| `SUPABASE_KEY` | No | — | Chat history persistence |
| `DEBUG` | No | `False` | Debug mode |

## Project structure

```
final-family-law/
├── app/
│   ├── main.py                    # FastAPI app
│   ├── config.py                  # Settings (env vars)
│   ├── api/chat.py                # Chat endpoint
│   ├── services/
│   │   ├── llm_service.py         # GPT-5.1 integration + system prompt
│   │   ├── data_loader.py         # JSON data loader (in-memory)
│   │   ├── semantic_search.py     # Search via lightweight model
│   │   └── supabase_service.py    # Chat persistence (optional)
│   └── tools/
│       └── legal_tools.py         # Tool definitions + execution
├── data/
│   ├── family_laws_final.json     # 1,512 sections, 58 acts
│   ├── intent_mappings.json       # 15 intents → sections
│   ├── procedural_knowledge.json  # Procedures + guidance
│   └── act_summaries.json         # Act metadata for search
└── requirements.txt
```

## Performance

- Response time: 10-30s (GPT-5.1 with reasoning)
- Token usage: ~20k tokens per complex query
- Cost: ~5.6c per query (GPT-5.1 + search model)
- Data: 1,512 sections across 58 Bangladesh family law acts

## Deployment

### Railway
Set `OPENAI_API_KEY` in environment variables. Railway auto-detects and deploys.

### Docker
```bash
docker build -t ain-bandhu .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key ain-bandhu
```

## License

MIT License — See [LICENSE](LICENSE).

## Disclaimer

This AI provides general legal information, not legal advice. Consult qualified legal professionals for specific matters.
