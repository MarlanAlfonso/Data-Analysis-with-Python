# Asset Management Guide

> Reference for how to capture, name, and embed screenshots, visualizations, and your certificate in this repository.

---

## Folder Structure

```
assets/
├── certificate/
│   └── certificate.png              ← Your earned certificate (PNG, downloaded from freeCodeCamp)
├── screenshots/
│   ├── mean-variance-std-calculator-output.png
│   ├── demographic-data-analyzer-output.png
│   ├── medical-data-visualizer-output.png
│   ├── page-view-time-series-visualizer-output.png
│   └── sea-level-predictor-output.png
└── visualizations/
    ├── medical-data-visualizer-catplot.png
    ├── medical-data-visualizer-heatmap.png
    ├── page-view-time-series-visualizer-line.png
    ├── page-view-time-series-visualizer-bar.png
    ├── page-view-time-series-visualizer-box.png
    └── sea-level-predictor-scatter.png
```

---

## Naming Convention

Use `kebab-case` for all files. Follow the pattern:

```
[project-name]-[output-type].[ext]

Examples:
  sea-level-predictor-scatter.png
  medical-data-visualizer-heatmap.png
  mean-variance-std-calculator-output.png
```

---

## How to Save Matplotlib/Seaborn Plots

Always save figures programmatically from your script — do NOT use screenshot tools for chart outputs.

```python
# Matplotlib
fig.savefig('../../assets/visualizations/sea-level-predictor-scatter.png',
            dpi=150, bbox_inches='tight')

# Seaborn catplot (returns FacetGrid, not Axes)
g = sns.catplot(...)
g.fig.savefig('../../assets/visualizations/medical-data-visualizer-catplot.png',
              dpi=150, bbox_inches='tight')
```

**Settings to always use:**
- `dpi=150` — High resolution, readable on GitHub
- `bbox_inches='tight'` — Prevents axis labels from being clipped

---

## How to Take Terminal/Notebook Screenshots

For showing unit test results or console output:

**macOS:** `Cmd + Shift + 4` → drag to select region  
**Windows:** `Win + Shift + S` (Snipping Tool)  
**Linux:** `gnome-screenshot -a` or `scrot -s`

Save to `assets/screenshots/[project-name]-output.png`.

---

## Embedding Images in README.md

### Project output screenshot (in a project's own README.md)

```markdown
## Output

![Mean-Variance-Std Calculator Output](../../assets/screenshots/mean-variance-std-calculator-output.png)
```

### Visualization in the master README.md

```markdown
## Sample Output — Medical Data Visualizer

| Categorical Plot | Heatmap |
|:---:|:---:|
| ![catplot](./assets/visualizations/medical-data-visualizer-catplot.png) | ![heatmap](./assets/visualizations/medical-data-visualizer-heatmap.png) |
```

Using a table with two columns creates a clean side-by-side layout that renders well on GitHub.

### Certificate

```markdown
## 🏆 Certificate of Completion

![freeCodeCamp Data Analysis with Python Certificate](./assets/certificate/certificate.png)

[Verify on freeCodeCamp →](https://freecodecamp.org/certification/your-username/data-analysis-with-python)
```

---

## Downloading Your freeCodeCamp Certificate

1. Go to [freecodecamp.org](https://www.freecodecamp.org) and log in
2. Navigate to **Settings → Certifications**
3. Claim the certification (requires all 5 projects submitted and passed)
4. Right-click the certificate image → **Save image as** → save as `certificate.png`
5. Place it in `assets/certificate/certificate.png`
6. Uncomment the certificate block in `README.md`

---

## Image Size Recommendations

| Asset Type | Recommended Width | Format |
|------------|------------------|--------|
| Certificate | 1200–1400 px | PNG |
| Chart/visualization | 900–1200 px | PNG |
| Terminal screenshot | 800–1000 px | PNG |

GitHub renders images at full container width. Keeping files under **500 KB** prevents slow page loads.

---

*No external image hosting needed — all assets live in the repo and render natively on GitHub.*