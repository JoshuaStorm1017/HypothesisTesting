from scipy.stats import chi2
from Functions import StatUtils


class OneProportionChi2Test:

    @staticmethod
    def one_proportion_chi2_test(k1, n, P0, Ha):
        # Calculate sample proportion
        p = k1 / n

        # Compute the chi-squared statistic
        chi2_stat = n * (p - P0) ** 2 / (P0 * (1 - P0))

        # p-value from the chi-squared distribution
        p_val = 1 - chi2.cdf(chi2_stat, df=1)

        # Determine the p-value based on Ha and residual
        residual = k1 - n * P0
        if Ha[1] == ">":
            if residual > 0:
                p_val = round(p_val + 0.0001, 3) / 2
                print(
                    "Since the alternative hypothesis suggests a greater value and the residual is positive, we use the one-tailed p-value (p-value/2).")
            else:
                p_val = 1 - (round(p_val + 0.0001, 3) / 2)
                print(
                    "Since the alternative hypothesis suggests a greater value but the residual is negative, we use 1 minus the one-tailed p-value (p-value/2).")
        elif Ha[1] == "<":
            if residual < 0:
                p_val = round(p_val + 0.0001, 3) / 2
                print(
                    "Since the alternative hypothesis suggests a lesser value and the residual is negative, we use the one-tailed p-value (p-value/2).")
            else:
                p_val = 1 - (round(p_val + 0.0001, 3) / 2)
                print(
                    "Since the alternative hypothesis suggests a lesser value but the residual is positive, we use 1 minus the one-tailed p-value (p-value/2).")
        else:
            p_val = round(p_val + 0.0001, 3)
            print("We use the two-tailed p-value since there's no clear direction in the alternative hypothesis.")

        return round(chi2_stat, 2), p_val, residual

    @staticmethod
    def execute_test():
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

        alpha = StatUtils.get_alpha()

        chi_square, p_value, residual = OneProportionChi2Test.one_proportion_chi2_test(k1, n, P0, Ha)
        print(f"\nChi-square: {chi_square: .2f}")
        print(f"P-Value: {p_value: .3f}")
        print(f"Residual: {residual}")

        # Draw conclusion based on p-value and alpha
        conclusion = StatUtils.check_p_value(p_value, alpha, Ho, Ha)
        print(conclusion)
