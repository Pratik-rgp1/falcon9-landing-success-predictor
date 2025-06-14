# SpaceX Falcon 9 & Falcon Heavy Launches Data Analysis

## Overview
This project covers web scraping, data wrangling, and exploratory data analysis (EDA) on SpaceX Falcon 9 and Falcon Heavy launch records, extracted from the Wikipedia page snapshot as of June 9, 2021. The goal is to understand launch patterns, booster landing outcomes, and orbit missions, and to prepare the data for machine learning models predicting booster landing success.

---

## Contents

### Web Scraping & Data Extraction
- **Objective:** Scrape launch data from a Wikipedia page snapshot.
- **Tasks:**
  - Fetch the Falcon 9 and Falcon Heavy launch page HTML.
  - Extract relevant launch tables.
  - Parse the launch records into a structured dictionary.
  - Clean and normalize data fields such as date, booster version, payload mass, and landing status.
  - Convert dictionary to a Pandas DataFrame.
  - Export the scraped data to CSV (`spacex_web_scraped.csv`).

### Data Wrangling & Label Creation
- **Objective:** Prepare data for modeling by cleaning and generating labels.
- **Tasks:**
  - Load the scraped dataset.
  - Perform exploratory data analysis (EDA) to identify patterns and missing data.
  - Convert detailed landing outcomes into binary classification labels (1 = successful landing, 0 = unsuccessful).
  - Calculate booster landing success rate.
  - Export cleaned data with labels to CSV (`dataset_part_2.csv`).

###Exploratory Data Analysis (EDA)
- **Objective:** Analyze launch site usage, orbit types, mission outcomes.
- **Tasks:**
  - Calculate number of launches per launch site.
  - Analyze the distribution of orbits, including LEO, GTO, SSO, GEO, and others.
  - Count occurrences of different mission outcomes and landing success/failure by orbit.
  - Prepare data visualizations (optional).

---

## Datasets

- `spacex_web_scraped.csv` — Raw data scraped from the Wikipedia launch tables.
- `dataset_part_2.csv` — Cleaned dataset with landing success labels, ready for ML modeling.

---


- **Helper Functions:** 
  - `date_time()` — extracts date and time from HTML table cells.
  - `booster_version()` — extracts booster version info.
  - `landing_status()` — extracts booster landing status.
  - `get_mass()` — parses and normalizes payload mass.
  - `extract_column_from_header()` — cleans table headers for column names.

- **Key Python Libraries:**
  - `requests` — HTTP requests to fetch webpage.
  - `BeautifulSoup` — parsing and scraping HTML tables.
  - `pandas` — data manipulation and analysis.
  - `unicodedata` — text normalization.

---

## Usage Instructions

1. **Clone the repository** and navigate to the working directory.
2. **Install dependencies** using pip:
   ```bash
   pip install requests beautifulsoup4 pandas
