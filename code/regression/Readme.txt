
This folder contains files related to replicating Figure 6 in paper, mainly involving regression analysis and result visualization operations.


1. File Descriptions

--regression_chemistry.dta: Data file for regression analysis in the field of Chemistry.

--regression_neuro.dta: Data file for regression analysis in the field of Neuroscience.

--regression_physics.dta: Data file for regression analysis in the field of Physics.

--regression_code.do: Stata code file used to execute regression analysis operations.

--reg_results_chem.xlsx: Result table file obtained from the regression analysis in the Chemistry field.

--reg_results_neuro.xlsx: Result table file obtained from the regression analysis in the Neuroscience field.

--reg_results_physics.xlsx: Result table file obtained from the regression analysis in the Physics field.

--visualization chart for regression coefficients.py: Python code file for visualizing regression coefficients.

--regression_coefficients.pdf: Final generated visualization chart file of regression coefficients.


2. Operation Steps

---Run Regression Analysis in Stata
Open the Stata software and execute the code in the regression_code.do file. This code will perform regression analysis based on different dataset files (regression_chemistry.dta, regression_neuro.dta, regression_physics.dta) respectively, and generate corresponding result files reg_results_chem.xlsx, reg_results_neuro.xlsx, and reg_results_physics.xlsx.

---Visualize Using Python
Ensure that Python and relevant dependent libraries (such as matplotlib, numpy, etc.) are installed, and run the visualization chart for regression coefficients.py file. This script will read the above - generated Excel result files, perform visualization processing on the regression coefficients, and output the final visualization chart as the regression_coefficients.pdf file.
