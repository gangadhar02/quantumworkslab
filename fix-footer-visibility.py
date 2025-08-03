#!/usr/bin/env python3
import os
import re
import glob

def fix_footer_visibility():
    """Add CSS file to all HTML files and fix duplicate footers"""
    
    # Get all HTML files
    html_files = glob.glob("**/*.html", recursive=True)
    
    css_link = '<link rel="stylesheet" href="fix-footer-visibility.css">'
    
    files_updated = 0
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if CSS link already exists
            if 'fix-footer-visibility.css' not in content:
                # Add CSS link before closing head tag
                content = re.sub(
                    r'(</head>)',
                    f'{css_link}\n</head>',
                    content
                )
            
            # Fix duplicate footers - keep only the first one
            footer_pattern = r'(<footer class="footer">.*?</footer>)'
            footer_matches = re.findall(footer_pattern, content, re.DOTALL)
            
            if len(footer_matches) > 1:
                # Keep only the first footer, remove the rest
                first_footer = footer_matches[0]
                content = re.sub(footer_pattern, '', content, flags=re.DOTALL)
                # Add back only the first footer
                content = re.sub(
                    r'(<div class="grid grid-cols-12 gap-4 md:gap-6"></div>)',
                    r'\1\n' + first_footer,
                    content
                )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            files_updated += 1
            print(f"Updated: {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\n✅ Footer visibility fixed in {files_updated} files!")
    print("The footer should now be visible with proper styling.")

if __name__ == "__main__":
    fix_footer_visibility() 