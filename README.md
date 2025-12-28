# 🧪 A/B Test Analysis for Feature Engagement Improvement

## 📌 Objective
Evaluate whether a new product feature improves user engagement and conversion rate using an A/B experiment.

---

## 📊 Metrics Analyzed
- Click Through Rate (CTR)
- Conversion Rate
- Statistical Significance (p-value)
- 95% Confidence Interval

---

## 🧠 Hypothesis
- **H₀ (Null Hypothesis):** The new feature does not improve conversion.
- **H₁ (Alternative Hypothesis):** The new feature improves conversion.

---

## 🧪 Experiment Design
- Users randomly split into Control and Treatment groups
- Primary metric: Conversion Rate
- Statistical test: Two-sample t-test
- Confidence level: 95% (α = 0.05)

---

## 📈 Results Summary
- Treatment group showed higher CTR and conversion
- Statistical test returned a p-value greater than 0.05
- Confidence interval for conversion lift included zero

---

## ❗ Key Insight
Although the Treatment group showed higher CTR and conversion, the experiment did not achieve statistical significance due to limited sample size.

---

## 📌 Final Recommendation
Do not roll out the feature yet. Increase sample size and re-run the experiment to validate impact with sufficient statistical power.

---

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib

---

## 🎯 Business Value
This project demonstrates the ability to:
- Design controlled experiments
- Apply statistical reasoning
- Make data-driven product decisions
