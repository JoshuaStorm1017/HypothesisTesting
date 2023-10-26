from scipy import stats
import numpy as np
from Functions import StatUtils


class DependentTest:

    @staticmethod
    # Function for dependent t-test
    def dependent_t_test(pre_data, post_data, Ha):
        # Perform paired sample t-test
        t_stat, two_tailed_p_val = stats.ttest_rel(post_data, pre_data)

        # Derive one-tailed p-value based on Ha and t_stat direction
        if Ha[5] == ">":
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
        elif Ha[5] == "<":
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

        return round(t_stat, 2), p_val

    @staticmethod
    def execute_test():
        # Collecting user inputs for data
        pre_data_input = input("Enter your pre data samples separated by commas (e.g., 7,5,8): ").split(',')
        post_data_input = input("Enter your post data samples separated by commas (e.g., 7,6,7): ").split(',')
        pre_data = np.array([float(sample) for sample in pre_data_input])
        post_data = np.array([float(sample) for sample in post_data_input])

        # Input and validation for hypotheses
        while True:
            Ha = input("Enter the alternative hypothesis 'Ha'(e.g., Mpost<Mpre): ")
            Ho = input("Enter the null hypothesis 'Ho'(e.g., Mpost>=Mpre): ")

            valid_Ho = (Ho[0:5].upper() == "MPOST" and (Ho[5:7] in ["<=", ">="] or Ho[5] in ["="]))
            valid_Ha = (Ha[0:5].upper() == "MPOST" and (Ha[5] in ["<", ">"] or Ha[5:7] in ["/="]))

            if valid_Ho and valid_Ha:
                break
            else:
                print("Please ensure that both hypotheses are entered correctly.")

        alpha = StatUtils.get_alpha()

        # Calculating t-statistic and p-value
        t_statistic, p_value = DependentTest.dependent_t_test(pre_data, post_data, Ha)

        # Draw conclusion based on p-value and alpha
        print(f"T-Statistic: {t_statistic: .2f}")
        print("Post Mean", np.mean(post_data))
        print("Pre Mean", np.mean(pre_data))
        print("Mean difference :", np.mean(post_data) - np.mean(pre_data))
        print(f"P-Value: {p_value: .3f}")
        conclusion = StatUtils.check_p_value(p_value, alpha, Ho, Ha)
        print(conclusion)
