# Quick Fix for Sound Issues - TL;DR

## The Problem
Sounds not playing → falling back to beep sound.

## The Cause
`DATABASE_URL` not configured in Vercel → app uses external URLs that fail.

## The Solution (5 Minutes)

### 1. Add DATABASE_URL to Vercel
1. Go to https://vercel.com → Your Project → Settings → Environment Variables
2. Add: `DATABASE_URL` = your Neon PostgreSQL connection string
3. Save

### 2. Add ADMIN_PASSWORD_HASH to Vercel
1. Run locally: `npm run generate-password YourPassword`
2. Copy the hash
3. Add to Vercel: `ADMIN_PASSWORD_HASH` = the hash
4. Save

### 3. Redeploy
1. Deployments tab → Latest deployment → ... → Redeploy
2. **Uncheck** "Use existing Build Cache"
3. Wait for deployment

### 4. Initialize Database
Visit: `https://your-app.vercel.app/api/init`

### 5. Upload Sounds (Optional but Recommended)
1. Visit: `https://your-app.vercel.app/admin`
2. Login with your password
3. Sons tab → Upload audio files
4. Note the IDs returned

### 6. Update Pinpoints (Optional but Recommended)
1. Points tab → Edit each pinpoint
2. Change sound URL from external to: `/api/sounds?id=1`
3. Save

### 7. Test
1. Clear browser cache (Ctrl+F5)
2. Click marker → Play sound
3. Should work! ✓

## Need More Details?
- Complete guide: [FIXING_SOUNDS.md](./FIXING_SOUNDS.md)
- Setup help: [VERCEL_SETUP.md](./VERCEL_SETUP.md)
- Troubleshooting: [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

## Still Not Working?
Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) or open a GitHub issue.
