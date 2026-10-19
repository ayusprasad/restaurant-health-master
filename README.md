# Restaurant Review Health Analysis

[![CI](https://github.com/ayusprasad/restaurant-health-master/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/restaurant-health-master/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-pandas-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Analysis-Jupyter-F37626?logo=jupyter&logoColor=white)

A notebook-led exploratory analysis of restaurant review, business, and user-rating data.

## What the notebook covers

- Review and business rating distributions.
- User activity and review reactions.
- Restaurant feature relationships and clustering.
- Correlation, profiling, and data quality checks.

## Project layout

~~~text
notebooks/restaurant_health_analysis.ipynb  end-to-end exploratory analysis
data/restaurants.csv                      local source dataset (not tracked)
~~~

## Run locally

### Prerequisites

- Python 3.11 or newer
- JupyterLab or Jupyter Notebook
- The source restaurant dataset, placed at data/restaurants.csv

### Install

~~~bash
git clone https://github.com/ayusprasad/restaurant-health-master.git
cd restaurant-health-master
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab notebooks/restaurant_health_analysis.ipynb
~~~

Notebook outputs are cleared in version control. It checks for the local dataset path and stops with a clear message when the file is missing.

## Quality checks

~~~bash
python -m pytest -q
~~~

GitHub Actions validates the notebook JSON and runs structural tests without needing the dataset. No environment variables are required.
