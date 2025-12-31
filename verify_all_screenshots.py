#!/usr/bin/env python3
"""Comprehensive screenshot verification - checks every reference against context and index."""

import re
from collections import defaultdict

def extract_screenshot_info():
    """Extract all screenshot info from index."""
    with open("SCREENSHOT_INDEX.md", 'r', encoding='utf-8') as f:
        index = f.read()
    
    # Pattern: | ID | Section | Path | Caption | Notes |
    pattern = r'\|\s*(\d{3})\s*\|\s*([^|]+)\s*\|\s*`(screenshots/[^`]+)`\s*\|\s*([^|]+)\s*\|'
    
    screenshots = {}
    for match in re.finditer(pattern, index):
        id_num, section, path, caption = [g.strip() for g in match.groups()]
        screenshots[path] = {
            'id': id_num,
            'section': section,
            'caption': caption,
            'path': path
        }
    
    return screenshots

def extract_bible_references():
    """Extract all screenshot references from Bible with context."""
    with open("KALSHI_FEATURE_BIBLE.md", 'r', encoding='utf-8') as f:
        bible = f.read()
    
    # Find all screenshot references with line numbers
    pattern = r'!\[([^\]]+)\]\((screenshots/[^)]+)\)'
    references = []
    
    for match in re.finditer(pattern, bible):
        caption = match.group(1).strip()
        path = match.group(2).strip()
        start = match.start()
        
        # Get line number
        line_num = bible[:start].count('\n') + 1
        
        # Get context (500 chars before, 500 after)
        context_start = max(0, start - 500)
        context_end = min(len(bible), match.end() + 500)
        context = bible[context_start:context_end]
        
        # Extract feature name (look for ### headers before this)
        feature_match = re.search(r'###\s+([^\n]+)', bible[max(0, start-2000):start])
        feature = feature_match.group(1).strip() if feature_match else "Unknown"
        
        references.append({
            'line': line_num,
            'caption': caption,
            'path': path,
            'feature': feature,
            'context': context
        })
    
    return references

def verify_references():
    """Verify all references are correct."""
    screenshots = extract_screenshot_info()
    references = extract_bible_references()
    
    print("="*80)
    print("COMPREHENSIVE SCREENSHOT VERIFICATION")
    print("="*80)
    print(f"\nTotal screenshots in index: {len(screenshots)}")
    print(f"Total references in Bible: {len(references)}\n")
    
    issues = []
    verified = []
    
    for ref in references:
        path = ref['path']
        
        if path not in screenshots:
            issues.append({
                'type': 'NOT_IN_INDEX',
                'ref': ref,
                'message': f"Path {path} not found in SCREENSHOT_INDEX.md"
            })
            continue
        
        index_info = screenshots[path]
        
        # Check if ID matches (extract ID from path)
        path_id = path.split('/')[-1].split('-')[0]
        if path_id != index_info['id']:
            issues.append({
                'type': 'ID_MISMATCH',
                'ref': ref,
                'index': index_info,
                'message': f"ID mismatch: path suggests {path_id}, index says {index_info['id']}"
            })
        
        # Check if section makes sense
        # (This is harder to verify automatically, but we can flag obvious issues)
        
        # Check caption similarity
        caption_similarity = check_caption_similarity(ref['caption'], index_info['caption'])
        if caption_similarity < 0.3:  # Very different
            issues.append({
                'type': 'CAPTION_MISMATCH',
                'ref': ref,
                'index': index_info,
                'similarity': caption_similarity,
                'message': f"Caption mismatch: Bible='{ref['caption']}' vs Index='{index_info['caption']}'"
            })
        else:
            verified.append({
                'ref': ref,
                'index': index_info,
                'similarity': caption_similarity
            })
    
    print(f"\n✅ VERIFIED: {len(verified)} references")
    print(f"❌ ISSUES: {len(issues)} references\n")
    
    # Group issues by type
    by_type = defaultdict(list)
    for issue in issues:
        by_type[issue['type']].append(issue)
    
    for issue_type, issue_list in sorted(by_type.items()):
        print(f"\n{'='*80}")
        print(f"{issue_type}: {len(issue_list)} issues")
        print('='*80)
        
        for issue in issue_list[:20]:  # Show first 20
            ref = issue['ref']
            print(f"\nLine {ref['line']}: {ref['feature']}")
            print(f"  Path: {ref['path']}")
            print(f"  Bible caption: {ref['caption']}")
            if 'index' in issue:
                print(f"  Index caption: {issue['index']['caption']}")
            print(f"  Message: {issue['message']}")
            print(f"  Context snippet: {ref['context'][:200]}...")
        
        if len(issue_list) > 20:
            print(f"\n  ... and {len(issue_list) - 20} more issues")
    
    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print('='*80)
    print(f"Total references: {len(references)}")
    print(f"Verified: {len(verified)}")
    print(f"Issues: {len(issues)}")
    print(f"  - Not in index: {len(by_type.get('NOT_IN_INDEX', []))}")
    print(f"  - ID mismatch: {len(by_type.get('ID_MISMATCH', []))}")
    print(f"  - Caption mismatch: {len(by_type.get('CAPTION_MISMATCH', []))}")
    
    return issues, verified

def check_caption_similarity(caption1, caption2):
    """Simple similarity check between two captions."""
    words1 = set(caption1.lower().split())
    words2 = set(caption2.lower().split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1 & words2
    union = words1 | words2
    
    return len(intersection) / len(union) if union else 0.0

if __name__ == "__main__":
    issues, verified = verify_references()
    
    # Write detailed report
    with open("VERIFICATION_REPORT.md", 'w') as f:
        f.write("# Screenshot Verification Report\n\n")
        f.write(f"**Total Issues Found:** {len(issues)}\n\n")
        f.write("## Issues by Type\n\n")
        
        by_type = defaultdict(list)
        for issue in issues:
            by_type[issue['type']].append(issue)
        
        for issue_type, issue_list in sorted(by_type.items()):
            f.write(f"### {issue_type}: {len(issue_list)} issues\n\n")
            for issue in issue_list:
                ref = issue['ref']
                f.write(f"- **Line {ref['line']}** - {ref['feature']}\n")
                f.write(f"  - Path: `{ref['path']}`\n")
                f.write(f"  - Bible caption: `{ref['caption']}`\n")
                if 'index' in issue:
                    f.write(f"  - Index caption: `{issue['index']['caption']}`\n")
                f.write(f"  - {issue['message']}\n\n")
    
    print(f"\n\nDetailed report written to VERIFICATION_REPORT.md")

if __name__ == "__main__":
    verify_references()

