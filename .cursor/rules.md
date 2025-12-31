# Project: Kalshi Teardown → Competitor Feature Bible (Opinion Kings)

## Objective

We are building a comprehensive, screenshot-driven competitor teardown of Kalshi.  

This document is NOT a generic summary. It is an end-to-end, feature-by-feature record of:

- What Kalshi has today (UX + product behavior)
- Exactly how each flow works (steps)
- What we like / dislike (user lens)
- How we think it's implemented or why it's designed that way (builder lens)
- Bugs, confusing moments, edge cases
- Implications and recommendations for Opinion Kings

This becomes our internal "Kalshi Feature Bible" to compare against our future builds.

---

## Canonical output

Primary doc: `KALSHI_FEATURE_BIBLE.md`  

Supporting docs:

- `SCREENSHOT_INDEX.md` (single source of truth mapping IDs → filenames → section)
- `BUG_LOG.md` (bugs, glitches, UX failures, reproducible steps)
- `DELTA_TABLE.md` (Kalshi vs Opinion Kings feature comparison + status)
- `RAW_NOTES.md` (quick dumps before polishing)

Screenshots stored in `/screenshots/` organized by sections.

---

## Required quality bar

Every section must be:

1) Screenshot-backed (at least 1 image per feature/flow)

2) Step-by-step reproducible (like a QA doc)

3) Includes at least one of:
   - Like/dislike
   - Confusion/friction
   - Behavioral nudges
   - Edge case / bug

4) Ends with Opinion Kings implications:
   - Copy / Avoid / Improve / Differentiate
   - Engineering notes (data models, events, possible APIs)
   - Metrics to track (activation, retention, conversion, liquidity, trust)

Do NOT write fluffy marketing language. Write like a PM + engineer doing a serious teardown.

---

## Documentation format (use this template for EVERY feature)

For each feature/flow, write in this exact structure:

### [Feature Name]

**Feature category:** (Onboarding / Discovery / Market Page / Trading / Portfolio / Social / Settlement / Support / Compliance / Notifications / Payments / Etc.)

**Screenshots:**  
- (ID + filename + short caption)

**User goal:**  
- What the user is trying to accomplish

**Kalshi flow (steps):**
1.
2.
3.

**Observed behavior:**
- What actually happens
- Microcopy / UI cues
- Defaults / guardrails

**What I like:**
- Bullet list

**What I don't like / confusion:**
- Bullet list

**Edge cases / bugs:**
- Bullet list + link to BUG_LOG entry (if applicable)

**Builder hypothesis (why they did it):**
- Bullet list (compliance, retention, liquidity, safety, growth)

**Opinion Kings implications:**
- Copy:
- Avoid:
- Beat:
- Implementation notes:
- Metrics:

---

## Screenshot discipline

All screenshots must be indexed.

Naming format: `###-section-shortslug.png`

Examples:
- `010-onboarding-signup.png`
- `042-order-ticket-fee-breakdown.png`
- `061-portfolio-open-positions.png`

Every screenshot must be added to `SCREENSHOT_INDEX.md` with:
- ID
- Section
- File path
- Short caption
- Notes (what to look at)

In the main doc, embed images like:

`![042 Fee breakdown](screenshots/04-order-ticket/042-order-ticket-fee-breakdown.png)`

---

## Bug logging discipline

All bugs go into `BUG_LOG.md` with:

- Bug ID: `B-###`
- Severity: P0/P1/P2/P3
- Area (onboarding/trading/etc.)
- Steps to reproduce
- Expected vs actual
- Screenshot references
- Hypothesis (why it happened)
- Risk (user trust / money risk / compliance risk)
- Opinion Kings prevention or advantage

If a behavior might be "intentional but feels like a bug," still log it as "UX Bug / Dark Pattern suspicion."

---

## Delta tracking discipline (Kalshi vs Opinion Kings)

Maintain `DELTA_TABLE.md` with columns:

- Feature
- Kalshi (Yes/No + notes)
- Opinion Kings plan (Copy / Modify / Differentiate / Skip)
- Priority (P0/P1/P2)
- Complexity (S/M/L)
- Notes

This is a living roadmap input.

---

## Scope: what to document (ALL of these if present)

1) Onboarding + KYC + trust/legal disclosures
2) Funding (ACH/debit), withdrawals, limits, fees shown
3) Discovery (home feed, categories, trending, search)
4) Market page (rules, sources, timelines, charting, orderbook)
5) Trading (market/limit, confirmation screens, errors, cancellations, partial fills)
6) Portfolio (positions, P&L, realized/unrealized, history)
7) Notifications (price movement, market resolution, reminders)
8) Social layer (leaderboards, sharing, referrals, incentives)
9) Support (help center, contact, dispute, "request settlement")
10) Integrity/safety cues (warnings, restrictions, risk disclosures)
11) Settings (privacy, security, notifications, account)
12) Any growth loops (promos, bonuses, referral programs)
13) Anything surprising (dark patterns, friction, hidden constraints)

Document even small UI details; those often reveal strategy.

---

## Writing style

- Clear, structured, tactical.
- Prefer bullets over paragraphs.
- Always tie observations to "why" and to "what we do."
- Be honest: if uncertain, label as hypothesis.
- Never invent features we didn't observe in screenshots.

---

## Cursor behavior (how to help)

When I provide:
- a screenshot
- or raw notes

You will:

1) Ask: "What section does this belong to?" ONLY if it is truly unclear.

2) Otherwise: place it into the right folder + index it.

3) Generate the full feature writeup using the template.

4) Update the Delta Table and Bug Log if relevant.

5) Keep docs consistent and non-duplicative.

We iterate by adding screenshots and polishing feature writeups.

