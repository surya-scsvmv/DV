# Data Visualization Lab

A structured collection of data visualization laboratory experiments using Python and R. The repository includes dataset preparation, statistical analysis, chart creation, and plot-export exercises, organized by experiment number and descriptive title.

<p>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Language-R-276DC3?style=flat-square&logo=r&logoColor=white" alt="R"/>
  <img src="https://img.shields.io/badge/Experiments-18-2563EB?style=flat-square" alt="18 exercise files"/>
  <img src="https://img.shields.io/badge/Includes-Charts%20%26%20Analysis-0F766E?style=flat-square" alt="Charts and analysis"/>
</p>

## Contents

| Experiment | Concepts | Programs |
|---|---|---|
| **01 — Dataset Preparation** | DataFrames, data validation, summary statistics, CSV files | [1 - Sample Dataset.py](python/Experiment-01/1%20-%20Sample%20Dataset.py) |
| **02 — Python Visualization** | Matplotlib, Seaborn, basic plotting, line charts, bar charts, histograms, scatter plots, heatmaps, box plots | [2A - Basic Matplotlib Plot.py](python/Experiment-02/2A%20-%20Basic%20Matplotlib%20Plot.py), [2B - Line Chart.py](python/Experiment-02/2B%20-%20Line%20Chart.py), [2C - Bar Chart.py](python/Experiment-02/2C%20-%20Bar%20Chart.py), [2D - Histogram.py](python/Experiment-02/2D%20-%20Histogram.py), [2E - Scatter Plot.py](python/Experiment-02/2E%20-%20Scatter%20Plot.py), [2F - Correlation Heatmap.py](python/Experiment-02/2F%20-%20Correlation%20Heatmap.py), [2G - Box Plot.py](python/Experiment-02/2G%20-%20Box%20Plot.py) |
| **03 — R Visualization** | R environment, data frames, base graphics, ggplot2, statistical plots | [3A - R Environment Setup.R](r/Experiment-03/3A%20-%20R%20Environment%20Setup.R), [3B - Student Dataset.R](r/Experiment-03/3B%20-%20Student%20Dataset.R), [3C - Base R Bar Chart.R](r/Experiment-03/3C%20-%20Base%20R%20Bar%20Chart.R), [3D - Line Chart.R](r/Experiment-03/3D%20-%20Line%20Chart.R), [3E - Histogram.R](r/Experiment-03/3E%20-%20Histogram.R), [3F - Box Plot.R](r/Experiment-03/3F%20-%20Box%20Plot.R), [3G - Regression Scatter Plot.R](r/Experiment-03/3G%20-%20Regression%20Scatter%20Plot.R), [3H - Grouped Bar Chart.R](r/Experiment-03/3H%20-%20Grouped%20Bar%20Chart.R), [3I - Pie Chart.R](r/Experiment-03/3I%20-%20Pie%20Chart.R) |
| **04 — Plot Export** | Saving graphics in PNG format using base R and ggplot2 | [4A - Saving Plots.R](r/Experiment-04/4A%20-%20Saving%20Plots.R) |

## Repository structure

```text
DV/
├── data/
│   ├── README.md
│   └── student_scores.csv
├── python/
│   ├── Experiment-01/
│   │   └── 1 - Sample Dataset.py
│   └── Experiment-02/
│       ├── 2A - Basic Matplotlib Plot.py
│       ├── 2B - Line Chart.py
│       ├── 2C - Bar Chart.py
│       ├── 2D - Histogram.py
│       ├── 2E - Scatter Plot.py
│       ├── 2F - Correlation Heatmap.py
│       ├── 2G - Box Plot.py
│       └── common.py
├── r/
│   ├── Experiment-03/
│   │   ├── 3A - R Environment Setup.R
│   │   ├── 3B - Student Dataset.R
│   │   ├── 3C - Base R Bar Chart.R
│   │   ├── 3D - Line Chart.R
│   │   ├── 3E - Histogram.R
│   │   ├── 3F - Box Plot.R
│   │   ├── 3G - Regression Scatter Plot.R
│   │   ├── 3H - Grouped Bar Chart.R
│   │   └── 3I - Pie Chart.R
│   ├── Experiment-04/
│   │   └── 4A - Saving Plots.R
│   └── common.R
├── output/
├── tests/
│   └── test_python_experiments.py
└── README.md
```

## Dataset

The shared dataset is stored in `data/student_scores.csv` and contains 10 fictional student records.

| Column | Description |
|---|---|
| `Student` | Student name |
| `Math`, `Science`, `English` | Subject marks (0–100) |
| `Age` | Student age in years |
| `Hours_Studied` | Study hours per day |

## Requirements

- **Python:** Python 3.10+ with Pandas, NumPy, Matplotlib, and Seaborn.
- **R:** R 4.2+ with ggplot2, tidyr, dplyr, and RColorBrewer.
- **Environment:** Python IDE / terminal and an R IDE or Rscript.

Install the Python packages with:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

Run the R environment setup program once to install the required R packages.

## Run the experiments

Run commands from the repository's main directory.

**Python**

```bash
python "python/Experiment-01/1 - Sample Dataset.py"
python "python/Experiment-02/2A - Basic Matplotlib Plot.py"
python "python/Experiment-02/2B - Line Chart.py"
python "python/Experiment-02/2C - Bar Chart.py"
python "python/Experiment-02/2D - Histogram.py"
python "python/Experiment-02/2E - Scatter Plot.py"
python "python/Experiment-02/2F - Correlation Heatmap.py"
python "python/Experiment-02/2G - Box Plot.py"
```

**R**

```bash
Rscript "r/Experiment-03/3A - R Environment Setup.R"
Rscript "r/Experiment-03/3B - Student Dataset.R"
Rscript "r/Experiment-03/3C - Base R Bar Chart.R"
Rscript "r/Experiment-03/3D - Line Chart.R"
Rscript "r/Experiment-03/3E - Histogram.R"
Rscript "r/Experiment-03/3F - Box Plot.R"
Rscript "r/Experiment-03/3G - Regression Scatter Plot.R"
Rscript "r/Experiment-03/3H - Grouped Bar Chart.R"
Rscript "r/Experiment-03/3I - Pie Chart.R"
Rscript "r/Experiment-04/4A - Saving Plots.R"
```

Generated charts are stored in the `output/` directory.

## Lab-submission checklist

- [ ] All prescribed experiments are present and numbered correctly.
- [ ] Each source file has a descriptive title and readable implementation.
- [ ] The dataset columns and score ranges are validated.
- [ ] Charts include appropriate titles, axes, labels, and legends.
- [ ] Generated plot files are checked before attaching them to a lab record.
- [ ] Programs are executed in the actual lab environment.

## Academic context

Data Visualization Laboratory coursework — SCSVMV University, Computer Science and Engineering (AI & Data Science).

## Related repositories

- [Java Programming Lab](https://github.com/surya-scsvmv/JAVA)
- [DSA in C](https://github.com/surya-scsvmv/DSA)
- [C++ Programming Lab](https://github.com/surya-scsvmv/CPP)
- [Design and Analysis of Algorithms](https://github.com/surya-scsvmv/DAA)
- [DBMS Laboratory](https://github.com/surya-scsvmv/DBMS)

---

<p align="center">Prepare the data. Visualize the patterns. Interpret the results.</p>
