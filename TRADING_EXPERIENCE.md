# Trading Experience & Process Documentation

> **Purpose:** Document real-world trading process, user thoughts, pain points, and insights from actually using Kalshi to trade markets. This complements the feature documentation with actual usage patterns and user experience.

**Last Updated:** 2024-12-31  
**Status:** In Progress

---

## How to Use This Document

This document captures:
- **Trading workflow:** Step-by-step process of how you trade
- **Decision-making:** What you think about when making trades
- **Pain points:** Friction and confusion during trading
- **What works well:** Features that enhance your trading experience
- **Mental models:** How you understand and navigate the platform
- **Market selection:** How you choose which markets to trade
- **Risk management:** How you manage positions and risk
- **Platform comparison:** How Kalshi compares to other trading platforms (if applicable)

---

## Trading Process Overview

### Overall Platform Experience

**UI/UX Assessment:**
- **UI is relatively easy to use** - Platform is intuitive and user-friendly
- **Information sources:** Can use information from:
  - Personal knowledge
  - Other traders' insights (social feed, ideas, comments)
  - Market data and analysis available on platform

### Funding & Deposit Experience

**Bank Account Linking:**
- **Easy to link bank account** - Process was straightforward
- **Regular deposits via Apple Pay** - Primary funding method
- **Instant fund access** - Funds are immediately available after deposit via Apple Pay
  - No waiting period
  - Can trade immediately after depositing

**Insufficient Funds Flow:**
- **Smart deposit prompt:** If user wants to trade a market but doesn't have sufficient funds for selected trade amount, **deposit popup shows up instantly**
- **Seamless experience:** No friction - deposit option appears automatically when needed
- **Quick resolution:** User can deposit and continue with trade without losing context

**Deposit Confirmation & Auto-Signature:**
- **Auto-signature agreement:** After depositing, user sees deposit confirmation screen
- **No manual signing required:** Signature is auto-generated (e.g., "Suraj Geddam" appears automatically)
- **Easy to use:** User doesn't have to manually sign - reduces friction significantly
- **Confirmation details shown:**
  - "Deposit ready" status
  - Deposit method ("Deposit with Card")
  - Amount ($98)
  - Processing fee ($2)
  - Auto-generated signature
- **Quick action:** "Start trading" button appears immediately after deposit
- **Frictionless flow:** From deposit → auto-signature → ready to trade in seconds

### Combo Creation Experience

**Combo Creation Flow:**
- **Mobile interface:** Card-based layout for selecting predictions
- **Prediction selection:** Yes/No buttons for each prediction (light purple = selected, dark purple = unselected)
- **Percentage display:** Shows odds for each prediction (e.g., 37%, 40%, 41%)
- **Summary bar:** Shows trade amount, potential payout, and prediction count
- **Cross-sport combinations:** Can combine NBA and NFL predictions in one combo
- **Confirmation screen:** Shows all predictions, total payout ($1,204.00), and cost ($36.00)

**Combo Creation Bugs & Issues:**
- **State persistence issue:**
  - **User feedback:** "If I X out of combos and go back in my previous picks that I didn't place aren't preloaded"
  - If user closes combo creation screen (X button), previous picks are NOT saved
  - User must re-select all predictions if they return
  - **Frustrating:** Loses user's work and time
  - **Impact:** May cause users to abandon combo creation
- **High-speed market errors (CRITICAL ISSUE):**
  - **Multiple expired errors:** "Expired" error happens 2-3 times before price changed error
  - **Price changed errors:** "The price changed" error when odds change during placement
  - **Multiple retry attempts:** User must try 4-5 times if odds keep changing
  - **User feedback:** "I have to try placing 4-5 times if the odds constantly change"
  - **Expected but problematic:** Price movements are expected in live markets, but current error handling creates poor UX
  - **Impact:** Very frustrating, may cause users to avoid combos in volatile markets
  - **Timing:** Happens frequently in high-speed live sports markets (NFL, NBA games in progress)
- **Odds synchronization bugs:**
  - **Odds not updating correctly:** When adding prediction to combo, odds/payout may be incorrect
  - **Example:** Defense scoring touchdown - odds correct on page, payout glitched in combo
  - **User feedback:** "Caused me to always double check that when I add something to my prediction combo it doesn't add the correct payout if a single prediction is glitched"
  - **Impact:** User must always verify payout accuracy, creates distrust
  - **Payout reverts to $10:** When odds refresh, custom trade amount reverts to default $10
  - **User feedback:** "When I add something and odds refresh it reverts to $10"
- **Combo restrictions:**
  - **Unclear rules:** Not clear which props can/cannot be combined
  - **User feedback:** "There are some rules with Kalshi not allowed certain props to be together based on what they allowed/don't allow"
  - User may not know restrictions until they try to combine props
  - No clear indication of which props are restricted
- **Missing features:**
  - No draft saving
  - No undo functionality
  - No way to remove predictions from combo

### Typical Trading Session

1. **Discovery Phase**
   - How do you find markets to trade?
   - What categories do you focus on?
   - Do you use search, browse categories, or follow specific markets?
   - Do you check social feed/ideas for market insights?

2. **Market Analysis Phase**
   - What information do you look at before trading?
   - How do you evaluate market odds/prices?
   - Do you check social feed/ideas before trading?
   - Do you look at orderbook, volume, or other metrics?
   - How do you use information from other traders?

3. **Trade Execution Phase**
   - How do you place orders?
   - Do you use market orders or limit orders?
   - How do you decide on position size?
   - Do you trade multiple markets at once?
   - What happens when you don't have enough funds? (Deposit popup appears instantly)

4. **Position Management Phase**
   - How do you monitor open positions?
   - When do you decide to close positions?
   - Do you use stop losses or take profits?
   - How do you handle losing positions?

5. **Post-Trade Phase**
   - Do you review completed trades?
   - What do you learn from wins/losses?
   - Do you share trades on social feed?

---

## Market Selection Process

_How do you choose which markets to trade?_

### Criteria for Market Selection

- [ ] Market category preference
- [ ] Market liquidity/volume
- [ ] Market odds/prices
- [ ] Market closing time
- [ ] Personal knowledge/interest
- [ ] Social signals (ideas feed, leaderboard)
- [ ] Market type (Unique vs Repeating, Mentions, etc.)

### Examples

_Add specific examples of markets you've traded and why..._

---

## Trading Decisions & Strategy

### Position Sizing

- How do you decide how much to invest in a trade?
- Do you have a fixed amount per trade or percentage-based?
- How does account balance affect position sizing?

### Risk Management

- How do you manage risk?
- Do you set maximum loss limits?
- How do you handle drawdowns?
- Do you diversify across markets?

### Entry Timing

- When do you enter positions?
- Do you wait for specific price levels?
- Do you trade on news/events?
- How does market timing affect your decisions?

### Exit Strategy

- When do you exit winning positions?
- When do you exit losing positions?
- Do you use trailing stops or fixed targets?
- How do you handle market settlements?

---

## Platform Experience

### What Works Well

**Funding & Deposits:**
- **Easy bank account linking** - Simple, straightforward process
- **Apple Pay integration** - Regular deposits via Apple Pay work seamlessly
- **Instant fund access** - Funds available immediately after Apple Pay deposit (no waiting period)
- **Smart deposit prompt** - Deposit popup appears instantly when insufficient funds for selected trade
  - No friction or dead ends
  - User can deposit and continue trading without losing context
  - Seamless flow from trade attempt → deposit → trade completion

**UI/UX:**
- **Relatively easy to use** - Platform is intuitive
- **Information accessibility** - Can use personal knowledge and other traders' insights
- **Social integration** - Easy access to other traders' thoughts and analysis

### Pain Points & Friction

_Issues, confusion, or friction you encounter while trading..._

**Note:** User reports overall positive experience with easy UI and seamless funding flow. Specific pain points to be documented as they arise during trading.

### Missing Features

_Features you wish existed but don't..._

### Comparison to Other Platforms

_If you've used other prediction markets or trading platforms, how does Kalshi compare?_

---

## Specific Trading Scenarios

### Scenario 1: [Market Type/Event]

**Context:**
- Market: [Market name/type]
- Your analysis: [What you thought about the market]
- Your decision: [What you decided to do]
- Outcome: [What happened]
- Learnings: [What you learned]

### Scenario 2: [Another scenario]

_Add more scenarios as you trade..._

---

## Platform Navigation Patterns

### Most Used Features

- Which features do you use most frequently?
- Which pages do you visit most often?
- What's your typical navigation flow?

### Least Used Features

- Which features do you rarely or never use?
- Why don't you use them?
- Would you use them if they were improved?

---

## Social Features Usage

### Ideas Feed

- Do you post predictions/ideas?
- Do you read others' ideas before trading?
- Do you comment or engage with posts?
- How does social feed influence your trading?

### Leaderboard

- Do you check leaderboard?
- Does it influence your trading decisions?
- Do you try to compete/rank?

### Profile & Stats

- Do you share your profile/stats?
- Do you hide positions/trades?
- How do you use privacy settings?

---

## Technical Issues & Bugs Encountered

### While Trading

- Any bugs or issues you encountered while trading?
- Performance issues (lag, slow loading)?
- Confusing UI/UX moments?
- Data accuracy issues?

---

## Suggestions for Opinion Kings

### Based on Your Trading Experience

- What would make trading easier?
- What features would you want?
- What would improve your experience?
- What would make you trade more?

---

## Notes & Observations

### Funding Experience

**Apple Pay Deposits:**
- User regularly deposits via Apple Pay
- Funds are instantly available (no waiting period)
- This is a key advantage over other payment methods that may have delays
- **Note:** There's a bug where Apple Pay deposits show as "Debit card" in transaction history (see BUG_LOG.md B-004)

**Insufficient Funds Flow:**
- When attempting to trade without sufficient funds, deposit popup appears instantly
- This is excellent UX - no dead ends or error messages
- User can quickly deposit and continue with trade
- Maintains trading context and momentum

### UI/UX Observations

- Platform is relatively easy to use overall
- Information from other traders is accessible and useful
- Social features (ideas feed) provide valuable market insights
- Integration between trading and social features works well

### Key Workflow Pattern

1. User finds market to trade
2. User selects trade amount
3. If insufficient funds → Deposit popup appears instantly
4. User deposits via Apple Pay → Funds available immediately
5. User completes trade → Seamless flow

This pattern shows good UX design - the platform anticipates user needs and provides solutions without friction.

### Trading Types & Combo Restrictions

**One-Off Trading (Default):**
- **Everything is one-off trading** - Single market trades are the standard
- Most markets are individual, standalone trades
- Each market is traded independently

**Combo Trading (Sports Only):**
- **Combo bets are ONLY available for sports** - Specifically professional sports
- **Regulations and data:** Combos exist because of how regulations and data work for sports
- **Cross-sport combinations allowed:** Can combine multiple sports together (e.g., basketball and football)
- **Professional level only:** Combos are only for:
  - **NBA** (professional basketball)
  - **NFL** (professional football)
- **Not available for:** Other sports categories, non-sports markets, or amateur/college sports
- **Purpose:** Allows users to create multi-leg bets across NBA and NFL games

**Key Insight:**
- Combo functionality is a special feature for professional sports only
- This is likely due to:
  - Regulatory requirements for sports betting
  - Data availability for professional sports
  - Market structure differences between sports and other categories
- **For Opinion Kings:** Consider if combo functionality should be limited to specific categories or available more broadly
  - **Current Kalshi restriction:** Only NBA and NFL support combos
  - **Cross-sport capability:** Can combine basketball and football together
  - **Regulatory/data basis:** Combos exist because of how regulations and data work for professional sports
  - **Decision point:** Should Opinion Kings follow same restriction or expand combo availability?

---

## Cash Out Experience

### Cash Out Value vs Current Value

**Critical Distinction:**
- **Cash out value is NOT the same as current value**
- **Current value:** What your position is worth based on current odds (e.g., $5.13)
- **Cash out value:** What Kalshi or another market buyer will pay for your position (e.g., $4.32)
- **Difference:** Cash out is typically lower than current value (represents market maker spread/liquidity cost)
- **User must understand:** They're getting less than current value when cashing out

**Example from Experience:**
- Position: FedEx earnings call prediction
- Entry (Dec 18): Cost $5.29, 57% chance
- Current (Now): Value $5.13, 57% chance
- Cash out value: $4.32 (lower than current value of $5.13)
- Payout if correct: $9

### Cash Out Availability Patterns

**Single Trades:**
- **Easier to get cashouts** - More liquidity available
- Cash out more frequently available
- Better pricing (smaller spread between current value and cash out value)

**Combo Sports (2-3+ Predictions):**
- **Rare to get cashouts** especially when:
  - Already live (games in progress)
  - Odds change a lot (high volatility)
- **Pre-game cashouts more common:**
  - User places $25 5-prediction sports combo
  - Before anything starts, might get offered cashout at ~$20
  - Cash out available before games begin
  - Less likely once games are live and odds are volatile
- **Factors affecting availability:**
  - More predictions = less liquidity = less cash out availability
  - Live games = volatile odds = less cash out availability
  - Pre-game = stable odds = more cash out availability

### User Experience Issues

**Unpredictable Availability:**
- Not clear when cash out will be available
- Must check position popup to see if cash out is available
- No notifications when cash out becomes available
- Frustrating when cash out not available (especially for combos)

**Value Confusion:**
- Cash out value lower than current value - why?
- Not clearly explained why there's a difference
- User may not understand they're getting less than current value
- Info icon exists but unclear what it shows

**Combo Cash Out Challenges:**
- Very rare to get cashouts on 2-3+ predictions
- Especially difficult when games are live and odds change a lot
- Pre-game cashouts more realistic but still limited
- Example: $25 5-prediction combo might get $20 cashout offer before games start

### For Opinion Kings

**Improvements Needed:**
- **Improve cash out availability:** Especially for combos
- **Clear communication:** Explain cash out value vs current value
- **Cash out notifications:** Notify users when cash out becomes available
- **Better pricing:** Reduce spread for cash outs
- **Partial cash out:** Allow cashing out some predictions in combo
- **Cash out calculator:** Show what cash out value would be before placing trade
- **Cash out history:** Show past cash out offers and value over time
- **Cash out guarantees:** Guarantee cash out availability for certain conditions
- **Lock cash out value:** Lock cash out value for short period (e.g., 10 seconds) when user views it

**Key Insights:**
- Cash out is a valuable feature but needs better UX
- Single trades have better cash out experience than combos
- Pre-game cashouts more reliable than live cashouts
- Market maker spread creates value difference (expected but needs explanation)
- More predictions = less liquidity = harder to cash out

---

## Trading Log

### Trade #1

**Date:** [Date]  
**Market:** [Market name]  
**Position:** [Yes/No, amount]  
**Entry Price:** [Price]  
**Exit Price:** [Price or settlement]  
**Result:** [Win/Loss, amount]  
**Notes:** [Your thoughts, analysis, learnings]

### Trade #2

_Add more trades as you make them..._

---

## Key Insights & Takeaways

_Summary of main insights from your trading experience..._

---

