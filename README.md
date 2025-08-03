# Labelbox Static Site

This is a static export of the Labelbox website built with Next.js.

## Deployment Instructions

### Local Development
```bash
# Install dependencies (optional, only for serve)
npm install

# Serve locally on port 3000
npm run serve
```

### Production Deployment

#### Option 1: Static File Server
```bash
# Serve on port 80 (requires sudo on some systems)
npm run serve:production
```

#### Option 2: Nginx
1. Copy all files to your web server directory (e.g., `/var/www/html`)
2. Configure Nginx to serve the static files
3. Example Nginx configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

#### Option 3: Apache
1. Copy all files to your web server directory (e.g., `/var/www/html`)
2. Create an `.htaccess` file with proper rewrite rules for client-side routing

#### Option 4: Cloud Platforms
- **Vercel**: Simply connect your repository and deploy
- **Netlify**: Drag and drop the folder or connect repository
- **AWS S3 + CloudFront**: Upload to S3 bucket and configure CloudFront
- **GitHub Pages**: Push to `gh-pages` branch

## Directory Structure
- `/` - Main index.html and root assets
- `/_next/` - Next.js build output with JavaScript and CSS assets
- `/why-labelbox/` - Additional pages
- Other directories contain individual pages as static HTML

## Notes
- This is a pre-built static site, no build step required
- All routing is handled client-side
- Ensure your web server is configured to serve `index.html` for all routes