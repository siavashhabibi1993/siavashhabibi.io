import os

pages = [
    {
        "embed": "https://observablehq.com/embed/@syaleni/mohrs-circle",
        "title": "Mohr's Circle",
        "description": "Interactive Mohr's Circle for stress transformation and principal stress visualization.",
        "filename": "mohrs-circle.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/section-properties-calculator",
        "title": "Section Properties Calculator",
        "description": "Interactive calculator for cross-section properties including moment of inertia, centroid, and section modulus.",
        "filename": "section-properties.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/simply-supported-beam",
        "title": "Analysis of a Simply Supported Beam",
        "description": "Interactive analysis of a simply supported beam with shear force and bending moment diagrams.",
        "filename": "simply-supported-beam.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/untitled",
        "title": "Flexural Resistance of a Reinforced Concrete Beam",
        "description": "Interactive calculator for the flexural resistance of reinforced concrete beams per CSA design standards.",
        "filename": "reinforced-concrete-beam.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/94e1b9b15982b882",
        "title": "Glass Panel Load Calculation",
        "description": "Interactive calculator for glass panel load capacity and thickness design per structural glazing standards.",
        "filename": "glass-panel.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/structural-panels",
        "title": "Structural Wood Panels",
        "description": "Interactive reference and design tool for structural wood panels and sheathing properties.",
        "filename": "structural-wood-panels.qmd"
    },
    {
        "embed": "https://observablehq.com/embed/@syaleni/soil-pressure-coefficients",
        "title": "Soil Pressure Coefficients",
        "description": "Interactive visualization of active and passive soil pressure coefficients using Rankine and Coulomb theories.",
        "filename": "soil-pressure-coefficients.qmd"
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

folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "structural-engineering")

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