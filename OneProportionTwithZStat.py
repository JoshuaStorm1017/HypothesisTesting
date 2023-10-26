import numpy as np
from scipy.stats import norm

def one_proportion_z_test(k1, n, P0, Ha):
    # Calculate sample proportion
    p = k1 / n

    # Compute the z-test statistic
    z = (p - P0) / np.sqrt(P0 * (1 - P0) / n)

    # Two-tailed p-value
    two_tailed_p_val = 2 * (1 - norm.cdf(abs(z)))

    # Determine the one-tailed p-value based on Ha and residual
    residual = k1 - n * P0
    if Ha[1] == ">":
        if residual > 0:
            p_val = two_tailed_p_val / 2
        else:
            p_val = 1 - (two_tailed_p_val / 2)
    elif Ha[1] == "<":
        if residual < 0:
            p_val = two_tailed_p_val / 2
        else:
            p_val = 1 - (two_tailed_p_val / 2)
    else:  # Assume two-tailed test
        p_val = two_tailed_p_val

    return z, p_val, residual

# Collecting user inputs
k1 = float(input("Enter the number of 'yes' (k1) responses: "))
k2 = float(input("Enter the number of 'no' (k2) responses: "))
n = k1 + k2
P0 = float(input("Enter the hypothesized population proportion (e.g., 0.1 for 10%): "))

# Input and validation for hypotheses
while True:
    Ha = input("Enter the alternative hypothesis (e.g., P>0.1): ")
    Ho = input("Enter the null hypothesis (e.g., P<=0.1): ")

    valid_Ho = (Ho[0].upper() == "P" and (Ho[1:3] in ["<=", ">="] or Ho[1] in ["="]))
    valid_Ha = (Ha[0].upper() == "P" and (Ha[1] in ["<", ">"] or Ha[1:3] in ["/="]))

    if valid_Ho and valid_Ha:
        break
    else:
        print("Please ensure that both hypotheses are entered correctly.")

alpha = float(input("Enter the significance level (e.g., 0.05 or 0.01): "))

z_statistic, p_value, residual = one_proportion_z_test(k1, n, P0, Ha)
print(f"\nZ-Statistic: {z_statistic}")
print(f"P-Value: {p_value}")
print(f"Residual: {residual}")

# Draw conclusion based on p-value and alpha
if p_value > alpha:
    conclusion = Ho
else:
    conclusion = Ha

print(f"Conclusion: {conclusion}")
