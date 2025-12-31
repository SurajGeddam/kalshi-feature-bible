#!/usr/bin/env python3
"""
Tool to help identify and fix screenshot mismatches.
This script extracts what each screenshot SHOULD show based on descriptions.
"""

import re
import os

def extract_screenshot_details():
    """Extract all screenshot details from the Bible."""
    with open("KALSHI_FEATURE_BIBLE.md", 'r', encoding='utf-8') as f:
        bible = f.read()
    
    screenshots = {}
    
    # Extract features and their screenshots
    feature_pattern = r'^### ([^\n]+)\n\n(.*?)(?=^### |\Z)'
    
    for match in re.finditer(feature_pattern, bible, re.MULTILINE | re.DOTALL):
        feature_name = match.group(1).strip()
        content = match.group(2)
        
        # Get screenshots list
        screenshots_section = re.search(r'\*\*Screenshots:\*\*\s*\n(.*?)(?=\*\*User goal|\*\*Kalshi flow|\*\*Observed|\Z)', content, re.DOTALL)
        if screenshots_section:
            screenshot_pattern = r'- (\d{3}): `([^`]+)` - (.+)'
            for scr_match in re.finditer(screenshot_pattern, screenshots_section.group(1)):
                screenshot_id, path, description = scr_match.groups()
                screenshot_id = screenshot_id.strip()
                
                # Get user goal and flow for context
                user_goal_match = re.search(r'\*\*User goal:\*\*\s*\n(.*?)(?=\*\*Kalshi flow|\*\*Observed|\Z)', content, re.DOTALL)
                user_goal = user_goal_match.group(1).strip() if user_goal_match else ""
                
                kalshi_flow_match = re.search(r'\*\*Kalshi flow.*?\*\*\s*\n(.*?)(?=\*\*Observed|\*\*What I like|\Z)', content, re.DOTALL)
                kalshi_flow = kalshi_flow_match.group(1)[:500].strip() if kalshi_flow_match else ""
                
                screenshots[screenshot_id] = {
                    'id': screenshot_id,
                    'path': path.strip(),
                    'description': description.strip(),
                    'feature': feature_name,
                    'user_goal': user_goal[:200] if user_goal else "",
                    'flow': kalshi_flow[:300] if kalshi_flow else ""
                }
    
    return screenshots

def generate_verification_report():
    """Generate a detailed verification report."""
    screenshots = extract_screenshot_details()
    
    print("="*80)
    print("SCREENSHOT VERIFICATION REPORT")
    print("="*80)
    print(f"\nTotal screenshots: {len(screenshots)}\n")
    
    # Known issues
    known_issues = ['012', '014', '102']
    
    print("KNOWN ISSUES (❌):")
    print("-" * 80)
    for sid in known_issues:
        if sid in screenshots:
            s = screenshots[sid]
            print(f"\n❌ Screenshot {sid}: {s['feature']}")
            print(f"   File: {s['path']}")
            print(f"   Should show: {s['description']}")
            print(f"   User goal: {s['user_goal'][:100]}...")
            print(f"   Flow: {s['flow'][:100]}...")
    
    # Generate checklist for all screenshots
    print("\n\n" + "="*80)
    print("COMPLETE VERIFICATION CHECKLIST")
    print("="*80)
    print("\nFor each screenshot:")
    print("1. Open the image file")
    print("2. Read the description below")
    print("3. Verify the image matches")
    print("4. Mark as ✅ or ❌\n")
    
    # Sort by ID
    sorted_ids = sorted(screenshots.keys(), key=lambda x: int(x))
    
    for sid in sorted_ids:
        s = screenshots[sid]
        status = "❌ KNOWN ISSUE" if sid in known_issues else "❓ TO VERIFY"
        
        print(f"\n{'='*80}")
        print(f"Screenshot {sid}: {s['feature']}")
        print(f"Status: {status}")
        print(f"File: screenshots/{s['path']}")
        print(f"\nShould show: {s['description']}")
        if s['user_goal']:
            print(f"\nUser goal context: {s['user_goal'][:150]}...")
        if s['flow']:
            print(f"\nFlow context: {s['flow'][:150]}...")
        print(f"\n[ ] Verified")

if __name__ == "__main__":
    generate_verification_report()

