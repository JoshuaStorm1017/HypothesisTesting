import numpy as np
from scipy import stats
from Functions import StatUtils


class OneSampleTTest:

    @staticmethod
    def one_sample_t_test(data, test_value, Ha):
        # Perform the one-sample t-test
        t_stat, two_tailed_p_val = stats.ttest_1samp(data, test_value)

        print(f"\nTwo-tailed p-value: {round(two_tailed_p_val, 3)}")

        # Derive the one-tailed p-value based on Ha and t_stat direction
        if Ha[1] == ">":
            if t_stat > 0:
                p_val = round(two_tailed_p_val, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a greater value and the t-statistic is positive(see below), we divide the two-tailed p-value by 2.")
            else:
                p_val = 1 - (round(two_tailed_p_val, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a greater value but the t-statistic is negative(see below), we use 1 minus the two-tailed p-value divided by 2.")
        elif Ha[1] == "<":
            if t_stat < 0:
                p_val = round(two_tailed_p_val, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a lesser value and the t-statistic is negative(see below), we divide the two-tailed p-value by 2.")
            else:
                p_val = 1 - (round(two_tailed_p_val, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a lesser value but the t-statistic is positive(see below), we use 1 minus the two-tailed p-value divided by 2.")
        else:
            p_val = round(two_tailed_p_val, 3)
            print(
                "We use the two-tailed p-value directly since there's no clear direction in the alternative hypothesis.")

        return round(t_stat, 2), p_val

    @staticmethod
    def execute_test():
        # Collecting user inputs
        data_samples_input = input("Enter your data samples separated by commas (e.g., 29,28,31): ").split(',')
        data_samples = np.array([float(sample) for sample in data_samples_input])

        test_value = float(input("Enter the test value: "))

        # Input and validation for hypotheses
        while True:
            Ha = input("Enter the alternative hypothesis (e.g., M>30): ")
            Ho = input("Enter the null hypothesis (e.g., M<=30): ")

            valid_Ho = (Ho[0].upper() == "M" and (Ho[1:3] in ["<=", ">="] or Ho[1] in ["="]))
            valid_Ha = (Ha[0].upper() == "M" and (Ha[1] in ["<", ">"] or Ha[1:3] in ["/="]))

            if valid_Ho and valid_Ha:
                break
            else:
                print("Please ensure that both hypotheses are entered correctly.")

        alpha = StatUtils.get_alpha()

        t_statistic, p_value = OneSampleTTest.one_sample_t_test(data_samples, test_value, Ha)
        print(f"\nT-Statistic: {t_statistic: .2f}")
        print(f"Resulting P-Value: {p_value: .3f}")

        # Draw conclusion based on p-value and alpha
        conclusion = StatUtils.check_p_value(p_value, alpha, Ho, Ha)
        print(conclusion)

