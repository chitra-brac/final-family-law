# Deployment Guide - Ain Bandhu

This guide covers deploying Ain Bandhu to production using Railway or Render.

## Prerequisites

- GitHub account
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- (Optional) Supabase account for persistence

## Option 1: Deploy to Railway (Recommended)

Railway offers easy deployment with automatic HTTPS and custom domains.

### Steps

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/ain-bandhu.git
git push -u origin main
```

2. **Create Railway Project**
- Go to [Railway](https://railway.app)
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your `ain-bandhu` repository

3. **Configure Environment Variables**

In Railway dashboard, add these variables:
```
OPENAI_API_KEY=sk-proj-your-key-here
OPENAI_MODEL=gpt-5-nano
DEBUG=False
```

Optional (for Supabase):
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

4. **Deploy**
- Railway will auto-detect the Dockerfile and build
- Wait for deployment to complete (~2-3 minutes)
- Get your public URL: `https://your-app.railway.app`

5. **Test the Deployment**
```bash
curl https://your-app.railway.app/health
```

### Railway Configuration

The included `railway.json` configures:
- Dockerfile-based builds
- Auto-restart on failure
- Health checks

## Option 2: Deploy to Render

Render provides free tier for testing (spins down after inactivity).

### Steps

1. **Push to GitHub** (same as Railway step 1)

2. **Create Render Web Service**
- Go to [Render](https://render.com)
- Click "New +" → "Web Service"
- Connect your GitHub repository

3. **Configure Build**
- **Name**: ain-bandhu
- **Environment**: Docker
- **Dockerfile Path**: `Dockerfile`
- **Instance Type**: Free (or Starter for production)

4. **Add Environment Variables**

In the Environment tab:
```
OPENAI_API_KEY=sk-proj-your-key-here
OPENAI_MODEL=gpt-5-nano
DEBUG=False
PORT=8000
```

5. **Deploy**
- Click "Create Web Service"
- Wait for build and deployment (~5 minutes)
- Get your URL: `https://ain-bandhu.onrender.com`

6. **Test the Deployment**
```bash
curl https://ain-bandhu.onrender.com/health
```

### Render Notes

- **Free Tier**: Spins down after 15 min inactivity (50s cold start)
- **Starter Tier**: $7/month, always on
- Auto-deploys on git push to main branch

## Option 3: Deploy with Docker (Self-Hosted)

For VPS deployment (DigitalOcean, AWS, etc.)

### Using Docker Compose

1. **Install Docker & Docker Compose**
```bash
# On Ubuntu
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo apt install docker-compose
```

2. **Clone Repository**
```bash
git clone https://github.com/yourusername/ain-bandhu.git
cd ain-bandhu
```

3. **Create .env File**
```bash
cp .env.example .env
# Edit .env with your API keys
nano .env
```

4. **Start Service**
```bash
docker-compose up -d
```

5. **Check Logs**
```bash
docker-compose logs -f
```

6. **Setup Nginx Reverse Proxy** (Optional)

Create `/etc/nginx/sites-available/ain-bandhu`:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/ain-bandhu /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

7. **Setup SSL with Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### Using Docker Run

```bash
docker run -d \
  -p 8000:8000 \
  -e OPENAI_API_KEY=sk-proj-your-key \
  -e OPENAI_MODEL=gpt-5-nano \
  --name ain-bandhu \
  --restart unless-stopped \
  ain-bandhu
```

## Post-Deployment

### Health Check

Test your deployment:
```bash
# Health check
curl https://your-domain.com/health

# Create session
curl -X POST https://your-domain.com/chat/new

# Send test message
curl -X POST https://your-domain.com/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "test-id",
    "message": "আমার স্বামী আমাকে মারে। আমি কি করতে পারি?"
  }'
```

### Monitoring

#### Railway
- Built-in metrics dashboard
- Auto-scaling available on Pro plan
- Logs accessible in dashboard

#### Render
- Built-in metrics and logs
- Email alerts for downtime
- Auto-scaling on paid plans

#### Self-Hosted
Use monitoring tools:
```bash
# Install monitoring stack
docker run -d --name prometheus prom/prometheus
docker run -d --name grafana grafana/grafana
```

### Performance Optimization

1. **Enable Response Caching** (for repeated queries)
2. **Add Redis** (for session management)
3. **Setup CDN** (for static assets)
4. **Use Load Balancer** (for high traffic)

### Scaling

**Current Performance:**
- Single instance handles ~100 concurrent users
- Avg response time: 18-20s
- Cost: ~$0.001/query

**For 1000+ concurrent users:**
- Deploy multiple instances behind load balancer
- Use Redis for shared session state
- Consider upgrading to gpt-5.1-mini for better performance

## Troubleshooting

### Build Fails

**Error**: `ModuleNotFoundError`
- Check `requirements.txt` includes all dependencies
- Verify Python version (3.12+)

**Error**: `Docker build timeout`
- Increase build timeout in Railway/Render settings
- Or build locally and push image to registry

### Runtime Errors

**Error**: `OPENAI_API_KEY not found`
- Verify environment variable is set correctly
- No quotes around the key value

**Error**: `Model 'gpt-5-nano' not found`
- Check your OpenAI account has access to gpt-5-nano
- Fallback: Use `gpt-4o-mini` or `gpt-4-turbo`

**Error**: `High latency`
- gpt-5-nano avg: 18-20s (normal)
- Check OpenAI API status
- Consider using gpt-4o-mini for faster responses

### Health Check Fails

```bash
# Check logs
docker logs ain-bandhu

# Test locally
curl http://localhost:8000/health

# Check port binding
netstat -tulpn | grep 8000
```

## Cost Estimates

### OpenAI API Costs (gpt-5-nano)

| Usage | Queries/Day | Cost/Month |
|-------|-------------|------------|
| Low | 50 | $1.50 |
| Medium | 500 | $15 |
| High | 5,000 | $150 |
| Very High | 50,000 | $1,500 |

### Hosting Costs

| Platform | Free Tier | Paid Tier | Notes |
|----------|-----------|-----------|-------|
| Railway | $5 credit | $5-20/month | Best for production |
| Render | Limited (spins down) | $7/month | Good for testing |
| DigitalOcean | - | $6/month | Full control |
| AWS/GCP | Free 1 year | $10-50/month | Enterprise scale |

### Total Monthly Cost Estimate

- **Development**: $0-5 (free tiers + low usage)
- **Small Production** (500 users/day): $15 API + $7 hosting = **$22/month**
- **Large Production** (5,000 users/day): $150 API + $20 hosting = **$170/month**

## Security Checklist

Before going to production:

- [ ] Set `DEBUG=False`
- [ ] Use strong API keys (rotate regularly)
- [ ] Configure CORS properly (not `["*"]`)
- [ ] Enable HTTPS (auto with Railway/Render)
- [ ] Add rate limiting (already configured)
- [ ] Setup logging and monitoring
- [ ] Regular security updates
- [ ] Backup Supabase database (if using)

## Backup & Recovery

### Backup Data
```bash
# Export conversations from Supabase
# Go to: Dashboard → Table Editor → conversations → Export as CSV

# Backup Docker volumes
docker run --rm -v ain-bandhu_data:/data -v $(pwd):/backup \
  ubuntu tar czf /backup/data-backup.tar.gz /data
```

### Restore
```bash
# Import to Supabase
# Dashboard → Table Editor → conversations → Import CSV

# Restore Docker volumes
docker run --rm -v ain-bandhu_data:/data -v $(pwd):/backup \
  ubuntu tar xzf /backup/data-backup.tar.gz -C /
```

## Support

- 📧 Email: support@ainbandhu.org
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ain-bandhu/issues)
- 📖 Docs: [Full Documentation](https://docs.ainbandhu.org)

---

**Next Steps**: After deployment, monitor performance and user feedback to optimize the system!
