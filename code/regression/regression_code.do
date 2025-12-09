
**Load dataset(Only one of the three commands should be used for each analysis)
use regression_neuro.dta, clear //using for the analysis in Neuroscience
use regression_chemistry.dta, clear //using for the analysis in Chemistry
use regression_physics.dta, clear //using for the analysis in Physics


*Generate squared term for average distance
gen ave_distance_sq = ave_distance^2


* Log-transform dependent variable to address skewness
gen ln_sum_credit = log(sum_credit)


** Log-transform control variables

// Mentee-related Factors
gen ln_career_len_mte = log(career_len_mte + 1)
gen ln_mte_work_count_first_5y = log(mte_work_count_first_5y + 1)

// Mentor-related Factors
gen ln_topic_num_mto = log(topic_num_mto + 1 )
gen ln_total_cits_mto = log(total_cits_mto + 1)

// Mentee-Mentor Collaboration Factors
gen ln_colla_work_count = log(colla_work_count + 1)
gen ln_colla_work_count_first_5y = log(colla_work_count_first_5y + 1)
gen ln_colla_work_count_later = log(colla_work_count_later + 1)
gen ln_common_cllaborators_count = log(common_cllaborators_count + 1)


* Define career length threshold for analysis
gen length =35


----------------------------regression analysis---------------------------------------------

* Hierarchical regression analysis for mentors with career length >=35
regress ln_sum_credit ave_distance if career_len_mte>=length
estimates store M1  // Base model: Linear effect of distance

regress ln_sum_credit ave_distance ave_distance_sq if career_len_mte>=length
estimates store M2 // Quadratic model: Testing nonlinear distance effect

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte if career_len_mte>=length 
estimates store M3  // Control for mentor career length

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y if career_len_mte>=length
estimates store M4 // Add early career output measure

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto if career_len_mte>=length
estimates store M5  // Include the number of mentors topics

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto ln_total_cits_mto if career_len_mte>=length
estimates store M6 // Add mentee citation count

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto ln_total_cits_mto ln_colla_work_count if career_len_mte>=length
estimates store M7 // Include total collaboration count of mentee and mentor

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto ln_total_cits_mto ln_colla_work_count_first_5y  if career_len_mte>=length
estimates store M8 // Add early collaboration count

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto ln_total_cits_mto ln_colla_work_count_first_5y ln_colla_work_count_later if career_len_mte>=length // Include later collaboration count of mentee and mentor
estimates store M9

regress ln_sum_credit ave_distance ave_distance_sq ln_career_len_mte ln_mte_work_count_first_5y ln_topic_num_mto ln_total_cits_mto ln_colla_work_count_first_5y ln_colla_work_count_later ln_common_cllaborators_count if career_len_mte>=length
estimates store M10 // Control for shared collaborators of mentee and mentor


* Export regression results to CSV with standardized formatting
esttab M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 using reg_results.csv, replace ///
    cells(b(star fmt(3)) se(par)) stats(r2 N, labels("R-squared" "Observations")) ///
    mlabels("Model 1" "Model 2" "Model 3" "Model 4" "Model 5" "Model 6" "Model 7" "Model 8" "Model 9" "Model 10" "Model 11") ///
    starlevels(* 0.10 ** 0.05 *** 0.01) ///
    nonumbers collabels(none) ///
    title(Regression Results)
