# Screenshot Verification Checklist

> **CRITICAL:** This is our one source of truth for Kalshi. Every screenshot must accurately represent what the text describes.

## Verification Process

For each screenshot reference in KALSHI_FEATURE_BIBLE.md:

1. **Open the screenshot file**
2. **Read the feature description** in the Bible
3. **Verify the screenshot shows what the text describes**
4. **Check the screenshot ID matches** (e.g., 021 should show detailed market page)
5. **Verify the caption matches** the actual image content

## Issues to Check For

### 1. Wrong Screenshot Referenced
- Screenshot shows different feature than described
- Screenshot ID doesn't match the feature
- Screenshot is from wrong section

### 2. Screenshot Description Mismatch
- Caption doesn't match what's actually shown
- Description in text doesn't match image
- Index description doesn't match Bible description

### 3. Missing Screenshots
- Feature is described but no screenshot
- Screenshot exists but not referenced
- Screenshot referenced but doesn't exist

### 4. Duplicate/Incorrect Usage
- Same screenshot used for multiple features incorrectly
- Screenshot used in wrong context
- Screenshot shows different state than described

## Sections to Verify (Priority Order)

### High Priority (Core Features)
- [ ] **Onboarding** (011-018) - Sign up, login, email validation, password, duplicate account, Apple OAuth
- [ ] **Market Page** (021-031, 038-046) - Detailed market page, trading interface, calendar, multi-market graph
- [ ] **Trading** (047-055, 109-115) - Buy/sell interface, orderbook, combo creation, order completion, errors
- [ ] **Portfolio** (020, 096, 113) - Portfolio page, cash out, empty state
- [ ] **Discovery** (010, 019, 057-081) - Landing page, trending, categories, calendar

### Medium Priority (Important Features)
- [ ] **Account** (095, 099-108) - Deposit, hamburger menu, security, activity, transfers, documents, incentives, referrals
- [ ] **Social** (032-037, 082-094, 097) - Ideas feed, profiles, leaderboard, returns, posting
- [ ] **Support** (041, 090-092) - Help center, contact support, community guidelines

### Lower Priority (Supporting Features)
- [ ] **Notifications** (098) - Notifications page
- [ ] **Settings** (106) - Settings page
- [ ] **Misc** (056) - Footer

## Verification Template

For each screenshot:

```
### Screenshot ID: XXX
**File:** screenshots/XX-section/XXX-description.png
**Feature:** [Feature name]
**Bible Description:** [What Bible says it shows]
**Index Description:** [What index says it shows]
**Actual Content:** [What screenshot actually shows]
**Match?** [Yes/No]
**Issues:** [Any mismatches or problems]
**Action:** [What needs to be fixed]
```

## Known Issues to Fix

1. **Missing References (6 screenshots):**
   - [x] 025, 026, 027 - Added to Detailed Market Page
   - [x] 103 - Added Documents Page section
   - [x] 104 - Added Incentives Page section
   - [x] 107 - Added Referrals Page section

2. **Duplicate References:**
   - 093, 094 - Used in both Ideas Feed and Returns Page (verify if intentional)

3. **Caption Mismatches:**
   - 029 - Bible says "Calendar popup 2", Index says "Calendar popup (Open tab 2)" (minor, but verify)

## Next Steps

1. **Manual Verification:** Go through each screenshot and verify it matches the description
2. **Fix Mismatches:** Update descriptions or screenshot references as needed
3. **Add Missing:** Ensure all screenshots are properly referenced
4. **Final Check:** Run audit script again to verify all issues resolved

## Notes

- This is a living document - update as issues are found and fixed
- When in doubt, the screenshot should match what the feature section describes
- If screenshot doesn't match, either fix the reference or update the description

