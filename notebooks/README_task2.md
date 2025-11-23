# Task 2 — Data Preparation & Exploratory Analysis

**Purpose:**
- **Summary:** Task 2 prepares and explores the news and stock datasets used in later tasks. It performs cleaning, type conversions, basic EDA (head, missing values, distributions), and outputs data ready for sentiment analysis and correlation tests.

**Files:**
- `notebooks/task-2.ipynb` or `notebooks/task2.ipynb`: main notebook for Task 2 (open this file to run the steps).  
- `data/raw_analyst_ratings.csv`: raw news/headlines dataset.  
- `data/data/<TICKER>.csv`: historical stock price CSV files used for returns and merging.

**Key steps performed in the notebook:**
- Load CSVs into `pandas` DataFrames.  
- Convert date columns to `datetime` and align formats between datasets.  
- Drop or handle missing values in critical columns (e.g., `headline`, `date`, `Close`).  
- Compute basic derived fields if present (e.g., percent changes, day-of-week).  
- Save or prepare cleaned dataframes for subsequent tasks (merging and sentiment analysis).

**Dependencies (minimum):**
- Python 3.8+  
- `pandas`  
- Optional for later steps: `nltk`, `textblob`, `matplotlib`, `seaborn` (these are not strictly required for initial cleaning but used in downstream notebooks).

**Quick Setup (PowerShell):**
```powershell
# activate your venv (adjust path)
& 'C:\Users\HP\Downloads\Wak''sDataScienceprojects\waksvenv\Scripts\Activate.ps1'

# install pandas if not present
pip install --upgrade pip
pip install pandas
```

**How to run Task 2 notebook:**
1. Open `notebooks/task2.ipynb` in VS Code or Jupyter.  
2. Select the kernel corresponding to your project venv (example: `Python (waksvenv)`) to ensure consistent package availability.  
3. Restart the kernel and run cells top-to-bottom.  
4. Inspect printed outputs and saved intermediate files (if the notebook writes cleaned CSVs back to `data/processed/` or similar).

**Verification cell to add / run (recommended):**
Run this at the top of the notebook to confirm interpreter and package availability:
```python
import sys
import pandas as pd
print('Python:', sys.executable)
print('pandas:', pd.__version__)
```

**Troubleshooting:**
- If `ModuleNotFoundError` appears for `pandas`, confirm the notebook kernel matches the venv where `pandas` is installed. Check `sys.executable` as shown above.  
- If date parsing yields many `NaT`, inspect the raw date strings and adjust `pd.to_datetime(..., errors='coerce', dayfirst=...)` or supply the correct `format=`.  
- If merges produce unexpectedly few rows, check both DataFrames for matching date types (both should be `datetime.date` or `datetime64[ns]`) and identical granularity (date vs datetime).

**Suggested next steps:**
- Save cleaned data to `data/processed/` for reproducibility.  
- Add unit checks (rows > 0, no nulls in key columns) before using cleaned data in Task 3.  
- Add small data-quality summary (counts, missing %) at the end of the notebook.

---
If you'd like, I can:
- Add this README file to the repository now (done), or
- Add a small top-of-notebook cell that prints `sys.executable`, package versions, and a short data-quality summary — tell me if you want me to insert that cell into `task2.ipynb`.