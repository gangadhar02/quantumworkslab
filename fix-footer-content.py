#!/usr/bin/env python3
import os
import glob
import re

def get_complete_footer():
    """Return the complete footer HTML content"""
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

def fix_footer_content():
    """Fix empty footer content in all HTML files"""
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
            
            # Check if file has empty footer class="footer"
            if '<footer class="footer">' in content:
                # Replace empty footer with complete footer
                new_content = content.replace('<footer class="footer">', get_complete_footer(), 1)
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Fixed footer content in: {file_path}")
                updated_count += 1
            else:
                print(f"⏭️  No empty footer found in: {file_path}")
                
        except Exception as e:
            print(f"❌ Error processing {file_path}: {str(e)}")
    
    print(f"\n🎉 Footer content fix complete!")
    print(f"📊 Files updated: {updated_count}")

if __name__ == "__main__":
    fix_footer_content()