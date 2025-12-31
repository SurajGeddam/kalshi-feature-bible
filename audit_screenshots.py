#!/usr/bin/env python3
"""Audit screenshot references and verify they match actual files."""

import os
import re
from pathlib import Path
from collections import defaultdict

def find_screenshot_refs(content, pattern):
    """Find all screenshot references in content."""
    return re.findall(pattern, content)

def get_all_screenshots():
    """Get all actual screenshot files."""
    screenshots = []
    for root, dirs, files in os.walk("screenshots"):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                rel_path = os.path.join(root, file).replace('\\', '/')
                screenshots.append(rel_path)
    return sorted(screenshots)

def main():
    print("🔍 AUDITING SCREENSHOT REFERENCES...\n")
    
    # Read files
    with open("KALSHI_FEATURE_BIBLE.md", 'r', encoding='utf-8') as f:
        bible_content = f.read()
    
    with open("SCREENSHOT_INDEX.md", 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Find references
    bible_pattern = r'!\[.*?\]\((screenshots/[^)]+)\)'
    bible_refs = find_screenshot_refs(bible_content, bible_pattern)
    
    index_pattern = r'`(screenshots/[^`]+)`'
    index_refs = find_screenshot_refs(index_content, index_pattern)
    
    # Get actual files
    screenshot_files = get_all_screenshots()
    
    print(f"📊 STATISTICS:")
    print(f"   - Bible references: {len(set(bible_refs))}")
    print(f"   - Index references: {len(set(index_refs))}")
    print(f"   - Actual files: {len(screenshot_files)}")
    print()
    
    # Check missing files
    bible_refs_set = set(bible_refs)
    index_refs_set = set(index_refs)
    screenshot_files_set = set(screenshot_files)
    
    missing_from_bible = bible_refs_set - screenshot_files_set
    missing_from_index = index_refs_set - screenshot_files_set
    unreferenced = screenshot_files_set - bible_refs_set
    
    if missing_from_bible:
        print(f"❌ {len(missing_from_bible)} files referenced in BIBLE but don't exist:")
        for ref in sorted(missing_from_bible):
            print(f"   - {ref}")
    else:
        print("✅ All Bible references exist!")
    
    if missing_from_index:
        print(f"\n❌ {len(missing_from_index)} files referenced in INDEX but don't exist:")
        for ref in sorted(missing_from_index)[:10]:
            print(f"   - {ref}")
    else:
        print("\n✅ All Index references exist!")
    
    if unreferenced:
        print(f"\n⚠️  {len(unreferenced)} files exist but NOT referenced in BIBLE:")
        for ref in sorted(unreferenced)[:10]:
            print(f"   - {ref}")
        if len(unreferenced) > 10:
            print(f"   ... and {len(unreferenced) - 10} more")
    else:
        print("\n✅ All files are referenced in Bible!")
    
    # Check for duplicates
    bible_dupes = [ref for ref in bible_refs if bible_refs.count(ref) > 1]
    if bible_dupes:
        print(f"\n⚠️  {len(set(bible_dupes))} duplicate references in BIBLE:")
        for ref in sorted(set(bible_dupes))[:5]:
            count = bible_refs.count(ref)
            print(f"   - {ref} (appears {count} times)")
    
    print("\n" + "="*60)
    print("SUMMARY:")
    print(f"  ✅ All good: {len(missing_from_bible) == 0 and len(missing_from_index) == 0}")
    print(f"  ⚠️  Issues found: {len(missing_from_bible) + len(missing_from_index) + len(unreferenced)}")

if __name__ == "__main__":
    main()

