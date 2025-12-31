# Delta Table: Kalshi vs Opinion Kings

> **Purpose:** Living roadmap input comparing Kalshi features to Opinion Kings plans. This drives prioritization and differentiation strategy.

---

## Feature Comparison

| Feature | Kalshi | Opinion Kings Plan | Priority | Complexity | Notes |
|---------|--------|-------------------|----------|------------|-------|
| Landing page with live markets | Yes | Modify | P0 | M | Show live markets but fix bugs, improve chart labels |
| Sign up modal | Yes | Modify | P0 | S | Center modal, add close button, improve UX |
| Log in modal | Yes | Modify | P0 | S | Add password field or clarify passwordless, add forgot password |
| Social login (Google/Apple) | Yes | Copy | P1 | M | OAuth integration required |
| Category navigation filters | Yes | Copy | P1 | S | Multiple navigation layers for discovery |
| Market tags/filters | Yes | Copy | P1 | S | Specific market category tags |
| Live market data display | Yes | Copy | P0 | M | Real-time scores, probabilities, charts |
| Market volume display | Yes | Modify | P2 | S | Add context/comparison |
| Promotional trust sections | Yes | Copy | P1 | S | Legal, portfolio growth, funding options |
| Price chart visualization | Yes | Modify | P1 | M | Fix axis labels, improve clarity |
| Email sign-up with validation | Yes | Modify | P0 | S | Real-time validation, improve error messages and UX |
| Legal terms modal | Yes | Modify | P1 | S | Center modal, add summaries, improve organization |
| Password creation with real-time validation | Yes | Copy | P0 | S | Excellent UX pattern - real-time checkmarks, clear requirements |
| Duplicate account detection | Yes | Modify | P1 | S | Dedicated page, but improve clarity of social login buttons |
| OAuth callback flow | Yes | Copy | P0 | M | Seamless redirect after OAuth, no intermediate screens |
| Apple OAuth first-time flow | Yes | Copy | P0 | M | Standard OAuth flow, verify subsequent auto-login optimization |
| Homepage trending (logged in) | Yes | Modify | P0 | M | Default to trending, watchlist/portfolio sidebar, infinite scroll, "For you" carousel (auto-rotate 7 markets with arrows) - add sort/filter to "For you" |
| New markets with Unique/Repeating tabs | Yes | Modify | P1 | M | "New" markets section with Unique (one-time) and Repeating (daily/weekly/monthly) tabs, URL routing - add sort/filter, time-based filtering, clear ordering logic |
| All category with advanced filtering/sorting | Yes | Modify | P1 | M | Comprehensive filtering (frequency, status) and sorting (trending, volume, liquidity, etc.) with toggles - add filter persistence, visual indicators, URL filters, filter reset |
| Politics category with sub-categories | Yes | Modify | P1 | M | Sub-categories (All, Trump Agenda, Culture war, etc.) with path-based URLs (`/category/politics/[subcategory]`), scrollable navigation - add bidirectional scrolling, sub-category counts, consistent URL patterns |
| Sports category with sportsbook interface | Yes | Modify | P1 | L | Sportsbook-style interface with left sidebar, live scores, market types (Games/Futures/Awards), trading panel defaults to first market, different URL pattern (`/sports/`) - add consistent URL patterns, trading panel control, search within Sports |
| Category page types analysis | Yes | Modify | P1 | M | Three category types: Type 1 (Sub-categories with path URLs), Type 2 (Filter dropdowns), Type 3 (Sportsbook) - standardize URL patterns, consistent navigation, sub-category counts, bidirectional scrolling |
| Live events calendar page | Yes | Modify | P1 | M | Live events page (`/calendar`) with left sidebar categories, live events list, right trading panel - use clearer URL (`/live`), add date navigation, time filters, trading panel control |
| Ideas feed page (main social platform) | Yes | Modify | P1 | L | Main Ideas feed (`/ideas/feed`) with left sidebar navigation, feed tabs (Ideas/Live trades/Market builder), post input, time filters, embedded markets, "Buy" buttons - feed updates live, unified post button, search within Ideas, category filters |
| Live trades tab | Yes | Modify | P1 | M | Live trades tab showing real-time trading activity (updates live and rapidly) - add clickable trades, clarify "Minimum amount" filter, category filters, time context, search |
| Market builder tab | Yes | Modify | P1 | L | Market builder tab for submitting market proposals to Kalshi team, viewing all proposals and status - add status updates, notification system, proposal editing, duplicate prevention, filtering, search |
| User profile page with tabs | Yes | Modify | P1 | M | User profile page with stats, privacy options (hide positions/trades), multiple tabs (Posts, Replies, Bookmarks, etc.) - simplify navigation, reduce UI complexity, align left sidebar with tabs |
| Community guidelines | Yes | Modify | P2 | S | Community Guidelines PDF document - convert to HTML, add search, table of contents, anchor links |
| Contact Kalshi Support | Yes | Modify | P1 | M | Contact support page with email, Help Center - add live chat, ticket system, response time estimates, support hours |
| Kalshi Ideas help center | Yes | Copy | P2 | S | Help center page explaining Kalshi Ideas platform with embedded examples - add video tutorials, more examples |
| Posting restrictions (trade requirement) | Yes | Copy | P1 | M | Modal requiring user to make a trade before posting - improve messaging, show active positions, allow posting from active positions |
| Returns page (closed trades) | Yes | Modify | P1 | M | Returns page showing closed trades with returns (wins/losses) - supports posting from live positions, win/loss posts with comments toggle, different card displays (market card vs payout card), cashout posting - add filtering, sorting, return details, analytics, clearer card display logic, post type indicators |
| Cash deposit options | Yes | Modify | P1 | M | Cash deposit options page with payment methods (Google Pay, Debit card, Bank transfer, Crypto, Wire transfer) - CRITICAL: add Apple Pay support, improve fee transparency, add comparison view |
| Portfolio main page | Yes | Modify | P1 | M | Main Portfolio page showing portfolio value, recent change, cash balance, interest eligibility, tabs - add time period selector, portfolio chart, breakdown, analytics |
| Portfolio position cash out | Yes | Modify | P1 | M | Cash out option for positions with current value vs cash out value - CRITICAL: improve cash out availability (especially combos), explain value difference, add notifications, reduce spread, partial cash out |
| Order completion confirmation (single) | Yes | Modify | P1 | M | Order completion screen with receipt-style design, order details, social sharing - add order ID, navigation links, position preview, order receipt download |
| No counterparty modal (liquidity warning) | Yes | Modify | P1 | M | Modal warning when no counterparty available, with limit order option - add liquidity indicator, price display, time estimate, limit order management, notification preferences |
| Leaderboard Activity page | Yes | Modify | P1 | M | Leaderboard page showing top users across Profit, Volume, Predictions - add "My rank" indicator, user search, profile links, historical leaderboards, rewards |
| Notifications page | Yes | Modify | P1 | M | Notifications page with chronological alerts - FIX: notification icon not red when unread (user feedback), add unread indicator, filtering, search, mark as read |
| API Documentation Portal | Yes | TBD | P3 | L | API documentation portal on separate subdomain (docs.kalshi.com) - separate feature, may or may not be implemented for Opinion Kings (documented for reference) |
| Combo creation flow (mobile) | Yes | Modify | P1 | M | Combo creation interface for NBA/NFL with prediction cards, Yes/No selections, confirmation screen - FIX: save picks when closing (state persistence bug), add draft saving, undo functionality |
| Portfolio empty state | Yes | Modify | P1 | S | Add guidance and suggestions for next steps |
| Detailed market page with trading | Yes | Modify | P0 | L | Good core, but improve order flow clarity and balance warnings |
| More markets expandable list | Yes | Copy | P1 | S | Progressive disclosure pattern - excellent UX |
| Dynamic trading interface updates | Yes | Copy | P0 | M | Immediate feedback when selecting prediction - excellent UX |
| Dynamic rules display | Yes | Copy | P1 | S | Contextual rules for selected prediction - excellent UX |
| Logged-in discovery page | Yes | Modify | P0 | M | Good core, but fix content bleed bug, clarify badges |
| Calendar popup and event-based routing | Yes | Modify | P1 | M | Excellent routing system for navigating between related markets, add search/filter and date indicators |
| Ideas/Activity feed with embedded markets | Yes | Modify | P1 | L | Social feed with market cards, improve payout transparency and filtering |
| Timeline and payout section | Yes | Modify | P1 | S | Expandable timeline, add countdown timer and real-time updates |
| People are also buying recommendations | Yes | Modify | P1 | M | Activity-based recommendations, add personalization and more context |
| Market rules documentation system | Yes | Modify | P1 | M | PDF, help center, popup - add downloadable PDF, unified page, simplified language |
| Market page header actions | Yes | Copy | P1 | S | Copy link, download price history, watchlist toggle - add tooltips and visual feedback |
| Multi-market graph comparison | Yes | Modify | P1 | M | Compare up to 4 markets on graph, improve market selection UX, consider flexible limit |
| Graph settings menu | Yes | Copy | P2 | S | Toggles for forecast graph, editorial section, sell buttons, price notifications |
| Buy/Sell interface with contracts dropdown | Yes | Modify | P0 | M | Buy/Sell tabs, different dropdown options, defaults to contracts (marketing-driven), add transparency and user-friendly defaults |
| Orderbook popup for prediction details | Yes | Modify | P1 | M | Orderbook popup on prediction word click, separate Yes/No views, graph integration - add clear trigger, close button, order placement |
| Footer and legal disclosure | Yes | Modify | P1 | S | Three-column footer with company/social/product links, comprehensive risk disclosure - make risk disclosure more prominent, add search, improve mobile |
| Watchlist and Portfolio sort functionality | Yes | Modify | P1 | S | Sort functionality for Watchlist (3 options) and Portfolio (9 options), minimize/expand sidebar - add filter options, search, more sort options, sort indicator |

**Legend:**
- **Kalshi:** Yes/No + brief notes
- **Opinion Kings Plan:** Copy / Modify / Differentiate / Skip
- **Priority:** P0 (must have) / P1 (should have) / P2 (nice to have) / P3 (later)
- **Complexity:** S (Small) / M (Medium) / L (Large)

---

## By Category

### Onboarding
- **Sign up modal**: Yes - Right-aligned modal with Google/Apple/Email options → Modify (center it, add close button)
- **Log in modal**: Yes - Centered modal with Google/Apple/Email → Modify (clarify passwordless or add password field, add forgot password)
- **Social login**: Yes - Google and Apple OAuth → Copy (standard pattern)
- **Email validation**: Yes - Real-time validation with clear error messages → Modify (improve error messages, add format hints)
- **Legal terms modal**: Yes - Right-side modal with document list → Modify (center modal, add summaries, improve UX)
- **Password creation**: Yes - Real-time validation with green checkmarks → Copy (excellent UX pattern)
- **Duplicate account detection**: Yes - Dedicated page with multiple login options → Modify (show original auth method, add "try different email" option)
- **Apple OAuth flow**: Yes - Standard Apple OAuth page for first-time → Copy (verify subsequent auto-login works)

### Funding
_No entries yet_

### Discovery
- **Landing page**: Yes - Live markets, navigation, promotional sections → Modify (improve chart labels)
- **Homepage trending**: Yes - Defaults to trending, watchlist/portfolio sidebar, infinite scroll, "For you" carousel (auto-rotate 7 markets with arrows) → Modify (add sort/filter to "For you", show ordering logic)
- **New markets**: Yes - "New" markets section with Unique/Repeating tabs, URL routing, frequency labels → Modify (add sort/filter, time-based filtering, clear ordering logic)
- **All category filtering**: Yes - Comprehensive filtering (frequency, status) and sorting (trending, volume, liquidity, 50-50, etc.) with toggles (list view, exclude sports) → Modify (add filter persistence, visual indicators, URL filters, filter reset)
- **Politics sub-categories**: Yes - Sub-categories with path-based URLs, scrollable navigation → Modify (add bidirectional scrolling, sub-category counts, consistent URL patterns across all categories)
- **Sports sportsbook interface**: Yes - Sportsbook-style interface with left sidebar, live scores, market types, trading panel defaults to first market, different URL pattern → Modify (consistent URL patterns, trading panel control, search within Sports, allow deselecting market)
- **Category page types**: Yes - Three distinct types: Sub-categories (Politics, Culture, Crypto, etc.), Filter dropdowns (Mentions, All), Sportsbook (Sports) → Modify (standardize URL patterns, consistent navigation patterns, sub-category counts, bidirectional scrolling, category templates)
- **Live events calendar**: Yes - Live events page (`/calendar`) with left sidebar, live events list, right trading panel → Modify (clearer URL `/live`, date navigation, time filters, trading panel control, upcoming events view)
- **Ideas feed page**: Yes - Main Ideas feed (`/ideas/feed`) with left sidebar, feed tabs, post input, time filters, embedded markets, live updates → Modify (unified post button, search within Ideas, category filters, post editing)
- **Live trades tab**: Yes - Real-time trading activity feed (updates live and rapidly) → Modify (clickable trades, clarify filters, category filters, time context, search)
- **Market builder tab**: Yes - Market proposal submission system, view all proposals and status → Modify (status updates, notifications, proposal editing, duplicate prevention, filtering, search)
- **Category filters**: Yes - Trending, Politics, Sports, etc. → Copy (multiple navigation layers)
- **Market tags**: Yes - Pro Football, Bowl Games, etc. → Copy (specific market filters)
- **Live market display**: Yes - Scores, probabilities, charts → Copy (real-time engagement)
- **Market volume**: Yes - Shows total volume → Modify (add context/comparison)

### Market Page
- **Logged-in discovery page**: Yes - Account info, watchlist, featured markets → Modify (clarify badges, better organize related markets)
- **Detailed market page**: Yes - Trading interface, chart, contracts → Modify (improve order flow, add balance warnings)
- **More markets expandable list**: Yes - Progressive disclosure, shows 4-5 initially, expands to 15+ → Copy (excellent UX pattern)
- **Dynamic trading interface**: Yes - Updates immediately when selecting prediction → Copy (excellent UX pattern)
- **Dynamic rules display**: Yes - Rules update for selected prediction → Copy (excellent UX pattern)
- **OAuth callback flow**: Yes - Seamless redirect after OAuth → Copy (excellent UX pattern)
- **Calendar popup and event-based routing**: Yes - Calendar popup with Open/History tabs for navigating between event-based markets → Modify (add search/filter, date indicators, favorites)
- **Timeline and payout section**: Yes - Expandable timeline showing market lifecycle and payout schedule → Modify (add countdown timer, real-time updates, payout status)
- **People are also buying recommendations**: Yes - Activity-based recommendations showing top 3 (expandable to top 10) → Modify (add personalization, more context, transparent algorithm)
- **Market page header actions**: Yes - Copy link, download price history, watchlist toggle in header → Copy (add tooltips, visual feedback, download options)
- **Multi-market graph comparison**: Yes - Compare up to 4 markets on graph with auto-update → Modify (improve market selection UX, consider flexible limit)
- **Graph settings menu**: Yes - Toggles for forecast graph, editorial section, sell buttons, price notifications → Copy (good customization options)

### Trading
- **Buy/Sell interface**: Yes - Buy/Sell tabs with contracts dropdown, defaults to contracts → Modify (add transparency, user-friendly defaults, limit order education)
- **Orderbook popup**: Yes - Orderbook popup on prediction word click with Trade Yes/No/Graph tabs → Modify (add clear trigger, close button, order placement from orderbook)

### Portfolio
- **Portfolio empty state**: Yes - Shows "No open positions" → Modify (add guidance, suggestions, portfolio value display)
- **Watchlist and Portfolio sort**: Yes - Sort functionality with different options for Watchlist (3) vs Portfolio (9), minimize/expand sidebar → Modify (add filter, search, more sort options, sort indicator)

### Social
- **Ideas/Activity feed**: Yes - Social feed with user posts, comments, embedded market cards → Modify (improve payout transparency, add filtering, show market status)

### Support
- **Market rules documentation**: Yes - PDF, help center, popup for rules → Modify (downloadable PDF, unified page, simplified language)
- **Footer and legal disclosure**: Yes - Three-column footer with company/social/product links, comprehensive risk disclosure → Modify (make risk disclosure more prominent, add search, improve mobile, remove redundancies)

### Settings
_No entries yet_

---

## Quick Add Template

When documenting a new feature:

1. Add row to main table
2. Add entry to category section
3. Update priority/complexity as needed
4. Link to feature writeup in main bible

---

## Strategic Notes

**Copy:** Features we should replicate (proven patterns)

**Modify:** Features we should adapt (good idea, needs improvement)

**Differentiate:** Features we should do differently (competitive advantage)

**Skip:** Features we should avoid (not aligned with our vision)

