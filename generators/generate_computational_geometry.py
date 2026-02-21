import os

pages = [
    {
        "embed": "https://observablehq.com/embed/@syaleni/kd-tree",
        "title": "KD Tree",
        "description": "Interactive visualization of KD Tree spatial partitioning and nearest neighbor search.",
        "filename": "kd-tree.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/convex-hull",
        "title": "Convex Hull",
        "description": "Interactive convex hull computation and visualization using computational geometry algorithms.",
        "filename": "convex-hull.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/35699e83a962b637",
        "title": "Evolution",
        "description": "Computational geometry simulation exploring evolutionary algorithms.",
        "filename": "evolution.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/96edd8bdd7f507a6",
        "title": "Interpolators",
        "description": "Interactive exploration of interpolation methods and smooth curve generation.",
        "filename": "interpolators.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/parametric-curve-viewer",
        "title": "Parametric Curve Viewer",
        "description": "Interactive viewer for parametric curves and geometric forms.",
        "filename": "parametric-curves.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/radial-pattern",
        "title": "Radial Pattern",
        "description": "Interactive radial pattern generator using parametric geometry and trigonometric functions.",
        "filename": "radial-patterns.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/65633b1f98ff39d9",
        "title": "Random Generatives",
        "description": "Generative art and randomized computational geometry visualizations.",
        "filename": "random-generatives.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/some-circles",
        "title": "Some Circles",
        "description": "Generative circle patterns using parametric geometry and iterative algorithms.",
        "filename": "some-circles.qmd"
    },
]

page_template = """---
pagetitle: "{title}"
description: "{description}"
format:
  html:
    toc: false
    title-block-banner: false
---

<div class="observable-embed">
  <iframe 
    src="{embed}?ui=classic"
    allow="cross-origin-isolated">
  </iframe>
</div>
"""

def write_index(folder):
    index_path = os.path.join(folder, "index.qmd")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write('---\n')
        f.write('format:\n')
        f.write('  html:\n')
        f.write('    toc: false\n')
        f.write('---\n\n')
        f.write('```{python}\n')
        f.write('#| echo: false\n')
        f.write('#| output: asis\n')
        f.write('import os\n')
        f.write('import re\n\n')
        f.write('def get_frontmatter(filepath):\n')
        f.write('    with open(filepath, "r", encoding="utf-8") as f:\n')
        f.write('        content = f.read()\n')
        f.write('    match = re.match(r"^---\\n(.*?)\\n---", content, re.DOTALL)\n')
        f.write('    if not match:\n')
        f.write('        return {}\n')
        f.write('    fm = {}\n')
        f.write('    for line in match.group(1).split("\\n"):\n')
        f.write('        if ":" in line:\n')
        f.write('            key, _, value = line.partition(":")\n')
        f.write('            fm[key.strip()] = value.strip().strip(\'"\')\n')
        f.write('    return fm\n\n')
        f.write('folder = os.getcwd()\n')
        f.write('pages = []\n\n')
        f.write('for fname in sorted(os.listdir(folder)):\n')
        f.write('    if fname.endswith(".qmd") and fname != "index.qmd":\n')
        f.write('        fm = get_frontmatter(os.path.join(folder, fname))\n')
        f.write('        title = fm.get("pagetitle", "")\n')
        f.write('        description = fm.get("description", "")\n')
        f.write('        if not title:\n')
        f.write('            continue\n')
        f.write('        pages.append((title, description, fname))\n\n')
        f.write('html = \'<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">\'\n')
        f.write('for title, description, link in pages:\n')
        f.write('    html += f\'<a href="{link}" style="text-decoration: none; color: inherit; border: 1px solid #ddd; border-radius: 8px; padding: 2rem; display: block;"><div style="font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;">{title}</div><div>{description}</div></a>\'\n')
        f.write('html += "</div>"\n\n')
        f.write('print(html)\n')
        f.write('```\n')
    print(f"Created: index.qmd")

folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "computational-geometry")

if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Created folder: {folder}")
else:
    print(f"Folder exists: {folder}")
    expected_files = {page["filename"] for page in pages} | {"index.qmd"}
    for fname in os.listdir(folder):
        if fname.endswith(".qmd") and fname not in expected_files:
            os.remove(os.path.join(folder, fname))
            print(f"Deleted: {fname}")

for page in pages:
    content = page_template.format(
        title=page["title"],
        description=page["description"],
        embed=page["embed"]
    )
    filepath = os.path.join(folder, page["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {page['filename']}")

write_index(folder)
print("\nDone!")