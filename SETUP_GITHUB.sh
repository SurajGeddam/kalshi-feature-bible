#!/bin/bash

# Setup script for GitHub repository
# Run this script to initialize git and prepare for GitHub push

echo "🚀 Setting up GitHub repository for Kalshi Feature Bible..."
echo ""

# Check if already a git repo
if [ -d .git ]; then
    echo "⚠️  Git repository already initialized"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    git init
    echo "✅ Git repository initialized"
fi

# Add all files
echo "📦 Adding files..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Comprehensive Kalshi Feature Bible

- 106 screenshots documented
- 54 features analyzed  
- 9 bugs logged
- Complete competitor analysis for Opinion Kings

Documentation includes:
- KALSHI_FEATURE_BIBLE.md: Complete feature documentation
- SCREENSHOT_INDEX.md: Screenshot index
- BUG_LOG.md: Tracked bugs and issues
- DELTA_TABLE.md: Feature comparison table
- TRADING_EXPERIENCE.md: User trading insights"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Create a new repository on GitHub (https://github.com/new)"
echo "2. Copy the repository URL"
echo "3. Run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "📖 For more options, see VIEWING_GUIDE.md"

