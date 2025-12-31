#!/usr/bin/env python3
"""Verify screenshot references match their context in the Bible."""

import re
from collections import defaultdict

def extract_feature_sections():
    """Extract each feature section with its screenshots."""
    with open("KALSHI_FEATURE_BIBLE.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by feature headers (### Feature Name)
    features = []
    pattern = r'^### ([^\n]+)\n\n(.*?)(?=^### |\Z)'
    
    for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
        feature_name = match.group(1).strip()
        feature_content = match.group(2)
        
        # Extract screenshots list
        screenshots_section = re.search(r'\*\*Screenshots:\*\*\s*\n(.*?)(?=\*\*User goal|\*\*Kalshi flow|\Z)', feature_content, re.DOTALL)
        screenshots_list = []
        if screenshots_section:
            # Extract screenshot IDs and descriptions
            screenshot_pattern = r'- (\d{3}): `([^`]+)` - (.+)'
            for scr_match in re.finditer(screenshot_pattern, screenshots_section.group(1)):
                screenshot_id, path, description = scr_match.groups()
                screenshots_list.append({
                    'id': screenshot_id,
                    'path': path.strip(),
                    'description': description.strip()
                })
        
        # Extract embedded screenshot references
        embedded_pattern = r'!\[([^\]]+)\]\((screenshots/[^)]+)\)'
        embedded_refs = []
        for emb_match in re.finditer(embedded_pattern, feature_content):
            caption = emb_match.group(1).strip()
            path = emb_match.group(2).strip()
            embedded_refs.append({
                'caption': caption,
                'path': path
            })
        
        # Extract key content
        user_goal = re.search(r'\*\*User goal:\*\*\s*\n(.*?)(?=\*\*Kalshi flow|\*\*Observed|\Z)', feature_content, re.DOTALL)
        kalshi_flow = re.search(r'\*\*Kalshi flow.*?\*\*\s*\n(.*?)(?=\*\*Observed|\*\*What I like|\Z)', feature_content, re.DOTALL)
        
        features.append({
            'name': feature_name,
            'screenshots_list': screenshots_list,
            'embedded_refs': embedded_refs,
            'user_goal': user_goal.group(1).strip() if user_goal else "",
            'kalshi_flow': kalshi_flow.group(1)[:500] if kalshi_flow else "",  # First 500 chars
            'content': feature_content[:1000]  # First 1000 chars for context
        })
    
    return features

def verify_screenshots():
    """Verify screenshots match their feature context."""
    features = extract_feature_sections()
    
    print("="*80)
    print("SCREENSHOT CONTEXT VERIFICATION")
    print("="*80)
    print(f"\nFound {len(features)} feature sections\n")
    
    issues = []
    
    for feature in features:
        feature_name = feature['name']
        screenshots_list = feature['screenshots_list']
        embedded_refs = feature['embedded_refs']
        
        # Check if screenshots list matches embedded refs
        list_paths = {s['path'] for s in screenshots_list}
        embedded_paths = {e['path'] for e in embedded_refs}
        
        if list_paths != embedded_paths:
            missing_in_embedded = list_paths - embedded_paths
            extra_in_embedded = embedded_paths - list_paths
            
            if missing_in_embedded:
                issues.append({
                    'type': 'MISSING_EMBEDDED',
                    'feature': feature_name,
                    'screenshots': screenshots_list,
                    'missing': missing_in_embedded,
                    'message': f"Screenshots listed but not embedded: {missing_in_embedded}"
                })
            
            if extra_in_embedded:
                issues.append({
                    'type': 'EXTRA_EMBEDDED',
                    'feature': feature_name,
                    'extra': extra_in_embedded,
                    'message': f"Screenshots embedded but not in list: {extra_in_embedded}"
                })
        
        # Check screenshot IDs match paths
        for screenshot in screenshots_list:
            path_id = screenshot['path'].split('/')[-1].split('-')[0]
            if path_id != screenshot['id']:
                issues.append({
                    'type': 'ID_PATH_MISMATCH',
                    'feature': feature_name,
                    'screenshot': screenshot,
                    'path_id': path_id,
                    'message': f"Screenshot ID {screenshot['id']} doesn't match path ID {path_id}"
                })
        
        # Check if feature content mentions the screenshot IDs
        content_lower = feature['content'].lower()
        for screenshot in screenshots_list:
            # Check if screenshot ID or description keywords appear in content
            id_mentioned = screenshot['id'] in feature['content']
            desc_keywords = screenshot['description'].lower().split()[:3]  # First 3 words
            keywords_mentioned = any(keyword in content_lower for keyword in desc_keywords if len(keyword) > 3)
            
            if not id_mentioned and not keywords_mentioned:
                issues.append({
                    'type': 'SCREENSHOT_NOT_MENTIONED',
                    'feature': feature_name,
                    'screenshot': screenshot,
                    'message': f"Screenshot {screenshot['id']} may not be relevant to feature content"
                })
    
    # Group by type
    by_type = defaultdict(list)
    for issue in issues:
        by_type[issue['type']].append(issue)
    
    print(f"Found {len(issues)} potential issues\n")
    
    for issue_type, issue_list in sorted(by_type.items()):
        print(f"\n{'='*80}")
        print(f"{issue_type}: {len(issue_list)} issues")
        print('='*80)
        
        for issue in issue_list[:10]:  # Show first 10
            print(f"\nFeature: {issue['feature']}")
            print(f"  {issue['message']}")
            if 'screenshot' in issue:
                print(f"  Screenshot: {issue['screenshot']}")
        
        if len(issue_list) > 10:
            print(f"\n  ... and {len(issue_list) - 10} more")
    
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print('='*80)
    print(f"Total features: {len(features)}")
    print(f"Total issues: {len(issues)}")
    for issue_type, issue_list in sorted(by_type.items()):
        print(f"  {issue_type}: {len(issue_list)}")

if __name__ == "__main__":
    verify_screenshots()

