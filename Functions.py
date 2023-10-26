class StatUtils:

    @staticmethod
    def check_p_value(p_value, alpha, Ho, Ha):
        if p_value > alpha:
            conclusion = Ho
            return f"Since the P-Value is greater than alpha\nConclusion: {conclusion}"
        else:
            conclusion = Ha
            return f"Since the P-Value is less than or equal to alpha\nConclusion: {conclusion}"

    @staticmethod
    def get_alpha():
        alpha = float(input("Enter the alpha from the research question (e.g., 0.05 or 0.01): "))
        return alpha
