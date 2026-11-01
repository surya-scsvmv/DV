<div align="center">

# DATA VISUALIZATION LAB

**A practical Python and R laboratory for exploring student-performance data.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.2%2B-276DC3?logo=r&logoColor=white)](https://www.r-project.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-statistical%20plots-4C72B0)](https://seaborn.pydata.org/)
[![ggplot2](https://img.shields.io/badge/ggplot2-R%20graphics-7A9ECA)](https://ggplot2.tidyverse.org/)

</div>

---

## Overview

This repository contains hands-on exercises covering data preparation, exploratory analysis, statistical graphics, and plot export. The same student-score dataset is used throughout so that Python and R workflows can be compared consistently.

## Repository structure

```text
DV/
├── data/student_scores.csv
├── python/1.py, 2B.py–2G.py, common.py
├── r/3A.R–3I.R, 4A.R, common.R
├── output/
├── tests/
├── requirements.txt
└── README.md
```

## Experiment index

### Python — Pandas, NumPy, Matplotlib and Seaborn

| File | Experiment | Main concepts |
|---|---|---|
| [`1.py`](python/1.py) | Student-score dataset | DataFrames, NumPy, validation, CSV export |
| [`2B.py`](python/2B.py) | Subject score line chart | Multiple series, markers, legends |
| [`2C.py`](python/2C.py) | Average score bar chart | Aggregation, labels, ranking |
| [`2D.py`](python/2D.py) | Mathematics histogram | Frequency distribution, mean reference |
| [`2E.py`](python/2E.py) | Study-hours scatter plot | Correlation, linear trend, annotations |
| [`2F.py`](python/2F.py) | Correlation heatmap | Correlation matrix, colour encoding |
| [`2G.py`](python/2G.py) | Subject box plots | Quartiles, spread, outliers |

### R — Base graphics and ggplot2

| File | Experiment | Main concepts |
|---|---|---|
| [`3A.R`](r/3A.R) | R environment setup | Package installation and loading |
| [`3B.R`](r/3B.R) | Student-score dataset | Data frames, validation, CSV export |
| [`3C.R`](r/3C.R) | Base R bar chart | Subject averages, reference line |
| [`3D.R`](r/3D.R) | ggplot2 line chart | Long-form data, grouped series |
| [`3E.R`](r/3E.R) | ggplot2 histogram | Bins, distribution, mean marker |
| [`3F.R`](r/3F.R) | ggplot2 box plot | Quartiles, jittered observations |
| [`3G.R`](r/3G.R) | Scatter plot with regression | Linear model, confidence band |
| [`3H.R`](r/3H.R) | Grouped bar chart | Side-by-side categorical comparison |
| [`3I.R`](r/3I.R) | A-grade pie chart | Threshold counts, proportions |
| [`4A.R`](r/4A.R) | Saving plots | PNG export from ggplot2 and base R |

> **Numbering note:** The supplied exercise sequence begins at 2B; no 2A exercise was present. The numbering is intentionally preserved rather than inventing an additional experiment.

## Dataset

`data/student_scores.csv` contains 10 fictional student records with these fields:

- `Student` — student label
- `Math`, `Science`, `English` — subject marks on a 0–100 scale
- `Age` — age in years
- `Hours_Studied` — hours studied per day

The Python and R dataset scripts can regenerate the CSV. Keep the column names unchanged when editing the data because the plotting scripts use them directly.

## Getting started

### Clone

```bash
git clone https://github.com/surya-scsvmv/DV.git
cd DV
```

### Python

Python 3.10 or later is recommended.

```bash
python -m venv .venv
```

Activate with `.venv\\Scripts\\activate` on Windows or `source .venv/bin/activate` on macOS/Linux, then run:

```bash
pip install -r requirements.txt
python python/1.py
python python/2B.py
python python/2C.py
python python/2D.py
python python/2E.py
python python/2F.py
python python/2G.py
```

### R

Install R 4.2 or later. Run the setup script once, then the exercises from the repository root:

```bash
Rscript r/3A.R
Rscript r/3B.R
Rscript r/3C.R
Rscript r/3D.R
Rscript r/3E.R
Rscript r/3F.R
Rscript r/3G.R
Rscript r/3H.R
Rscript r/3I.R
Rscript r/4A.R
```

`3A.R` installs missing packages: `ggplot2`, `tidyr`, `dplyr`, and `RColorBrewer`.

## Output and tests

Chart images are saved in `output/`. Generated PNG files are ignored by Git so that running exercises does not create noisy commits.

Run Python checks from the repository root:

```bash
python -m unittest discover -s tests -v
```

## Learning outcomes

- Create, inspect, validate, and export tabular datasets.
- Choose suitable charts for categorical and numerical data.
- Summarise data with averages, distributions, and correlations.
- Reshape data between wide and long formats.
- Build charts with Python and R visualisation libraries.
- Export plot images for reports and presentations.

---

<div align="center">

**Built for learning, experimentation, and reproducible data visualisation.**

</div>
