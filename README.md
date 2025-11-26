# Ain Bandhu - AI Legal Assistant for Bangladeshi Women

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI-powered legal chatbot providing free legal guidance to underprivileged Bangladeshi women on family law, domestic violence, rape, dowry, divorce, custody, and women's rights.

## Features

- **🇧🇩 Bangladesh-Specific Legal Knowledge**: 58 legal sections from 8 family law acts
- **🤖 AI-Powered Responses**: Uses OpenAI gpt-5-nano for intelligent, context-aware advice
- **⚡ Fast & Cost-Effective**: ~19s response time, ~$0.001/query (99% cheaper than gpt-5)
- **🛡️ Safety-First Approach**: Always prioritizes user safety, provides emergency contacts
- **📚 Comprehensive Coverage**: 12 legal intent categories (9/12 working in MVP)
- **🔧 Tool-Based Architecture**: Separates legal knowledge retrieval from procedural guidance
- **💾 Conversation Persistence**: Optional Supabase integration for storing chat history

## Supported Legal Topics

| Intent | Coverage | Description |
|--------|----------|-------------|
| ✅ Domestic Violence | Working | Physical/emotional abuse, protection orders |
| ✅ Rape & Sexual Violence | Working | Sexual assault, FIR filing, medical evidence |
| ✅ Dowry | Working | Dowry demands, harassment, legal remedies |
| ✅ Child Marriage | Working | Underage marriage prevention |
| ✅ Divorce/Talaq | Working | Islamic divorce procedures, rights |
| ✅ Polygamy | Working | Second marriage permissions |
| ✅ Inheritance | Working | Property succession rights |
| ✅ Marriage Registration | Working | Legal marriage registration |
| ✅ Dower/Mehr | Working | Mehr payment obligations |
| ⚠️ Custody | Partial | Works with explicit queries |
| ⚠️ Maintenance | Partial | Works with explicit queries |
| ⚠️ Parent Maintenance | Partial | Works with explicit queries |

## Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key
- (Optional) Supabase account for persistence

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ain-bandhu.git
cd ain-bandhu
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

4. **Run the server**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

5. **Test the API**
```bash
curl -X POST http://localhost:8000/chat/new
```

## Docker Deployment

### Build and Run

```bash
# Build the image
docker build -t ain-bandhu .

# Run the container
docker run -d \
  -p 8000:8000 \
  -e OPENAI_API_KEY=your_key_here \
  --name ain-bandhu \
  ain-bandhu
```

### Docker Compose

```yaml
version: '3.8'
services:
  ain-bandhu:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENAI_MODEL=gpt-5-nano
      - DEBUG=False
    restart: unless-stopped
```

## API Documentation

### Endpoints

#### `POST /chat/new`
Create a new chat session.

**Response:**
```json
{
  "session_id": "uuid-here",
  "greeting": "আসসালামু আলাইকুম। আমি আইন বন্ধু...",
  "timestamp": "2025-11-26T00:00:00"
}
```

#### `POST /chat`
Send a message and get AI response.

**Request:**
```json
{
  "session_id": "uuid-here",
  "message": "আমার স্বামী আমাকে মারে। আমি কি করতে পারি?"
}
```

**Response:**
```json
{
  "session_id": "uuid-here",
  "response": "আপনার নিরাপত্তা সবার আগে...",
  "intent": "domestic_violence_general",
  "urgency": null,
  "tools_used": ["get_legal_knowledge", "get_procedural_guidance"],
  "timestamp": "2025-11-26T00:00:00"
}
```

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-11-26T00:00:00"
}
```

## Architecture

```
┌─────────────────┐
│   FastAPI App   │
└────────┬────────┘
         │
    ┌────┴─────┐
    │          │
┌───▼───┐  ┌──▼──────┐
│  LLM  │  │ Data    │
│Service│  │ Loader  │
└───┬───┘  └──┬──────┘
    │         │
┌───▼─────────▼───┐
│   Legal Tools   │
├─────────────────┤
│ get_legal_      │
│ knowledge()     │
│                 │
│ get_procedural_ │
│ guidance()      │
└─────────────────┘
         │
    ┌────┴─────┐
    │          │
┌───▼───┐  ┌──▼──────────┐
│Family │  │ Procedural  │
│ Laws  │  │ Knowledge   │
│ JSON  │  │    JSON     │
└───────┘  └─────────────┘
```

## Performance Metrics

| Metric | gpt-5 | gpt-5-nano | Improvement |
|--------|-------|------------|-------------|
| Response Time | 51.73s | 18.89s | 65% faster |
| Cost/Query | $0.09 | $0.001 | 99% cheaper |
| Tokens/Query | 38,809 | ~7,000 | 82% reduction |
| Monthly Cost (500 queries/day) | $1,350 | $15 | $1,335 savings |

## Data Sources

### Legal Knowledge
- **family_laws_final.json**: 58 legal sections from 8 Bangladesh family law acts
  - Women & Children Repression Prevention Act 2000 (Act 835)
  - Domestic Violence (Prevention and Protection) Act 2010 (Act 1063)
  - Dowry Prohibition Act 1980 (Act 1256)
  - Child Marriage Restraint Act 2017 (Act 1207)
  - Muslim Family Laws Ordinance 1961 (Act 305)
  - And more...

### Procedural Knowledge
- **procedural_knowledge.json**: Intent-specific guidance
  - Lawyer's strategic playbook
  - Step-by-step legal processes
  - Support organizations (BNWLA, ASK, OCC)
  - General procedures (FIR filing, evidence collection, safety planning)

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | - | OpenAI API key |
| `OPENAI_MODEL` | No | `gpt-4-turbo` | Model to use (recommend `gpt-5-nano`) |
| `SUPABASE_URL` | No | - | Supabase project URL (optional) |
| `SUPABASE_KEY` | No | - | Supabase anon key (optional) |
| `DEBUG` | No | `False` | Enable debug mode |
| `CORS_ORIGINS` | No | `["*"]` | Allowed CORS origins |

## Development

### Project Structure
```
ain-bandhu/
├── app/
│   ├── main.py              # FastAPI app
│   ├── config.py            # Configuration
│   ├── models.py            # Pydantic models
│   ├── services/
│   │   ├── llm_service.py   # OpenAI integration
│   │   ├── data_loader.py   # Legal data loader
│   │   └── supabase_service.py
│   └── tools/
│       └── legal_tools.py   # Tool definitions
├── data/
│   ├── family_laws_final.json
│   ├── procedural_knowledge.json
│   ├── intent_mappings.json
│   └── act_summaries.json
├── requirements.txt
├── Dockerfile
└── README.md
```

### Running Tests
```bash
# Test specific intent
python -c "
import requests
response = requests.post('http://localhost:8000/chat/new', json={})
session_id = response.json()['session_id']
response = requests.post(
    'http://localhost:8000/chat',
    json={'session_id': session_id, 'message': 'আমার স্বামী আমাকে মারে। আমি কি করতে পারি?'}
)
print(response.json()['response'])
"
```

## Deployment

### Railway

1. Create new project on [Railway](https://railway.app)
2. Connect GitHub repository
3. Add environment variables:
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL=gpt-5-nano`
4. Deploy!

### Render

1. Create new Web Service on [Render](https://render.com)
2. Connect GitHub repository
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables
6. Deploy!

## Roadmap

### MVP (Current)
- ✅ 9/12 legal intents working
- ✅ gpt-5-nano integration
- ✅ Tool-based architecture
- ✅ Safety-first responses
- ✅ Docker support

### Future Enhancements
- [ ] Upgrade to gpt-5.1-mini (when available)
- [ ] Improve prompt engineering for better intent detection
- [ ] Add Bengali NLP for better query understanding
- [ ] Frontend web interface
- [ ] WhatsApp/SMS integration
- [ ] Analytics dashboard
- [ ] Multi-turn conversation improvement
- [ ] Voice input/output support

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Legal content curated by Bangladesh legal experts
- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [OpenAI](https://openai.com/)
- Optional persistence with [Supabase](https://supabase.com/)

## Support

For issues, questions, or contributions:
- 📧 Email: support@ainbandhu.org
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ain-bandhu/issues)
- 📖 Docs: [Full Documentation](https://docs.ainbandhu.org)

---

**Disclaimer**: This AI assistant provides general legal information only and should not be considered legal advice. Users should consult with qualified legal professionals for specific legal matters.
