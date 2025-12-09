# README: The Independence Paradox in Scientific Careers

This repository accompanies the paper:  
**"The independence paradox in scientific careers"**

## 1. System Requirements

✅ **All software dependencies and operating systems (including version numbers)**  
- Python 3.9+  
- pandas >= 1.5.0  
- numpy >= 1.21  
- networkx >= 2.6  
- scikit-learn >= 1.0  
- statsmodels >= 0.13  
- matplotlib >= 3.5
- Requests >= 2.25
- BeautifulSoup4 >= 4.1
- Compatible OS: macOS Monterey, Windows 10+

✅ **Versions the software has been tested on**   
- macOS Ventura 13.0  
- Windows 11

✅ **Any required non-standard hardware**  
- No specialized hardware is required. The analysis can be performed on a standard desktop with ≥16GB RAM recommended for full dataset runs.

## 2. Installation Guide

✅ **Instructions**  
Clone the repository and install dependencies via `pip`:

✅ **Typical install time on a "normal" desktop computer**  
Installation typically completes in under 2 minutes with a stable internet connection.

## 3. Demo

✅ **Instructions to run on data**  
To reproduce the main figures and results:

To begin, load the input dataset described in the ‘demo dataset’ folder. Then, sequentially execute each Jupyter notebook in the ‘code’ folder.

✅ **Expected output**  
- `results/` will include:
  - impact metrics over time  
  - community dectection results  
  - Co-authorship network metrics  
  - Reproduction of key figures from the manuscript

✅ **Expected run time for demo on a "normal" desktop computer**  
- Full analysis on the sample data runs in ~5–10 minutes  
- Full-scale dataset (~500,000 pairs) may take several hours depending on hardware

## 4. Instructions for Use

✅ **How to run the software on your data**  
To apply the pipeline to your own mentor-mentee data:

--input your_data.csv --sequentially adjust and execute each Jupyter notebook in the ‘code’ folder --output your_results/


Ensure your data follows the expected schema:
```csv
mentee_id, mentor_id, year, mentee_publications, mentor_publications, coauthorships, topics
```

✅ **(OPTIONAL) Reproduction instructions**  
To reproduce all quantitative results in the manuscript:


This script will:
- Run all key analysis modules  
- Generate figures and tables used in the paper  
- Export a summary of statistical models and results

---
Please note that, at this stage, we are only providing the demo code and dataset necessary to reproduce the main results and figures related to the analysis in Chemistry presented in the manuscript. The full code and dataset will be made publicly available upon publication.

For any issues or questions, please contact: [yanmeng0608@outlook.com]
