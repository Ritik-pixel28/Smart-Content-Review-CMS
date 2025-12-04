# Quick Deployment Guide

## Fastest Option: Railway (5 minutes)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Railway**
   - Go to https://railway.app
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add PostgreSQL database (click "New" → "Database" → "PostgreSQL")
   
3. **Set Environment Variables** (in Railway dashboard)
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   DJANGO_SETTINGS_MODULE=smartcms.settings.production
   ```

4. **Deploy & Migrate**
   Railway auto-deploys. Then run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

Your site will be live at: `https://your-project.railway.app`

## Files Created for Deployment
- ✅ `Procfile` - Deployment commands
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - Dependencies (updated)
- ✅ `.env.example` - Environment variables template
- ✅ `smartcms/settings/production.py` - Production settings

See full guide in DEPLOYMENT.md
