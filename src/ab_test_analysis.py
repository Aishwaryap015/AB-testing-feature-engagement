import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/ab_test_data.csv")

# Split groups
control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

# Metrics
control_ctr = control["clicked"].mean()
treatment_ctr = treatment["clicked"].mean()

control_conv = control["converted"].mean()
treatment_conv = treatment["converted"].mean()

# Hypothesis Testing (Conversion Rate)
t_stat, p_value = stats.ttest_ind(
    treatment["converted"],
    control["converted"],
    equal_var=False
)

print("=== A/B TEST RESULTS ===")
print(f"Control CTR: {control_ctr:.2%}")
print(f"Treatment CTR: {treatment_ctr:.2%}")
print(f"Control Conversion: {control_conv:.2%}")
print(f"Treatment Conversion: {treatment_conv:.2%}")
print(f"P-Value: {p_value:.4f}")

# Confidence Interval for Conversion Difference
diff = treatment_conv - control_conv

std_control = control["converted"].std()
std_treatment = treatment["converted"].std()

se = np.sqrt(
    (std_control**2 / len(control)) +
    (std_treatment**2 / len(treatment))
)

ci_low = diff - 1.96 * se
ci_high = diff + 1.96 * se

print(f"95% Confidence Interval for Conversion Lift: [{ci_low:.2f}, {ci_high:.2f}]")

# Final Decision
if p_value < 0.05:
    print("✅ Result is statistically significant. Recommend deploying Treatment.")
else:
    print("❌ No statistical significance. Keep Control.")

# Visualization
labels = ["Control", "Treatment"]
conversion_rates = [control_conv, treatment_conv]

plt.bar(labels, conversion_rates)
plt.ylabel("Conversion Rate")
plt.title("Conversion Rate Comparison")
plt.show()
