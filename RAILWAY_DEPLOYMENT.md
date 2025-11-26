# Railway Deployment Guide (2025)

## Prerequisites
- GitHub account with your code pushed
- Railway account (sign up at https://railway.app)
- Environment variables ready

## Step 1: Create Railway Project

1. Go to https://railway.app/new
2. Click "Deploy from GitHub repo"
3. Select your repository: `rarba/brac-final` (or whatever your repo is)
4. Railway will auto-detect the Dockerfile

## Step 2: Configure Environment Variables

In the Railway dashboard, go to your project → Variables tab and add:

```
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-5-nano
SUPABASE_URL=https://mqfegmiuakfgbcksxdam.supabase.co
SUPABASE_KEY=sb_publishable_q6Ckv6oIrL9NlA0lOcH03Q_qBtEPOtf
```

**Important**: Do NOT add a `PORT` variable - Railway automatically sets this.

## Step 3: Deploy

1. Railway will automatically deploy after you add the variables
2. Wait for the build to complete (2-3 minutes)
3. Once deployed, Railway will provide you with a public URL like:
   `https://your-app-name.up.railway.app`

## Step 4: Verify Deployment

Test the health endpoint:
```bash
curl https://your-app-name.up.railway.app/health
```

Should return:
```json
{"status": "healthy", "version": "1.0.0"}
```

Test a chat request:
```bash
curl -X POST https://your-app-name.up.railway.app/chat/new \
  -H "Content-Type: application/json" \
  -d '{"user_id": "test-user"}'
```

Then send a message:
```bash
curl -X POST https://your-app-name.up.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "SESSION_ID_FROM_ABOVE",
    "message": "আমার স্বামী আমাকে মারে। আমি কি করতে পারি?"
  }'
```

## Step 5: Monitor

- View logs in Railway dashboard under "Deployments" → "View Logs"
- Check metrics in the "Metrics" tab
- Monitor costs in "Usage" tab

## Troubleshooting

### Build fails
- Check Dockerfile syntax
- Ensure requirements.txt is up to date
- Check Railway build logs

### App crashes on startup
- Verify all environment variables are set correctly
- Check Railway logs for error messages
- Ensure Supabase credentials are correct

### Port binding errors
- Don't manually set PORT - Railway does this automatically
- Our Dockerfile uses `${PORT:-8000}` which Railway overrides

## Cost Estimation

With gpt-5-nano and expected usage:
- **Railway**: ~$5-10/month for a small app (usage-based)
- **Supabase**: Free tier (up to 500MB database, 2GB bandwidth)
- **OpenAI API**: ~$0.50-2/month with gpt-5-nano (very cheap)

**Total estimated cost**: ~$6-12/month for MVP

## Next Steps After Deployment

1. Update frontend with the Railway URL
2. Test all 12 intents on production
3. Monitor analytics in Supabase dashboard
4. Consider adding:
   - Custom domain
   - Rate limiting
   - CORS configuration (if needed for frontend)
