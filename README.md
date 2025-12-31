# Kalshi Feature Bible - Opinion Kings Competitor Analysis

> Comprehensive, screenshot-driven teardown of Kalshi to inform Opinion Kings product development.

## Overview

This repository contains a complete feature-by-feature analysis of Kalshi, documenting:
- UX flows and product behavior
- What we like/dislike
- Implementation hypotheses
- Bugs and edge cases
- Opinion Kings implications

## Executive Summary

This documentation represents a comprehensive competitive analysis of Kalshi, capturing 106 screenshots across 54 features, 9 documented bugs, and detailed user experience insights from real-world trading. While Opinion Kings and Kalshi are similar prediction market platforms, this analysis serves as a strategic reference to understand proven UX patterns, identify pain points to avoid, and discover opportunities to differentiate. The documentation includes a feature comparison table (DELTA_TABLE.md) that maps each Kalshi feature to our product strategy—whether to copy, modify, differentiate, or skip—ensuring we build on what works while creating a unique value proposition that aligns with our vision for Opinion Kings.

## Quick Start

**New to this documentation?** Start here:
1. Read this README for overview
2. Check **[VIEWING_GUIDE.md](./VIEWING_GUIDE.md)** for best ways to view and share
3. Browse **[KALSHI_FEATURE_BIBLE.md](./KALSHI_FEATURE_BIBLE.md)** for detailed features
4. Review **[DELTA_TABLE.md](./DELTA_TABLE.md)** for Opinion Kings planning

**Want to share with your team?**
- **GitHub (Recommended):** See [VIEWING_GUIDE.md](./VIEWING_GUIDE.md) for setup
- **Quick setup:** Run `./SETUP_GITHUB.sh` to initialize git repository

## Documentation Structure

### Main Documents

- **[KALSHI_FEATURE_BIBLE.md](./KALSHI_FEATURE_BIBLE.md)** - Complete feature documentation with embedded screenshots
- **[SCREENSHOT_INDEX.md](./SCREENSHOT_INDEX.md)** - Index of all screenshots
- **[BUG_LOG.md](./BUG_LOG.md)** - Tracked bugs and UX issues
- **[DELTA_TABLE.md](./DELTA_TABLE.md)** - Kalshi vs Opinion Kings feature comparison
- **[TRADING_EXPERIENCE.md](./TRADING_EXPERIENCE.md)** - Real-world trading process, thoughts, and user experience insights
- **[VIEWING_GUIDE.md](./VIEWING_GUIDE.md)** - Best ways to view and share this documentation

### Screenshot Organization

Screenshots are organized by feature category:
- `screenshots/01-onboarding/` - Sign up, login, KYC flows
- `screenshots/02-funding/` - Deposits, withdrawals, payment methods
- `screenshots/03-discovery/` - Landing page, market discovery, categories
- `screenshots/04-market-page/` - Individual market pages
- `screenshots/05-order-ticket/` - Trading interface, order placement
- `screenshots/06-portfolio/` - Positions, P&L, history
- `screenshots/07-social/` - Leaderboards, sharing, referrals
- `screenshots/08-settlement-support/` - Support, disputes, settlement
- `screenshots/99-misc/` - Other observations

## Quick View: Screenshots

### Discovery

#### Landing Page (Logged Out)
![010 Landing page](screenshots/03-discovery/010-discovery-landing-page.png)
*Main discovery page showing live markets, navigation, and promotional sections*

### Onboarding

#### Sign Up Modal
![011 Sign up modal](screenshots/01-onboarding/011-onboarding-signup-modal.png)
*Registration modal with Google, Apple, and email options*

#### Log In Modal
![012 Log in modal](screenshots/01-onboarding/012-onboarding-login-modal.png)
*Login modal with Google, Apple, and email options*

#### Email Sign-Up with Validation
![013 Email validation](screenshots/01-onboarding/013-onboarding-email-validation.png)
*Email input screen with real-time validation error*

#### Legal Terms Modal
![014 Legal terms modal](screenshots/01-onboarding/014-onboarding-legal-terms-modal.png)
*Legal terms popup showing all agreements and policies*

#### Password Creation
![015 Password creation](screenshots/01-onboarding/015-onboarding-password-creation.png)
*Password creation screen with real-time requirement validation*

#### Duplicate Account Detection
![016 Duplicate account](screenshots/01-onboarding/016-onboarding-duplicate-account.png)
*Page shown when user tries to sign up with existing email (handles cross-method duplicates)*

#### Apple OAuth Flow
![018 Apple OAuth](screenshots/01-onboarding/018-onboarding-apple-oauth.png)
*Apple ID authentication page for first-time OAuth authorization*

### 02 - Account / Funding

#### Cash Deposit Options
![095 Cash deposit options](screenshots/02-account/095-account-cash-deposit-options.png)
*Cash deposit options page showing payment methods (Google Pay, Debit card, Bank transfer, Crypto, Wire transfer) - NOTE: Apple Pay is missing, which is a critical gap for iOS users*

### 03 - Discovery

#### Homepage Trending (Logged In)
![019 Homepage trending](screenshots/03-discovery/019-discovery-homepage-trending.png)
*Logged-in homepage defaulting to trending markets with watchlist/portfolio sidebar*

### 04 - Market Page

#### Logged-In Discovery Page (Post-OAuth)
![017 Logged-in discovery page](screenshots/04-market-page/017-market-page-logged-in-discovery.png)
*Discovery page after successful OAuth login - shows account balance, watchlist, and featured markets*

#### Detailed Market Page with Trading
![021 Detailed market page with trading](screenshots/04-market-page/021-market-page-detailed-trading.png)
*Market page with trading interface, chart, and contract selection - clickable watchlist/portfolio items*

#### More Markets & Dynamic Trading Interface
![022 More markets expanded](screenshots/04-market-page/022-market-page-more-markets-expanded.png)
![023 Prediction selected](screenshots/04-market-page/023-market-page-prediction-selected.png)
![024 Rules display](screenshots/04-market-page/024-market-page-rules-display.png)
*"More markets" expandable list, dynamic trading interface updates, and contextual rules display*

#### Calendar Popup and Event-Based Routing
![028 Calendar popup 1](screenshots/04-market-page/028-market-page-calendar-popup-1.png)
![029 Calendar popup 2](screenshots/04-market-page/029-market-page-calendar-popup-2.png)
![030 Determined history market](screenshots/04-market-page/030-market-page-determined-history.png)
![031 Calendar open market](screenshots/04-market-page/031-market-page-calendar-open-market.png)
*Calendar popup with Open/History tabs for navigating between event-based markets - excellent routing system for mentions markets*

#### Timeline and Payout Section
![038 Timeline and payout](screenshots/04-market-page/038-market-page-timeline-payout.png)
*Expandable timeline section showing market lifecycle, closure conditions, and payout schedule*

#### People are also buying Recommendations
![039 People are also buying](screenshots/04-market-page/039-market-page-people-also-buying.png)
*Activity-based recommendations showing top 3 markets (expandable to top 10) - not restricted to mentions, shows related markets*

#### Market Rules Documentation
![040 Full rules PDF](screenshots/04-market-page/040-market-page-full-rules-pdf.png)
![041 Help center rules](screenshots/08-settlement-support/041-support-help-center-rules.png)
![042 Rules summaries popup](screenshots/04-market-page/042-market-page-rules-summaries-popup.png)
*Three access points for rules: PDF (full contract terms), Help center (documentation), Popup (quick definitions) - plus header actions: copy link, download price history, watchlist toggle*

### 06 - Portfolio

#### Portfolio Main Page
![096 Portfolio main page](screenshots/06-portfolio/096-portfolio-page-main.png)
*Main Portfolio page showing portfolio value, recent change, cash balance, interest eligibility, and tabs (Position, Resting, History)*

#### Portfolio Empty State
![020 Portfolio empty state](screenshots/06-portfolio/020-portfolio-empty-state.png)
*Portfolio tab showing empty state when user has no open positions*

### 07 - Social

#### Ideas/Activity Feed
![032 Ideas/Activity feed 1](screenshots/07-social/032-social-ideas-activity-feed-1.png)
![033 Ideas/Activity feed 2](screenshots/07-social/033-social-ideas-activity-feed-2.png)
![034 Inline post input](screenshots/07-social/034-social-post-input-inline.png)
![035 Activity feed detailed](screenshots/07-social/035-social-activity-feed-detailed.png)
![036 Comment thread](screenshots/07-social/036-social-comment-thread.png)
![037 Ideas page](screenshots/07-social/037-social-ideas-page.png)
![082 Ideas feed page](screenshots/07-social/082-social-ideas-feed-page.png)
![083 Live trades tab](screenshots/07-social/083-social-live-trades-tab.png)
![084 Market builder tab](screenshots/07-social/084-social-market-builder-tab.png)
![086 Ideas feed combo card](screenshots/07-social/086-social-ideas-feed-combo-card.png)
![087 Profile replies tab](screenshots/07-social/087-social-profile-replies-tab.png)
![088 Profile bookmarks tab](screenshots/07-social/088-social-profile-bookmarks-tab.png)
![089 Profile posts tab](screenshots/07-social/089-social-profile-posts-tab.png)
![093 Post trade requirement modal](screenshots/07-social/093-social-post-trade-requirement-modal.png)
![094 Returns page](screenshots/07-social/094-social-returns-page.png)
![097 Leaderboard page](screenshots/07-social/097-social-leaderboard-page.png)
*Social feed with user posts, comments, embedded market cards, inline post creation, user profiles with stats, volume/leaderboard badges, dedicated idea pages, main Ideas feed page (`/ideas/feed`), Live trades tab (real-time trading activity), Market builder tab (market proposal system), user profile page with tabs and privacy options, posting restrictions (require trade to post), Returns page (closed trades with returns), Leaderboard Activity page (top users across Profit, Volume, Predictions) - unified feed including open and history markets*

### 08 - Settlement/Support

#### Help Center and Support
![041 Help center rules](screenshots/08-settlement-support/041-support-help-center-rules.png)
![090 Community guidelines PDF](screenshots/08-settlement-support/090-social-community-guidelines-pdf.png)
![091 Contact Kalshi Support](screenshots/08-settlement-support/091-support-contact-kalshi-support.png)
![092 Kalshi Ideas help](screenshots/08-settlement-support/092-support-kalshi-ideas-help.png)
*Help center pages for market rules, Community Guidelines PDF, Contact Kalshi Support page, and Kalshi Ideas help center*

### 09 - Notifications

#### Notifications Page
![098 Notifications page](screenshots/09-notifications/098-notifications-page.png)
*Notifications page showing chronological list of alerts (event updates, market settlements, price movements) - NOTE: Notification icon bug (not red when unread, user feedback)*

## How to Use This Repository

1. **Browse by Feature**: Check `KALSHI_FEATURE_BIBLE.md` for complete feature writeups
2. **Find Screenshots**: Use `SCREENSHOT_INDEX.md` to locate specific screenshots
3. **Track Issues**: Review `BUG_LOG.md` for bugs and UX problems
4. **Compare Features**: See `DELTA_TABLE.md` for Opinion Kings implementation plans

## Contributing

When adding new screenshots:
1. Save with format: `###-section-shortslug.png`
2. Place in appropriate folder
3. Documentation will be automatically updated

## Status

**Last Updated:** 2024-12-31  
**Screenshots Documented:** 106  
**Features Documented:** 54  
**Bugs Logged:** 9

---

*This is a living document. As we capture more screenshots and analyze more features, this bible will grow.*

