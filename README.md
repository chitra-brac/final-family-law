# Family Law Assistant for Bangladeshi Women

AI-powered legal assistant providing free legal guidance to Bangladeshi women on family law, domestic violence, divorce, custody, and women's rights — in Bengali.

## Architecture

```
User (Bengali) ──► FastAPI ──► GPT-5.1 (reasoning)
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
             get_legal_     get_procedural_  search_legal_
             knowledge      guidance         sections
             (JSON lookup)  (JSON lookup)    (JSON lookup)
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                          GPT-5.1 response
                          (Bengali, conversational)
```

GPT-5.1 decides which tools to call (often all three in parallel). All tools are in-memory JSON lookups (<10ms). `search_legal_sections` accepts optional `section_numbers` to return full law text for specific sections.

## Data

All files are loaded into memory at startup — every tool call is a dict lookup, under 10ms.

| File | Records | Description |
|------|---------|-------------|
| `family_laws_final.json` | 1,512 sections / 58 acts | Full law text + semantic summary per section, indexed as `sections[act_id][section_number]` for O(1) lookup |
| `intent_mappings.json` | 15 intents | Maps each intent to 2–4 hand-picked section references (31 total) — the curated fast path |
| `procedural_knowledge.json` | 15 intent-specific + 8 general | Bengali guidance per intent (definitions, court orders, penalties, immediate actions) + cross-cutting how-to guides (file FIR, safety planning, legal aid, evidence collection, etc.) |
| `act_summaries.json` | 58 acts | Short English summary per act — returned as a browse layer before drilling into sections |

## Tools

GPT-5.1 calls these as OpenAI function-calling tools. All three are in-memory JSON lookups with no external calls.

### `get_legal_knowledge(intent)`
Takes one of 15 intent enum values. Looks up the curated section references for that intent in `intent_mappings.json`, then fetches the full law text for each from `family_laws_final.json`. Returns 2–4 sections of actual statute text. This is the fast path for known intents.

### `get_procedural_guidance(intent, topics[])`
Takes an intent plus an optional array of up to 3 general procedure topics (`file_fir`, `safety_planning`, `get_legal_aid`, etc.). Returns the intent-specific guidance block (definitions, court orders, exact penalties, immediate actions — all in Bengali) plus the requested general procedure guides. Almost always called alongside `get_legal_knowledge` in the same parallel round.

### `search_legal_sections(act_ids[], query, section_numbers[])`
The open-ended tool for anything outside the 15 intents. Uses a two-phase pattern:
- **Browse** (no `section_numbers`): returns section titles + semantic summaries for all sections in the requested acts, capped at 200. Also returns each act's summary from `act_summaries.json`.
- **Drill-down** (with `section_numbers`): returns full law text for the specified sections only.

GPT reads the summaries in round 1, picks the relevant section numbers, then calls again in round 2 for full text. This avoids dumping the entire act into context. The full catalog of all 58 acts (organised by category: Violence, Muslim, Hindu, Christian, Children, Courts, Property, Maintenance, etc.) is embedded in the tool's description so GPT can select act IDs without an extra lookup.

The 15 intents cover 31 curated sections across 12 acts. The remaining 46 acts and 1,481 sections are only reachable via `search_legal_sections`.

## Request flow

1. User sends Bengali message via `POST /chat`
2. GPT-5.1 analyzes the question and calls all 3 tools in parallel
3. All tools return from in-memory JSON (<10ms)
4. `search_legal_sections` returns summaries; if `section_numbers` passed, includes full law text for those sections
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
  "intent": "domestic_violence_general",
  "tools_used": ["get_legal_knowledge", "get_procedural_guidance", "search_legal_sections"],
  "timestamp": "2026-03-14T12:00:00Z"
}
```

### `GET /health`

Returns `{"status": "healthy", "version": "1.0.0", "timestamp": "2026-03-14T12:00:00Z"}`.

## Supported intents

Domestic violence, rape/sexual violence, sexual harassment, dowry, child marriage, divorce/talaq, custody, maintenance, parent maintenance, polygamy/second marriage, inheritance, marriage registration, dower/mehr, cybercrime, Hindu separation.

## Environment variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-5.1-chat-latest` | Main reasoning model |
| `SUPABASE_URL` | No | — | Chat history persistence |
| `SUPABASE_KEY` | No | — | Chat history persistence |
| `DEBUG` | No | `False` | Debug mode |

## Project structure

```
final-family-law/
├── app/
│   ├── main.py                    # FastAPI app
│   ├── config.py                  # Settings (env vars)
│   ├── services/
│   │   ├── llm_service.py         # GPT-5.1 integration + system prompt
│   │   ├── data_loader.py         # JSON data loader (in-memory)
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
- Cost: ~4.8c per query (GPT-5.1 only, all tools are free lookups)
- Data: 1,512 sections across 58 Bangladesh family law acts

## Deployment

### Railway
Set `OPENAI_API_KEY` in environment variables. Railway auto-detects and deploys.

### Docker
```bash
docker build -t family-law-assistant .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key family-law-assistant
```

## License

MIT License — See [LICENSE](LICENSE).

## Disclaimer

This AI provides general legal information, not legal advice. Consult qualified legal professionals for specific matters.
