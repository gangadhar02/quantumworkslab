#!/bin/bash
find /Users/gangadhar/labelbox_clone/labelbox.com -name "*.html" -type f | while read -r file; do
    if ! grep -q "disable-navigation-dropdown.css" "$file"; then
        sed -i '' 's|</head>|<link rel="stylesheet" href="/disable-navigation-dropdown.css">\
</head>|' "$file"
        echo "Updated: $file"
    else
        echo "Already updated: $file"
    fi
done
echo "All HTML files have been updated with the navigation CSS."