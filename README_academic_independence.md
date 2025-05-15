# README: Quantifying Academic Independence and the Association with Career Success

This repository accompanies the paper:  
**"Quantifying academic independence and the association with career success"**

## 1. System Requirements

✅ **All software dependencies and operating systems (including version numbers)**  
- Python 3.9+  
- pandas >= 1.5.0  
- numpy >= 1.21  
- networkx >= 2.6  
- scikit-learn >= 1.0  
- statsmodels >= 0.13  
- matplotlib >= 3.5  
- Compatible OS: Ubuntu 20.04+, macOS Monterey, Windows 10+

✅ **Versions the software has been tested on**  
- Ubuntu 22.04 LTS  
- macOS Ventura 13.0  
- Windows 11

✅ **Any required non-standard hardware**  
- No specialized hardware is required. The analysis can be performed on a standard desktop with ≥16GB RAM recommended for full dataset runs.

## 2. Installation Guide

✅ **Instructions**  
Clone the repository and install dependencies via `pip`:

```bash
git clone https://github.com/yourusername/academic-independence.git
cd academic-independence
pip install -r requirements.txt
```

✅ **Typical install time on a "normal" desktop computer**  
Installation typically completes in under 2 minutes with a stable internet connection.

## 3. Demo

✅ **Instructions to run on data**  
To reproduce the main figures and results:

```bash
python run_analysis.py --input data/processed_pairs.csv --output results/
```

✅ **Expected output**  
- `results/` will include:
  - Divergence metrics over time  
  - Topic evolution plots  
  - Co-authorship network metrics  
  - Reproduction of key figures from the manuscript

✅ **Expected run time for demo on a "normal" desktop computer**  
- Full analysis on the sample data runs in ~5–10 minutes  
- Full-scale dataset (~500,000 pairs) may take several hours depending on hardware

## 4. Instructions for Use

✅ **How to run the software on your data**  
To apply the pipeline to your own mentor-mentee data:

```bash
python run_analysis.py --input your_data.csv --output your_results/
```

Ensure your data follows the expected schema:
```csv
mentee_id, mentor_id, year, mentee_publications, mentor_publications, coauthorships, topics
```

✅ **(OPTIONAL) Reproduction instructions**  
To reproduce all quantitative results in the manuscript:

```bash
bash reproduce_all.sh
```

This script will:
- Run all key analysis modules  
- Generate figures and tables used in the paper  
- Export a summary of statistical models and results

---

We encourage you to include instructions for reproducing **all the quantitative results** in the manuscript.

For any issues or questions, please contact: [your_email@domain.edu]
