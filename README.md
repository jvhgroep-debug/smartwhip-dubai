# Smartwhip Dubai

Multilingual static website for Smartwhip and Cream Deluxe in Dubai.

- 45 pages in English, Dutch and French
- Product-specific WhatsApp orders and cash on delivery
- Eight Dubai delivery-area pages and a blog

## Hosting

Deploy the `dist` directory as static files. For Cloudflare Pages use production branch `main`, no build command, and output directory `dist`.

## Editing

GitHub is the source of truth for this exported website. Preserve existing URLs and language routes. Do not remove or overwrite source changes when regenerating pages.

The Python generators are included for reference. `python build_all.py` regenerates the website using Python 3 standard-library modules. Generated HTML is committed for build-free deployment.

Current public site: https://smartwhip-dubai.jvhgroep.chatgpt.site
