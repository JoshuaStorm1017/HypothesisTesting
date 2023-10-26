from scipy import stats
import numpy as np
from Functions import StatUtils


class VarianceTest:

    @staticmethod
    # Function for testing homogeneity of variances
    def test_variances(group1, group2, Ha):
        # Levene's test for equality of variances
        levene_stat, levene_p = stats.levene(group1, group2, center='mean')

        # Derive one-tailed p-value based on Ha and standard deviations
        std1 = np.std(group1, ddof=1)
        std2 = np.std(group2, ddof=1)

        if Ha[2] == ">":
            if std1 > std2:
                p_val = round(levene_p, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests that variance of group 1 is greater and the standard deviation of group 1 is greater, we divide the p-value by 2.")
            else:
                p_val = 1 - (round(levene_p, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests that variance of group 1 is greater but the standard deviation of group 1 is lesser, we use 1 minus the p-value divided by 2.")
        elif Ha[2] == "<":
            if std1 < std2:
                p_val = round(levene_p, 3) / 2
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests that variance of group 1 is less and the standard deviation of group 1 is lesser, we divide the p-value by 2.")
            else:
                p_val = 1 - (round(levene_p, 3) / 2)
                p_val = round(p_val + 0.0001, 3)
                print(
                    "Since the alternative hypothesis suggests that variance of group 1 is lesser but the standard deviation of group 1 is greater, we use 1 minus the p-value divided by 2.")
        else:
            p_val = round(levene_p, 3)
            print(
                "We use the two-tailed p-value directly since there's no clear direction in the alternative hypothesis.")

        return round(levene_stat, 2), p_val, round(levene_p, 3)

    @staticmethod
    def execute_test():
        # Collecting user inputs for data
        group1_data_input = input("Enter your data samples for Group 1 separated by commas (e.g., 7,5,8): ").split(',')
        group2_data_input = input("Enter your data samples for Group 2 separated by commas (e.g., 6,7,5): ").split(',')
        group1_data = np.array([float(sample) for sample in group1_data_input])
        group2_data = np.array([float(sample) for sample in group2_data_input])

        # Input and validation for hypotheses
        while True:
            Ha = input("Enter the alternative hypothesis 'Ha' (e.g., S1>S2): ")
            Ho = input("Enter the null hypothesis 'Ho' (e.g., S1<=S2): ")

            valid_Ha = (Ha[0:2].upper() == "S1" and (Ha[2] in ["<", ">"] or Ha[2:4] in ["/="]))
            valid_Ho = (Ho[0:2].upper() == "S1" and (Ho[2:4] in ["<=", ">="] or Ho[2] in ["="]))

            if valid_Ha and valid_Ho:
                break
            else:
                print("Please ensure that both hypotheses are entered correctly.")

        alpha = StatUtils.get_alpha()

        # Calculating Levene's statistic and p-value
        levene_stat, p_value, levene_p = VarianceTest.test_variances(group1_data, group2_data, Ha)

        # Draw conclusion based on p-value and alpha
        n1 = len(group1_data)
        n2 = len(group2_data)
        total_n = n1 + n2

        print("Group 1 N: ", n1)
        print("Group 1 Mean: ", round(np.mean(group1_data), 2))
        print("Group 1 Std:", round(np.std(group1_data, ddof=1), 2))
        print("Group 2 N: ", n2)
        print("Group 2 Mean: ", round(np.mean(group2_data), 2))
        print("Group 2 Std:", round(np.std(group2_data, ddof=1), 2))
        print("Combined Mean: ", round(((np.sum(group1_data) + np.sum(group2_data)) / total_n), 2))
        print(f"Levene's Statistic: {levene_stat: .2f}")
        print(f"Levene P-Value : {levene_p}")
        print(f"P-Value: {p_value}")
        conclusion = StatUtils.check_p_value(p_value, alpha, Ho, Ha)
        print(conclusion)
