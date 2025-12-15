# Database Configuration Notes

## ⚠️ SECURITY WARNING
This file contains notes about database configuration. It should NOT be committed with actual credentials. The actual DATABASE_URL should only be stored in:
- Vercel Environment Variables (for production)
- Local `.env` file (for development, which is in .gitignore)

## DATABASE_URL Configuration

The DATABASE_URL for this project has been provided and should be configured in Vercel.

### Where to Add It

**For Production (Vercel):**
1. Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add variable:
   - Name: `DATABASE_URL`
   - Value: Your Neon PostgreSQL connection string
   - Environment: Production, Preview, Development (all)

**For Local Development:**
1. Copy `.env.example` to `.env`
2. Set `DATABASE_URL` in `.env`
3. The `.env` file is already in `.gitignore` and will not be committed

### Connection String Format

The format should be:
```
postgresql://[username]:[password]@[host].[region].neon.tech/[database]?sslmode=require
```

Components:
- **username**: Database user (e.g., `neondb_owner`)
- **password**: User password
- **host**: Database host endpoint (e.g., `ep-quiet-hat-agtqdlpy-pooler`)
- **region**: AWS region (e.g., `eu-central-1`)
- **database**: Database name (e.g., `neondb`)
- **sslmode**: Always use `require` for secure connections

### Important Notes

1. **Always use pooler**: The `-pooler` suffix in the host ensures connection pooling
2. **Include sslmode=require**: This ensures secure, encrypted connections
3. **Never commit credentials**: Always use environment variables
4. **Rotate regularly**: Change passwords periodically for security

## Verifying Connection

After configuration, test the connection:

```bash
# Visit this endpoint
https://your-app.vercel.app/api/init

# Expected response
{
  "message": "Database initialized successfully. Tables created and sample data seeded if empty.",
  "info": "Note: This endpoint only seeds data if tables are empty to prevent duplicates.",
  "seededPinpoints": 3,
  "success": true
}
```

If you get an error about DATABASE_URL missing, the environment variable is not properly set.

## Database Schema

The initialization creates these tables:

### `pinpoints` Table
- `id` (SERIAL PRIMARY KEY)
- `latitude` (DECIMAL)
- `longitude` (DECIMAL)
- `title` (VARCHAR)
- `description` (TEXT)
- `sound_url` (TEXT) - Can be external URL or `/api/sounds?id=X`
- `icon` (VARCHAR) - Emoji or symbol
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### `sounds` Table
- `id` (SERIAL PRIMARY KEY)
- `filename` (VARCHAR)
- `data` (BYTEA) - Binary audio data
- `mime_type` (VARCHAR)
- `size` (INTEGER)
- `created_at` (TIMESTAMP)

### `map_config` Table
- `id` (SERIAL PRIMARY KEY)
- `tile_layer_url` (TEXT)
- `center_lat` (DECIMAL)
- `center_lng` (DECIMAL)
- `zoom_level` (INTEGER)
- `max_zoom` (INTEGER)
- `min_zoom` (INTEGER)
- `attribution` (TEXT)
- `updated_at` (TIMESTAMP)

## Neon Database Features

Your Neon PostgreSQL database includes:

1. **Connection Pooling**: Automatically managed via `-pooler` endpoint
2. **Serverless**: Scales to zero when not in use
3. **Branching**: Create database branches for testing
4. **Point-in-Time Recovery**: Restore to any point in time
5. **Automatic Backups**: Daily backups included

## Monitoring

Monitor your database at:
- Neon Dashboard: https://neon.tech
- Vercel Functions Tab: See database query logs
- Application endpoint: `/api/config` to verify connectivity

## Troubleshooting Connection Issues

### "Error connecting to database: fetch failed"
- Verify DATABASE_URL is correctly set in Vercel
- Check Neon database is not suspended
- Verify network connectivity

### "DATABASE_URL manquante"
- DATABASE_URL environment variable not set
- Redeploy after adding the variable

### "SSL connection required"
- Add `?sslmode=require` to connection string

## Security Best Practices

✅ **DO:**
- Store DATABASE_URL in Vercel environment variables
- Use strong passwords
- Enable Neon IP allowlist if needed
- Rotate passwords regularly
- Monitor database access logs

❌ **DON'T:**
- Commit DATABASE_URL to Git
- Share credentials publicly
- Use weak passwords
- Disable SSL
- Leave database publicly accessible without auth

## Need Help?

- Neon Documentation: https://neon.tech/docs
- Vercel Environment Variables: https://vercel.com/docs/environment-variables
- Troubleshooting Guide: [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

**Remember**: The actual DATABASE_URL with credentials should never be committed to the repository. Always use environment variables and keep credentials secure.
