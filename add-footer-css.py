#!/usr/bin/env python3
import os
import glob

def add_css_to_html_files():
    """Add CSS to disable JS footer in all HTML files"""
    css_link = '<link rel="stylesheet" href="/disable-js-footer.css">'
    
    # Find all HTML files
    html_files = glob.glob('**/*.html', recursive=True)
    
    updated_count = 0
    
    for file_path in html_files:
        # Skip the new-footer.html file itself
        if file_path == 'new-footer.html':
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if CSS link is already present
            if 'disable-js-footer.css' in content:
                print(f"⏭️  CSS already present in: {file_path}")
                continue
            
            # Find the closing </head> tag
            head_end = content.find('</head>')
            if head_end == -1:
                print(f"⚠️  No </head> tag found in: {file_path}")
                continue
            
            # Insert CSS link before </head>
            new_content = content[:head_end] + css_link + '\n' + content[head_end:]
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Added footer CSS to: {file_path}")
            updated_count += 1
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {str(e)}")
    
    print(f"\n🎉 CSS addition complete!")
    print(f"📊 Files updated: {updated_count}")

if __name__ == "__main__":
    add_css_to_html_files()