#!/bin/bash

# Add the disable-navigation-dropdown.css to all HTML files
find /Users/gangadhar/labelbox_clone/labelbox.com -name "*.html" -type f | while read -r file; do
    # Check if the file already has a link to disable-navigation-dropdown.css
    if ! grep -q "disable-navigation-dropdown.css" "$file"; then
        # Add the CSS link before the closing </head> tag
        sed -i '' 's|</head>|<link rel="stylesheet" href="/disable-navigation-dropdown.css">\n</head>|' "$file"
        echo "Updated: $file"
    else
        echo "Already updated: $file"
    fi
done

echo "All HTML files have been updated with the navigation CSS."