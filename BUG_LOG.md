# Bug Log

> **Purpose:** Track all bugs, glitches, UX failures, and "intentional but feels like a bug" behaviors observed in Kalshi.

**Severity Levels:**
- **P0:** Critical (money risk, compliance risk, data loss)
- **P1:** High (user trust, major UX failure, broken flow)
- **P2:** Medium (confusing, friction, minor UX issue)
- **P3:** Low (cosmetic, edge case, minor annoyance)

---

## Bugs

| Bug ID | Severity | Area | Title | Status |
|--------|----------|------|-------|--------|
| B-001 | P2 | Market Page | Rules dropdown selection doesn't update chart and main list selection state | Open |
| B-002 | P2 | Order Ticket | Orderbook graph view bottom navigation cutoff and buggy display | Open |
| B-003 | P2 | Notifications | Notification icon not red when unread notifications exist | Open |
| B-004 | P2 | Account | Deposit method incorrectly labeled as "Debit card" when using Apple Pay | Open |
| B-005 | P2 | Trading | Combo picks not saved when closing creation screen | Open |
| B-006 | P1 | Trading | Combo payout glitch / incorrect odds refresh | Open |
| B-007 | P2 | Trading | Combo creation - odds refresh reverts to $10 | Open |
| B-008 | P1 | Trading | Multiple expired/price changed errors in high-speed live markets | Open |
| B-009 | P1 | Trading | Market closes too quickly when odds reach extremes, preventing cash out | Open |

---

## Bug Template

### B-###: [Bug Title]

**Severity:** P0/P1/P2/P3

**Area:** (onboarding/trading/portfolio/etc.)

**Date Found:** YYYY-MM-DD

**Steps to Reproduce:**
1.
2.
3.

**Expected Behavior:**
- What should happen

**Actual Behavior:**
- What actually happens

**Screenshots:**
- Reference screenshot IDs or file paths

**Hypothesis (why it happened):**
- Technical guess
- Design oversight
- Intentional but poorly executed

**Risk Assessment:**
- User trust impact
- Money risk
- Compliance risk
- Retention impact

**Opinion Kings Prevention/Advantage:**
- How we avoid this
- How we can do better
- Competitive advantage

---

## UX Bugs / Dark Pattern Suspicions

### B-001: Rules dropdown selection doesn't update chart and main list selection state

**Severity:** P2

**Area:** Market Page / Trading Interface

**Date Found:** 2024-12-19

**Steps to Reproduce:**
1. Navigate to a market page with multiple predictions (e.g., "What will the announcers say during the Carolina at Tampa Bay professional football game?")
2. Click a Yes/No button on a prediction in the main list (e.g., "What a Catch" Yes)
3. Observe: Trading interface, rules, chart, and main list selection all update correctly
4. Click the rules dropdown (green hyperlink/button in rules section)
5. Select a different prediction from the dropdown (e.g., "Wind / Windy")
6. Observe: Trading interface and rules update, but chart and main list selection do NOT update

**Expected Behavior:**
- When selecting a prediction from rules dropdown, ALL components should update:
  - Trading interface updates (shows selected prediction and prices) ✓
  - Rules section updates (shows selected prediction's rules) ✓
  - Chart updates (shows lines for selected prediction) ✗
  - Main list selection state updates (highlights selected prediction's button) ✗

**Actual Behavior:**
- Trading interface updates correctly
- Rules section updates correctly
- Chart does NOT update (still shows previous prediction's lines)
- Main list selection state does NOT update (previous prediction's button still highlighted)
- Creates inconsistent UI state where different parts of the page show different selections

**Screenshots:**
- 027: `027-market-page-rules-dropdown-selection.png` - Shows inconsistent state after selecting from rules dropdown

**Hypothesis (why it happened):**
- **State management issue:** Rules dropdown uses different state update path than Yes/No buttons
- **Incomplete implementation:** Rules dropdown was added later and doesn't trigger all the same state updates
- **Missing event handlers:** Rules dropdown selection doesn't call the same functions that update chart and list selection
- **Component isolation:** Chart and main list components may not be listening to rules dropdown state changes
- **Different code paths:** Yes/No buttons likely have comprehensive update logic, but rules dropdown only updates trading/rules

**Risk Assessment:**
- **User trust impact:** Medium - Confusing, makes platform seem buggy or inconsistent
- **Money risk:** Low - User can still trade, but might trade on wrong prediction if confused about which is selected
- **Compliance risk:** None
- **Retention impact:** Medium - Frustrating UX, could cause users to abandon or lose trust

**Opinion Kings Prevention/Advantage:**
- **How we avoid this:**
  - Use single source of truth for selected prediction (React Context, Redux, or shared state)
  - Ensure all selection methods (Yes/No buttons, rules dropdown, keyboard shortcuts) use same state update function
  - Create unified `selectPrediction(predictionId)` function that updates ALL components
  - Test all selection methods to ensure consistent behavior
  - Use React state management that ensures all components stay in sync
- **How we can do better:**
  - Single `selectPrediction()` function that updates: trading interface, rules, chart, main list selection
  - All selection methods (buttons, dropdown, keyboard) call same function
  - Add visual indicator showing which prediction is currently selected (highlight chart line, highlight list item)
  - Add state validation to ensure all components show same selected prediction
  - Consider removing rules dropdown as selection method, or make it update everything
- **Competitive advantage:**
  - Consistent, predictable UI behavior
  - Better user trust through bug-free experience
  - Clearer indication of selected prediction across all UI elements

### B-002: Orderbook graph view bottom navigation cutoff and buggy display

**Severity:** P2

**Area:** Order Ticket / Orderbook Popup

**Date Found:** 2024-12-31

**Steps to Reproduce:**
1. Navigate to a mentions market page
2. Click on a prediction word (e.g., "No Good") - NOT the Yes/No buttons
3. Orderbook popup appears
4. Click on "Graph" tab
5. Observe: Graph shows 3 lines with + icon
6. Can add other words/predictions to graph by clicking on them
7. Scroll down or look at bottom of popup
8. Observe: Bottom navigation/category tabs are cutoff and very buggy
9. No icons to fill out - looks odd/incomplete

**Expected Behavior:**
- Bottom navigation/category tabs (e.g., "Superbowl", "Pro", "What", "Roughing", "Next") should display fully
- Icons should be visible and properly rendered
- Interface should look complete and polished
- All navigation elements should be accessible

**Actual Behavior:**
- Bottom navigation tabs are cutoff
- Display is very buggy
- No icons visible (looks incomplete)
- Interface looks odd and unprofessional
- Functionality works (can add predictions to graph by clicking words) but UI is broken

**Screenshots:**
- 055: `055-order-ticket-orderbook-graph-multi-prediction-bug.png` - Shows graph with 3 lines, + icon, and cutoff bottom navigation

**Hypothesis (why it happened):**
- **Layout/overflow issue:** Popup height or overflow settings causing bottom content to be cut off
- **CSS/styling bug:** Bottom navigation not properly positioned or styled within popup
- **Icon loading issue:** Icons not loading or not properly rendered
- **Responsive design issue:** Popup not handling content overflow correctly
- **Incomplete implementation:** Bottom navigation feature may have been added but not fully implemented
- **Z-index or positioning issue:** Bottom navigation may be behind other elements or positioned incorrectly

**Risk Assessment:**
- **User trust impact:** Medium - Broken UI makes platform seem unprofessional or buggy
- **Money risk:** Low - Core functionality (adding predictions to graph) works, but poor UX
- **Compliance risk:** None
- **Retention impact:** Medium - Users may lose trust or find platform unreliable due to visual bugs

**Opinion Kings Prevention/Advantage:**
- **How we avoid this:**
  - Proper popup/modal height management (max-height, overflow handling)
  - Test popup with various content lengths
  - Ensure all UI elements are visible and properly styled
  - Icon loading and fallback handling
  - Proper CSS for bottom navigation positioning
  - Responsive design testing for popups
- **How we can do better:**
  - Proper overflow handling (scrollable content area if needed)
  - Clear visual boundaries for popup content
  - Ensure all icons load and display correctly
  - Test with maximum content (many predictions, long lists)
  - Add loading states for icons
  - Better popup sizing and positioning
  - Clear visual hierarchy and spacing
- **Competitive advantage:**
  - Polished, bug-free UI builds trust
  - Professional appearance increases user confidence
  - Better UX leads to higher retention

---

## B-003: Notification Icon Not Red When Unread Notifications Exist

**Severity:** P2 (Medium) - UX Issue  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
Notification bell icon in top navigation bar does not change color or show visual indicator when unread notifications exist. User feedback: "Notification icon is not red while showing this and says not red after"

**Steps to Reproduce:**
1. User has unread notifications
2. User clicks notification bell icon
3. Notifications page displays with list of notifications
4. Notification icon remains unchanged (not red, no badge, no visual indicator)
5. After viewing notifications, icon still does not indicate read/unread status

**Expected Behavior:**
- Notification icon should show red badge/count when unread notifications exist
- Icon should change color or show visual indicator
- Badge should disappear when all notifications are read
- Icon should update in real-time when new notifications arrive

**Actual Behavior:**
- Notification icon does not change color
- No badge or count indicator
- No visual feedback that unread notifications exist
- Icon does not update after viewing notifications

**User Impact:**
- Users cannot tell if there are new notifications without opening notifications page
- Reduces engagement (users may miss important updates)
- Poor UX (standard pattern is to show unread indicator)

**Hypothesis:**
- Missing implementation of unread notification tracking
- No visual state management for notification icon
- May be intentional design choice (but poor UX)

**Risk Assessment:**
- **User Experience:** High - Users miss notifications, reduced engagement
- **Business Impact:** Medium - May reduce user retention and engagement
- **Technical Complexity:** Low - Need to track read/unread status and update icon

**Recommendation:**
- Implement unread notification tracking
- Add red badge/count on notification icon when unread notifications exist
- Update icon in real-time when notifications arrive
- Clear badge when all notifications are read
- Consider adding notification count (e.g., "3" badge)

**Related Feature:** Notifications Page (KALSHI_FEATURE_BIBLE.md)

---

## B-004: Deposit Method Incorrectly Labeled as "Debit card" When Using Apple Pay

**Severity:** P2 (Medium) - Data Accuracy Issue  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
Transaction history on Transfers page incorrectly shows "Deposit from Debit card" when user makes deposits via Apple Pay. User feedback: "You need to link bank but I have been making deposits via Apple Pay and it says via debit"

**Steps to Reproduce:**
1. User makes deposit using Apple Pay
2. Deposit completes successfully
3. User navigates to Transfers page
4. Transaction history shows "Deposit from Debit card"
5. Should show "Deposit from Apple Pay" or similar

**Expected Behavior:**
- Transaction history should accurately reflect payment method used
- Apple Pay deposits should show "Deposit from Apple Pay"
- Debit card deposits should show "Deposit from Debit card"
- All payment methods should be correctly labeled

**Actual Behavior:**
- All deposits show "Deposit from Debit card" regardless of actual payment method
- Apple Pay deposits incorrectly labeled as "Debit card"
- Inaccurate transaction history

**User Impact:**
- Confusing for users (can't tell which payment method was used)
- Inaccurate transaction records
- May cause confusion when linking bank accounts (user thinks they need to link bank, but already using Apple Pay)

**Hypothesis:**
- Payment method detection not properly implemented
- Apple Pay transactions processed through debit card processor, but method not tracked separately
- Transaction record stores generic "Debit card" instead of actual payment method

**Risk Assessment:**
- **User Experience:** Medium - Confusing but not blocking
- **Business Impact:** Low - Doesn't affect functionality, but reduces trust
- **Technical Complexity:** Low - Need to track payment method correctly

**Recommendation:**
- Track payment method correctly in transaction records
- Store actual payment method (Apple Pay, Debit card, Google Pay, etc.)
- Display accurate payment method in transaction history
- Update existing transactions if possible (or at least fix going forward)

**Related Feature:** Transfers Page (KALSHI_FEATURE_BIBLE.md)

---

## B-005: Combo Picks Not Saved When Closing Creation Screen

**Severity:** P2 (Medium) - UX Issue / Data Loss  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
When creating a combo bet, if user closes the combo creation screen (clicks X button) before placing the trade, their previous picks/selections are not saved or preloaded when they return to combo creation. User feedback: "If I X out of combos and go back in my previous picks that I didn't place aren't preloaded"

**Steps to Reproduce:**
1. User navigates to Sports category and selects "Combo" sub-navigation
2. User starts creating combo bet
3. User selects multiple predictions (Yes/No for each)
4. User clicks X button to close combo creation screen
5. User returns to combo creation
6. Previous picks/selections are NOT preloaded
7. User must start over and re-select all predictions

**Expected Behavior:**
- Combo picks should be saved when user closes creation screen
- When user returns to combo creation, previous picks should be preloaded
- User should be able to continue where they left off
- State should persist until trade is placed or explicitly cleared

**Actual Behavior:**
- Combo picks are NOT saved when closing creation screen
- Previous picks are NOT preloaded when returning
- User loses all their work and must start over
- No way to recover previous selections

**User Impact:**
- **High frustration:** User loses time and effort spent selecting predictions
- **Work loss:** User must re-select all predictions if they accidentally close or need to check something
- **Abandonment risk:** Users may abandon combo creation if they lose work
- **Poor UX:** Standard expectation is that work is saved

**Hypothesis:**
- State management not implemented for combo creation
- Selections stored only in component state (not persisted)
- State cleared when component unmounts (X button closes screen)
- May be intentional to prevent confusion, but creates frustration

**Risk Assessment:**
- **User Experience:** High - Significant frustration and work loss
- **Business Impact:** Medium - May reduce combo creation and trading
- **Technical Complexity:** Low - Need to persist state (local storage or session)

**Recommendation:**
- Implement state persistence for combo creation
- Save selections to local storage or session storage
- Restore selections when user returns to combo creation
- Clear state only after successful trade or explicit user action
- Consider adding "Save as draft" functionality
- Consider adding "Resume combo" option

**Related Feature:** Combo Creation Flow (KALSHI_FEATURE_BIBLE.md)

---

## B-006: Odds Not Updating Correctly When Adding Prediction to Combo

**Severity:** P1 (High) - Data Accuracy / Financial Impact  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
When adding a prediction to a combo, the odds/payout displayed in the combo may be incorrect (glitched) even though the odds are correct on the individual market page. User feedback: "When I click on 2 combos the odds didn't change correctly... caused me to always double check that when I add something to my prediction combo it doesn't add the correct payout if a single prediction is glitched"

**Steps to Reproduce:**
1. User views a prediction on market page (e.g., "Defense scoring a touchdown")
2. Odds are correct on the market page
3. User adds prediction to combo
4. Odds/payout shown in combo are incorrect (glitched)
5. User must double-check payout to ensure accuracy

**Expected Behavior:**
- Odds in combo should match odds on individual market page
- Payout calculation should be accurate
- User should be able to trust that combo odds are correct

**Actual Behavior:**
- Odds/payout in combo may be incorrect even when market page shows correct odds
- Example: Defense scoring touchdown - odds correct on page, payout glitched in combo
- User must manually verify payout is correct
- Creates distrust in platform accuracy

**User Impact:**
- **High - Financial risk:** Incorrect odds could lead to unexpected losses
- **User distrust:** User must always double-check payout accuracy
- **Time waste:** User must verify each prediction's payout
- **User feedback:** "Caused me to always double check that when I add something to my prediction combo it doesn't add the correct payout if a single prediction is glitched"

**Hypothesis:**
- Odds synchronization issue between market page and combo builder
- Race condition when fetching odds for multiple predictions
- Caching issue - combo may show stale odds
- Real-time update not propagating to combo correctly

**Risk Assessment:**
- **User Experience:** High - Creates distrust and requires constant verification
- **Business Impact:** High - Financial accuracy is critical, could lead to disputes
- **Technical Complexity:** Medium - Need to ensure odds synchronization

**Recommendation:**
- Fix odds synchronization between market page and combo builder
- Ensure real-time odds updates propagate to combo
- Add validation to verify odds match before allowing trade
- Show warning if odds have changed significantly
- Add "Refresh odds" button to update combo odds
- Log odds discrepancies for monitoring

**Related Feature:** Combo Creation Flow (KALSHI_FEATURE_BIBLE.md)

---

## B-007: Payout Reverts to $10 When Odds Refresh

**Severity:** P2 (Medium) - UX Issue  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
When user sets a custom trade amount in combo creation, if odds refresh/update, the trade amount reverts to the default $10. User feedback: "When I add something and odds refresh it reverts to $10"

**Steps to Reproduce:**
1. User creates combo and sets custom trade amount (e.g., $20, $50, $100)
2. User adds prediction to combo
3. Odds refresh/update (automatic or manual)
4. Trade amount reverts to default $10
5. User must re-enter custom trade amount

**Expected Behavior:**
- Trade amount should persist when odds refresh
- User's custom amount should be maintained
- Only odds/payout should update, not trade amount

**Actual Behavior:**
- Trade amount resets to default $10 when odds refresh
- User must re-enter custom trade amount
- Frustrating if user had set a specific amount

**User Impact:**
- **Medium:** User must re-enter trade amount
- **Frustrating:** Loses user's input
- **Time waste:** Must re-enter amount multiple times if odds refresh frequently

**Hypothesis:**
- State management issue - trade amount not persisted when odds update
- Component re-render resets trade amount to default
- Trade amount state not included in odds refresh logic

**Risk Assessment:**
- **User Experience:** Medium - Frustrating but not blocking
- **Business Impact:** Low - Doesn't affect functionality, just UX
- **Technical Complexity:** Low - Need to persist trade amount in state

**Recommendation:**
- Persist trade amount when odds refresh
- Separate trade amount state from odds state
- Only update odds/payout, not trade amount
- Add "Remember amount" option if user wants

**Related Feature:** Combo Creation Flow (KALSHI_FEATURE_BIBLE.md)

---

## B-008: Multiple Expired/Price Changed Errors in High-Speed Live Markets

**Severity:** P1 (High) - UX Issue / Trading Friction  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
In volatile live sports markets, users encounter multiple errors when trying to place combo trades. "Expired" error appears multiple times (2-3 times), followed by "The price changed" error. User must retry 4-5 times before order goes through. User feedback: "I have to try placing 4-5 times if the odds constantly change"

**Steps to Reproduce:**
1. User creates combo in high-speed live sports market (e.g., NFL game in progress)
2. User attempts to place combo trade
3. "Expired" error modal appears with "Take me back" button
4. User clicks "Take me back" and retries
5. "Expired" error appears again (2-3 times total)
6. "The price changed" error appears: "Your order didn't go through as the odds of your combo changed."
7. User must retry multiple times (4-5 attempts) before order succeeds
8. Odds may have changed significantly by the time order goes through

**Expected Behavior:**
- Order should be placed quickly without multiple errors
- If odds change, should handle gracefully (auto-update or clear error)
- Should not require 4-5 retry attempts
- Should provide better error handling for volatile markets

**Actual Behavior:**
- "Expired" error appears multiple times (2-3 times)
- Then "The price changed" error appears
- User must retry 4-5 times before order succeeds
- Each retry requires clicking "Take me back" button
- Odds may change significantly during retry attempts
- User may miss desired odds by the time order goes through

**User Impact:**
- **High frustration:** Must retry multiple times
- **Time waste:** Each retry takes time, odds may change
- **Missed opportunities:** May miss desired odds by the time order succeeds
- **User feedback:** "I have to try placing 4-5 times if the odds constantly change"
- **Expected but problematic:** Price movements are expected in live markets, but current error handling creates poor UX

**Hypothesis:**
- Order timeout too short for combo processing
- Multiple validation checks causing delays
- Odds changing faster than order can be processed
- No auto-retry mechanism
- No odds locking mechanism for combos
- Race condition between odds update and order submission

**Risk Assessment:**
- **User Experience:** High - Significant frustration and time waste
- **Business Impact:** High - May reduce trading in volatile markets, users may abandon combos
- **Technical Complexity:** Medium - Need better error handling and possibly odds locking

**Recommendation:**
- **Auto-retry mechanism:** Automatically retry order if expired (with user confirmation)
- **Odds locking:** Lock odds for short period (e.g., 5-10 seconds) when user starts combo creation
- **Better error handling:** Combine multiple errors into single message
- **Faster processing:** Optimize combo order processing to reduce timeout
- **Odds tolerance:** Allow small odds changes without rejecting order
- **Progress indicator:** Show order processing status instead of just errors
- **Smart retry:** Automatically retry with updated odds if price changed slightly

**Related Feature:** Combo Creation Flow (KALSHI_FEATURE_BIBLE.md)

---

## B-009: Market Closes Too Quickly When Odds Reach Extremes, Preventing Cash Out

**Severity:** P1 (High) - Financial Impact / User Trust  
**Status:** Open  
**Reported:** 2024-12-31

**Description:**
In live markets (especially mentions markets and sports), when odds move quickly to extremes (e.g., 99% vs 1%), the market gets closed before users can cash out their positions. Users cannot cash out for the 1 cent or 99 cent value depending on which side of the prediction they're on. This is particularly problematic in live events where odds can change rapidly.

**Steps to Reproduce:**
1. User has an open position in a live market (mentions or sports)
2. Live event occurs (e.g., sports play, news event)
3. Odds move quickly to extreme values (e.g., 99% vs 1%)
4. User attempts to cash out position
5. Market closes before cash out can be executed
6. User cannot cash out for the 1 cent or 99 cent value (depending on position side)
7. Position is locked until market settlement

**Expected Behavior:**
- User should be able to cash out position even when odds reach extremes
- Market should remain open for reasonable time after odds reach extremes
- User should be able to cash out for the extreme value (1 cent or 99 cent)
- Cash out should be available until market actually closes/settles
- User should have opportunity to exit position before market closes

**Actual Behavior:**
- Market closes very quickly when odds reach extremes (99% vs 1%)
- User cannot cash out position before market closes
- Position is locked until market settlement
- User cannot access the 1 cent or 99 cent value (depending on position side)
- Market closure happens too fast for user to react
- Particularly problematic in live markets (mentions, sports)

**User Impact:**
- **Financial impact:** User cannot cash out position at extreme value
- **Lost opportunity:** User misses chance to exit at favorable price
- **Frustration:** Market closes before user can react
- **Trust issue:** User may feel platform is closing markets too quickly
- **User feedback:** "I can't cashout our for the 1 cent or the 99 cent depending on what side of prediction im on because the market gets closed"
- **Correlation with live markets:** Issue is very correlated with live stuff (mentions markets, sports)

**Market Types Affected:**
- **Mentions markets:** User has tested and observed issue
- **Sports markets:** User has tested and observed issue
- **Other markets:** User hasn't tested many markets, just mentions and sports
- **Live events:** Issue is particularly problematic during live events

**Hypothesis:**
- Market closure logic triggers too quickly when odds reach extremes
- No grace period for users to cash out before market closes
- Automatic market closure when odds reach certain threshold (e.g., 99% or 1%)
- No consideration for users with open positions
- Market closure may be triggered by event outcome rather than odds threshold
- In live markets, events happen quickly and markets close immediately

**Risk Assessment:**
- **User Experience:** High - Users cannot exit positions when they want
- **Financial Impact:** High - Users lose opportunity to cash out at favorable prices
- **Business Impact:** High - May reduce user trust, users may avoid live markets
- **Technical Complexity:** Medium - Need to adjust market closure logic and cash out availability

**Recommendation:**
- **Grace period:** Add grace period (e.g., 30-60 seconds) after odds reach extremes before closing market
- **Cash out priority:** Ensure cash out remains available even when odds reach extremes
- **Market closure delay:** Delay market closure to allow users to cash out
- **User notification:** Notify users when odds reach extremes and market may close soon
- **Cash out guarantee:** Guarantee cash out availability for X seconds after odds reach extremes
- **Manual closure option:** Allow manual market closure with warning instead of automatic closure
- **Position protection:** Ensure users with open positions can always cash out before market closes
- **Extreme odds handling:** Different closure logic for extreme odds vs normal market closure
- **Live market considerations:** Special handling for live markets where events happen quickly

**Related Feature:** 
- Portfolio Position Cash Out Feature (KALSHI_FEATURE_BIBLE.md)
- Market Closure Logic (not yet documented)
- Live Markets Handling (not yet documented)

**User Testing Notes:**
- User has primarily tested mentions markets and sports markets
- Issue is very correlated with live events
- User has not tested many other market types
- Issue may be specific to live markets or may affect all markets

---

## Notes

- **Only log bugs when explicitly identified by the user**
- Do not assume something is a bug - many UI elements are intentional business logic
- Include reproducible steps for all bugs
- Link bugs to relevant feature sections in main bible

