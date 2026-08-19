#!/usr/bin/env python3
"""
Jekyll to Quarto Migration Script for ghif.github.io
Converts all posts in _posts/ into Quarto posts in posts/<date>-<slug>/index.qmd
"""

import os
import re
import shutil
import yaml

def clean_categories(raw):
    if not raw:
        return []
    if isinstance(raw, list):
        items = raw
    elif "," in str(raw):
        items = [x.strip() for x in str(raw).split(",")]
    else:
        items = [str(raw).strip()]
    
    synonyms = {
        "ai": "AI",
        "artificial-intelligence": "AI",
        "graphic": "Graphics",
        "probabilty and statistics": "Probability & Statistics",
        "unsupervised learning": "Unsupervised Learning",
        "machine learning": "Machine Learning",
        "machine-learning": "Machine Learning",
        "math": "Mathematics",
        "computer vision": "Computer Vision",
        "optimization": "Optimization",
        "media": "General"
    }
    cleaned = []
    for item in items:
        item_str = item.strip().strip("'\"")
        if not item_str:
            continue
        norm = synonyms.get(item_str.lower(), item_str.title())
        if norm and norm not in cleaned:
            cleaned.append(norm)
    return cleaned

def clean_body_content(body):
    # Strip leading whitespace and any leading '---' separator
    body = body.lstrip()
    while body.startswith("---"):
        body = body[3:].lstrip()

    # Replace standalone '---' horizontal rules with '* * *' to avoid YAML confusion
    body = re.sub(r'(?m)^---\s*$', '* * *', body)

    # 1. Replace Liquid {% highlight <lang> %} ... {% endhighlight %}
    body = re.sub(r'\{%\s*highlight\s+([a-zA-Z0-9_]+)\s*%\}([\s\S]*?)\{%\s*endhighlight\s*%\}',
                  r'```\1\2```', body)
    
    # 2. Replace Liquid {% include embed.html url="..." %}
    def embed_replace(match):
        url = match.group(1)
        return f'<div class="ratio ratio-16x9 my-4"><iframe src="{url}" allowfullscreen></iframe></div>'
    body = re.sub(r'\{%\s*include\s+embed\.html\s+url=[\"\x27]([^\x27\"]+)[\"\x27]\s*%\}', embed_replace, body)
    
    # 3. Clean escaped liquid tags
    body = body.replace('{{ "{% highlight language " }}%}', '```language')
    body = body.replace('{{ "{% endhighlight " }}%}', '```')
    
    # 4. Clean raw LaTeX sections in body (e.g. \section{...})
    body = re.sub(r'\\section\{([^}]+)\}', r'## \1', body)
    body = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', body)
    body = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', body)
    
    # 5. Clean LaTeX enumerate environment
    body = re.sub(r'\\begin\{enumerate\}', '', body)
    body = re.sub(r'\\end\{enumerate\}', '', body)
    body = re.sub(r'\\item\s+', r'1. ', body)
    
    # 6. Clean LaTeX algorithm environments in lbfgs
    def clean_algorithm_blocks(text):
        def alg_sub(m):
            block = m.group(1)
            # Extract caption
            cap_match = re.search(r'\\caption\{([^}]+)\}', block)
            caption = cap_match.group(1) if cap_match else "Algoritma"
            # Remove labels and caption
            lines = []
            for line in block.split('\n'):
                line = line.strip()
                if line.startswith(r'\caption') or line.startswith(r'\label') or line == r'\Begin{' or line == '}':
                    continue
                if not line:
                    continue
                # Clean line formatting
                line = line.rstrip(r'\;')
                if line.startswith(r'\For{'):
                    cond = line[5:-1] if line.endswith('}') else line[5:]
                    lines.append(f"   **For** {cond}:")
                elif line.startswith(r'{') or line.startswith(r'}'):
                    continue
                else:
                    lines.append(f"   - {line}")
            body_text = "\n".join(lines)
            return f"\n::: {{.callout-note appearance=\"minimal\" icon=false}}\n**Algoritma: {caption}**\n\n{body_text}\n:::\n"

        return re.sub(r'\\begin\{algorithm\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{algorithm\}', alg_sub, text)

    body = clean_algorithm_blocks(body)

    # 7. Clean kramdown IAL / ALD tags (e.g. {: style="..."})
    body = re.sub(r'\{:\s*[^}]+\}', '', body)

    # 8. Normalize image links
    body = re.sub(r'https?://ghif\.github\.io/assets/', '/assets/', body)
    
    # 9. Normalize external images that exist locally
    body = body.replace('http://sebastianruder.com/content/images/2015/12/without_momentum.gif', '/assets/without_momentum.gif')
    body = body.replace('http://sebastianruder.com/content/images/2015/12/with_momentum.gif', '/assets/with_momentum.gif')
    
    return body

def migrate():
    os.makedirs("posts", exist_ok=True)
    
    # 1. Cleanup legacy theme assets if they exist
    legacy_asset_dirs = ["assets/css", "assets/fonts", "assets/katex", "assets/fontawesome"]
    for ldir in legacy_asset_dirs:
        if os.path.exists(ldir):
            shutil.rmtree(ldir)
            print(f"✓ Removed legacy theme folder: {ldir}")
    if os.path.exists("assets/main.css"):
        os.remove("assets/main.css")
        print("✓ Removed legacy assets/main.css")

    # 2. Process all posts in _posts
    posts = sorted([f for f in os.listdir("_posts") if f.endswith((".md", ".markdown"))])
    print(f"Found {len(posts)} posts to migrate...")

    for fname in posts:
        fpath = os.path.join("_posts", fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        fm = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                cleaned_yaml = "\n".join(line.rstrip() for line in parts[1].split("\n"))
                fm = yaml.safe_load(cleaned_yaml) or {}
                body = parts[2]

        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.*)\.(?:md|markdown)$", fname)
        if m:
            date_prefix, slug = m.groups()
        else:
            date_prefix = "2020-01-01"
            slug = os.path.splitext(fname)[0]

        title = fm.get("title", slug.replace("-", " ").title())
        date_raw = str(fm.get("date", date_prefix))[:10]
        categories = clean_categories(fm.get("categories"))
        is_published = fm.get("published", True)
        if is_published is None:
            is_published = True

        post_dir = os.path.join("posts", f"{date_prefix}-{slug}")
        os.makedirs(post_dir, exist_ok=True)

        new_fm = {
            "title": title,
            "date": date_raw,
            "categories": categories,
            "aliases": [f"/{slug}/"]
        }
        if not is_published:
            new_fm["draft"] = True

        cleaned_body = clean_body_content(body)

        out_path = os.path.join(post_dir, "index.qmd")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(new_fm, f, sort_keys=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(cleaned_body.lstrip("\n"))

        print(f"  ✓ Migrated: {fname} -> {out_path}")

    print(f"Migration complete! {len(posts)} posts migrated to posts/")

if __name__ == "__main__":
    migrate()
