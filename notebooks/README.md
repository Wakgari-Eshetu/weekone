Correlation between News Sentiment and Stock Returns

Purpose:
Summarizes Task 3: compute daily news sentiment from headlines and test correlation with daily stock returns for several tickers (AAPL, AMZN, GOOG, etc.) using task3.ipynb.

Files:

task3.ipynb : main analysis notebook (sentiment, merging with price data, correlation, visualizations).
raw_analyst_ratings.csv : source headlines / news data.
data/data/<TICKER>.csv : historical stock prices for each ticker (e.g., AAPL.csv, AMZN.csv).
Key steps performed:

Clean and align dates in news and stock data.
Compute sentiment for each headline using TextBlob (polarity).
Aggregate sentiment to daily average and merge with stock daily returns.
Compute correlation (Pearson) and visualize scatter, time-series, density plots, and 10-day rolling correlation.
Environment / Dependencies:

Python 3.8+ recommended. Primary packages used: pandas, nltk, textblob, matplotlib, seaborn.
Notebook expects a Python kernel linked to the project venv (e.g., waksvenv) or any interpreter with the above packages installed.
Quick Setup (PowerShell on Windows):

How to run the notebook:

Open task3.ipynb in VS Code or Jupyter.
Ensure the kernel (top-right) is Python (waksvenv) or the interpreter with the dependencies.
Restart kernel and run cells from top to bottom. The notebook prints head samples, correlation values, and displays plots.
Notes on NLTK/TextBlob:

TextBlob uses nltk under the hood; ensure nltk and the required corpora (punkt, stopwords, wordnet) are installed.
If you see ModuleNotFoundError: No module named 'nltk', either the notebook kernel uses a different Python or nltk is not installed in the active interpreter. Use the PowerShell commands above to install into the correct venv.
Expected outputs:

A printed correlation score (example: Correlation between news sentiment and daily stock returns: 0.0123).
Scatter plot of daily sentiment vs daily return, time-series plot of sentiment and returns, density histograms, and 10-day rolling correlation plot.
Troubleshooting:

If imports fail in the notebook but work in the terminal: confirm the notebook kernel matches the venv. Check sys.executable inside a quick cell:
If nltk is installed yet tokenizers/data raise errors, run:
Execution policy errors when activating venv in PowerShell:
Next steps / enhancements (suggested):
Replace TextBlob with a stronger sentiment model (VADER or transformer-based) for better financial sentiment.
Use intraday timestamps where available to align news with intraday stock moves.
Add statistical significance testing (p-values) or lagged correlation analysis.
If you'd like, I can:

Create and save this README as notebooks/README_task3.md (I can write the file now), or
Add a short "Getting started" cell at the top of task3.ipynb that performs environment checks and prints sys.executable and package versions.
Which would you prefer?