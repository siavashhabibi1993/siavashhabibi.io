# Site Commands

## Preview locally

quarto preview

## Render full site

quarto render

## Render a single page

quarto render structural-engineering/mohrs-circle.qmd

## Render a single folder

quarto render structural-engineering/

## Push to GitHub Pages

git add .
git commit -m "Update site"
git push

## Regenerate section folders

python generators/generate_computational_geometry.py
python generators/generate_structural_engineering.py
python generators/generate_creative_coding.py

## Activate virtual environment (required before quarto preview/render)

.venv\Scripts\activate
