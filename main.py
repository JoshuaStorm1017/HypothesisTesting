from OneSampleT import OneSampleTTest
from OneProportionT import OneProportionChi2Test
from DependentT import DependentTest
from IndependentT import IndependentTest
from VarianceT import VarianceTest

valid_tests = ["one sample test", "one proportion test", "dependent test", "independent test", "variance test"]

while True:
    user_test = input('What test would you like to perform? (One Sample Test, One Proportion Test, \n'
                      'Dependent Test, Independent Test, Variance Test): ')
    if user_test.lower() in valid_tests:  # Convert the user input to lowercase before checking
        break  # exit the loop if the user entered a valid test
    else:
        print("Invalid test type. Please enter a valid test.")

# Convert back to original case for execution
if user_test.lower() == "one sample test":
    OneSampleTTest.execute_test()
elif user_test.lower() == "one proportion test":
    OneProportionChi2Test.execute_test()
elif user_test.lower() == "dependent test":
    DependentTest.execute_test()
elif user_test.lower() == "independent test":
    IndependentTest.execute_test()
elif user_test.lower() == "variance test":
    VarianceTest.execute_test()


