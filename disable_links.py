#!/usr/bin/env python3
import os
import re
from pathlib import Path

def disable_link(match):
    """Convert a link to plain text, keeping the text content"""
    # Extract the text content between <a> tags
    full_match = match.group(0)
    text_match = re.search(r'>([^<]+)<', full_match)
    if text_match:
        text = text_match.group(1)
        return f'<span style="color: inherit; cursor: default;">{text}</span>'
    return full_match

def disable_specific_links(content):
    """Disable specific links in the content"""
    
    # 1. Disable "Start for free" links (with app.labelbox.com)
    content = re.sub(
        r'<a[^>]*href="https://app\.labelbox\.com/signup"[^>]*>Start for free</a>',
        '<span style="color: inherit; cursor: default;">Start for free</span>',
        content
    )
    
    # 2. Disable "Docs" link in footer
    content = re.sub(
        r'<a[^>]*href="https://docs\.labelbox\.com"[^>]*>Docs</a>',
        '<span style="color: inherit; cursor: default;">Docs</span>',
        content
    )
    
    # 3. Disable Terms of Service link
    content = re.sub(
        r'<a[^>]*href="https://docs\.labelbox\.com/page/terms-of-service"[^>]*>Terms of Service</a>',
        '<span style="color: inherit; cursor: default;">Terms of Service</span>',
        content
    )
    
    # 4. Disable Privacy Notice link
    content = re.sub(
        r'<a[^>]*href="https://docs\.labelbox\.com/page/privacy-notice"[^>]*>Privacy Notice</a>',
        '<span style="color: inherit; cursor: default;">Privacy Notice</span>',
        content
    )
    
    # 5. Disable Copyright Dispute Policy link
    content = re.sub(
        r'<a[^>]*href="https://docs\.labelbox\.com/page/copyright-dispute-policy"[^>]*>Copyright Dispute Policy</a>',
        '<span style="color: inherit; cursor: default;">Copyright Dispute Policy</span>',
        content
    )
    
    return content

def process_file(filepath):
    """Process a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = disable_specific_links(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {filepath}")
            return True
        else:
            print(f"No changes needed: {filepath}")
            return False
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    # Update footer template first
    footer_template = Path("footer-template.html")
    if footer_template.exists():
        process_file(footer_template)
    
    # Find all HTML files
    html_files = list(Path(".").rglob("*.html"))
    
    # Exclude certain patterns
    exclude_patterns = [
        'node_modules/',
        '.git/',
        '_next/'
    ]
    
    # Filter and process files
    updated_count = 0
    for filepath in html_files:
        file_str = str(filepath)
        if not any(pattern in file_str for pattern in exclude_patterns):
            if process_file(filepath):
                updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()