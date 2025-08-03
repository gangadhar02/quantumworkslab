#!/usr/bin/env python3
import os
import re
import glob

def get_new_footer():
    """Return the new footer HTML content"""
    return '''<footer class="footer">
        <div class="footer-container">
            <div class="footer-content">
                <!-- Product Section -->
                <div class="footer-section">
                    <h6>Product</h6>
                    <ul>
                        <li><a href="/product/platform/">Platform</a></li>
                        <li><a href="/product/model/foundry-models/">Model Foundry</a></li>
                        <li><a href="/product-demos/">Product Demos</a></li>
                        <li><a href="/recorded-demo/">Recorded Demo</a></li>
                    </ul>
                </div>

                <!-- Solutions Section -->
                <div class="footer-section">
                    <h6>Solutions</h6>
                    <ul>
                        <li><a href="/solutions/computer-vision/">Computer Vision</a></li>
                        <li><a href="/solutions/natural-language-processing/">Natural Language Processing</a></li>
                        <li><a href="/solutions/complex-reasoning/">Complex Reasoning</a></li>
                        <li><a href="/solutions/multimodal-reasoning/">Multimodal Reasoning</a></li>
                        <li><a href="/solutions/coding-tasks/">Coding</a></li>
                        <li><a href="/solutions/multilingual/">Multilingual</a></li>
                        <li><a href="/solutions/text-to-audio/">Audio</a></li>
                    </ul>
                </div>

                <!-- Learn Section (Resources) -->
                <div class="footer-section">
                    <h6>Learn</h6>
                    <ul>
                        <li><a href="/blog/">Blog</a></li>
                        <li><a href="/guides/">Guides</a></li>
                        <li><a href="https://docs.labelbox.com" target="_blank">Docs</a></li>
                        <li><a href="/faqs/">FAQs</a></li>
                        <li><a href="/research/">Research</a></li>
                        <li><a href="/product/model/foundry-models/">Models</a></li>
                        <li><a href="/datasets/">Public datasets</a></li>
                    </ul>
                </div>

                <!-- Company Section -->
                <div class="footer-section">
                    <h6>Company</h6>
                    <ul>
                        <li><a href="/company/about/">About</a></li>
                        <li><a href="/company/security/">Privacy & Security</a></li>
                        <li><a href="https://alignerr.com" target="_blank">Alignerr</a></li>
                    </ul>
                </div>

                <!-- Data Factory Section -->
                <div class="footer-section">
                    <h6>The data factory</h6>
                    <ul>
                        <li><a href="/why-labelbox/">Why Quantumworks Lab</a></li>
                        <li><a href="/services/labeling/">Labeling Services</a></li>
                        <li><a href="/services/alignerr-connect/">Alignerr Connect</a></li>
                        <li><a href="/model-foundry/">Model Foundry</a></li>
                        <li><a href="/leaderboards/">Leaderboards</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-logo">
                    <img src="static/images/favicon-v4-black.png" alt="Quantumworks Lab logo" loading="lazy" height="36" width="36">
                </div>
                <div class="footer-copyright">
                    © Quantumworks Lab, Inc<br>
                    We enable breakthroughs
                </div>
                <div class="footer-links">
                    <a href="https://docs.labelbox.com/page/terms-of-service" target="_blank">Terms of Service</a>
                    <div class="footer-divider"></div>
                    <a href="https://docs.labelbox.com/page/privacy-notice" target="_blank">Privacy Notice</a>
                    <div class="footer-divider"></div>
                    <a href="https://docs.labelbox.com/page/copyright-dispute-policy" target="_blank">Copyright Dispute Policy</a>
                </div>
            </div>
        </div>
    </footer>'''

def get_footer_css():
    """Return the CSS for the new footer"""
    return '''
        /* Footer styles */
        .footer {
            background-color: #ffffff;
            padding: 100px 0 40px 0;
            border-top: 1px solid #e5e7eb;
        }

        .footer-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 40px;
            margin-bottom: 60px;
        }

        .footer-section h6 {
            font-size: 20px;
            font-weight: 500;
            margin-bottom: 20px;
            color: #1f2937;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            margin-bottom: 12px;
        }

        .footer-section ul li a {
            color: #49535F;
            text-decoration: none;
            font-size: 16px;
            transition: color 0.3s ease;
        }

        .footer-section ul li a:hover {
            color: #2876D4;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 40px;
            border-top: 1px solid #e5e7eb;
        }

        .footer-logo {
            margin-bottom: 20px;
        }

        .footer-logo img {
            height: 36px;
            width: auto;
        }

        .footer-copyright {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 14px;
            color: #1f2937;
            margin-bottom: 20px;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: #49535F;
            text-decoration: none;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 14px;
            transition: color 0.3s ease;
        }

        .footer-links a:hover {
            color: #2876D4;
        }

        .footer-divider {
            width: 1px;
            height: 16px;
            background-color: #e5e7eb;
            margin: 0 8px;
        }

        /* Responsive design */
        @media (max-width: 1024px) {
            .footer-content {
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
            }
        }

        @media (max-width: 768px) {
            .footer-content {
                grid-template-columns: repeat(2, 1fr);
                gap: 24px;
            }
            
            .footer {
                padding: 60px 0 30px 0;
            }
        }

        @media (max-width: 480px) {
            .footer-content {
                grid-template-columns: 1fr;
                text-align: center;
            }
            
            .footer-links {
                flex-direction: column;
                align-items: center;
                gap: 12px;
            }
            
            .footer-divider {
                display: none;
            }
        }
    '''

def replace_footer_in_file(file_path):
    """Replace the old footer with the new one in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the old footer
        old_footer_pattern = r'<footer class="Footer__StyledFooter-sc-u68pnv-0 eJChXt">.*?</footer>'
        
        # Check if file contains the old footer
        if re.search(old_footer_pattern, content, re.DOTALL):
            # Replace the old footer with the new one
            new_content = re.sub(old_footer_pattern, get_new_footer(), content, flags=re.DOTALL)
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated footer in: {file_path}")
            return True
        else:
            print(f"⏭️  No old footer found in: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False

def add_css_to_head(file_path):
    """Add footer CSS to the head section if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if footer CSS is already present
        if '.footer {' in content:
            print(f"⏭️  Footer CSS already present in: {file_path}")
            return False
        
        # Find the closing </head> tag
        head_end = content.find('</head>')
        if head_end == -1:
            print(f"⚠️  No </head> tag found in: {file_path}")
            return False
        
        # Insert CSS before </head>
        css_to_add = f'<style>{get_footer_css()}</style>'
        new_content = content[:head_end] + css_to_add + content[head_end:]
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added footer CSS to: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding CSS to {file_path}: {str(e)}")
        return False

def main():
    """Main function to replace footers across all HTML files"""
    print("🚀 Starting footer replacement across all HTML files...")
    
    # Find all HTML files
    html_files = glob.glob('**/*.html', recursive=True)
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    print(f"📁 Found {len(html_files)} HTML files")
    
    updated_count = 0
    css_added_count = 0
    
    for file_path in html_files:
        # Skip the new-footer.html file itself
        if file_path == 'new-footer.html':
            continue
            
        # Replace footer
        if replace_footer_in_file(file_path):
            updated_count += 1
            
        # Add CSS
        if add_css_to_head(file_path):
            css_added_count += 1
    
    print(f"\n🎉 Footer replacement complete!")
    print(f"📊 Summary:")
    print(f"   • Files with footer updated: {updated_count}")
    print(f"   • Files with CSS added: {css_added_count}")
    print(f"   • Total files processed: {len(html_files)}")

if __name__ == "__main__":
    main() 