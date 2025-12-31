# Quick Push to GitHub

## Simple Solution: Use Personal Access Token

**Run this command:**
```bash
cd "/Users/surajgeddam/Desktop/Opinion Kings"
git push -u origin main
```

**When prompted for credentials:**
1. **Username:** `SurajGeddam`
2. **Password:** Use a Personal Access Token (NOT your GitHub password)

## Get Your Token (2 minutes):

1. Go to: https://github.com/settings/tokens/new
2. Name: "Kalshi Docs"
3. Expiration: 90 days (or your choice)
4. Check: ✅ **repo** (Full control of private repositories)
5. Click "Generate token"
6. **Copy the token** (starts with `ghp_`)

## Then Push:

```bash
git push -u origin main
```

- Username: `SurajGeddam`
- Password: Paste your token

**Done!** Your docs will be on GitHub.

