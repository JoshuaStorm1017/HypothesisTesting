from scipy import stats
import numpy as np
from Functions import StatUtils


class IndependentTest:

    @staticmethod
    # Function for independent t-test
    def independent_t_test(group1, group2, Ha, alpha):
        # Levene's test for equality of variances
        levene_stat, levene_p = stats.levene(group1, group2, center='mean')

        # Perform independent sample t-test
        if levene_p > alpha:
            t_stat, two_tailed_p_val = stats.ttest_ind(group1, group2, equal_var=True)
        else:
            t_stat, two_tailed_p_val = stats.ttest_ind(group1, group2, equal_var=False)

        # Derive one-tailed p-value based on Ha and t_stat direction
        if Ha[2] == ">":
            if t_stat > 0:
                p_val = round(two_tailed_p_val, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a greater value and the t-statistic is positive, we divide the two-tailed p-value by 2.")
            else:
                p_val = 1 - (round(two_tailed_p_val, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a greater value but the t-statistic is negative, we use 1 minus the two-tailed p-value divided by 2.")
        elif Ha[2] == "<":
            if t_stat < 0:
                p_val = round(two_tailed_p_val, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a lesser value and the t-statistic is negative, we divide the two-tailed p-value by 2.")
            else:
                p_val = 1 - (round(two_tailed_p_val, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests a lesser value but the t-statistic is positive, we use 1 minus the two-tailed p-value divided by 2.")
        else:
            p_val = round(two_tailed_p_val, 3)
            print(
                "We use the two-tailed p-value directly since there's no clear direction in the alternative hypothesis.")

        return round(t_stat, 2), p_val, round(levene_stat, 2), round(levene_p, 3)

    @staticmethod
    def execute_test():
        # Collecting user inputs for data
        group1_data_input = input("Enter your data samples for Group 1 separated by commas (e.g., 7,5,8): ").split(',')
        group2_data_input = input("Enter your data samples for Group 2 separated by commas (e.g., 6,7,5): ").split(',')
        group1_data = np.array([float(sample) for sample in group1_data_input])
        group2_data = np.array([float(sample) for sample in group2_data_input])

        # Input and validation for hypotheses
        while True:
            Ha = input("Enter the alternative hypothesis 'Ha' (e.g., M1<M2): ")
            Ho = input("Enter the null hypothesis 'Ho' (e.g., M1>=M2): ")

            valid_Ho = (Ho[0:2].upper() == "M1" and (Ho[2:4] in ["<=", ">="] or Ho[2] in ["="]))
            valid_Ha = (Ha[0:2].upper() == "M1" and (Ha[2] in ["<", ">"] or Ha[2:4] in ["/="]))

            if valid_Ho and valid_Ha:
                break
            else:
                print("Please ensure that both hypotheses are entered correctly.")

        alpha = StatUtils.get_alpha()

        # Calculating t-statistic, p-value, Levene's statistic and p-value
        t_statistic, p_value, levene_stat, levene_p = IndependentTest.independent_t_test(group1_data, group2_data, Ha,
                                                                                         alpha)

        # Draw conclusion based on p-value and alpha

        print("Group 1 Mean:", round(np.mean(group1_data), 2))
        print("Group 2 Mean:", round(np.mean(group2_data), 2))
        print("Mean difference :", round(np.mean(group1_data) - np.mean(group2_data), 2))
        print(f"Levene's Statistic: {levene_stat: .2f}")
        print(f"Levene's P-Value: {levene_p: .3f}")
        print(f"T-Statistic: {t_statistic: .2f}")
        print(f"P-Value: {p_value: .3f}")
        conclusion = StatUtils.check_p_value(p_value, alpha, Ho, Ha)
        print(conclusion)
