'''
For this task, there are a lot of 'input' calls that are conditional on a response. i.e. only accept 'investment' or 'bond'.
So I wrote a function called 'ask_input' to make this easier.

This function takes an optional list argument for strings or a number range to accept,
It will loop with an appropriate error message until the user inputs a valid response.
The function will then return either the index of the word entered in the list (as int), or a number in range as a float.
'''

import math

#------------------------
def ask_input(ask_str, is_str=False, valid_list=[1, 10**10]):
    while True:
        test_input = input(ask_str).lower()
        try:
            if is_str:
                if not test_input in valid_list: raise Exception("not_in_list")
                test_input = valid_list.index(test_input)
            else:
                test_input = float(test_input) # will raise a ValueError if not a number.
                if test_input < valid_list[0] or test_input > valid_list[1]: raise Exception("out_range")
            return test_input # checks passed. return.
        except Exception as err:
            if str(err) == "not_in_list": print(f"Input '{test_input}' is not a valid entry. Try again.")
            elif str(err) == "out_range": print(f"Number needs to be between {valid_list[0]} and {valid_list[1]}. Try again.")
            else: print(f"Input '{test_input}' Is not a valid number. Try again.") # ValueError from 'float()'
            print() # blank line.
#------------------------

# lambda function to string format a number to pound.
pound = lambda x: "£{:.2f}".format(x)

print('''Welcome To Finance Calculator.

investment - to calculate the amount of interest you'll earn on your investment.)
bond       - to calculate the amount of you'll have to pay on a home loan.\n''')

# call the 'ask_input' function. This only returns if user enters 'investment' or 'bond'.
to_do = ask_input("Enter either 'investment' or 'bond' from the menu above to proceed: ",
                  True, ["investment", "bond"])

if to_do == 0: # 'investment' selected.
    deposit = ask_input("What is the amount of money your depositing? : ")
    interest_per = ask_input("What is the interest rate? : ")
    invest_years = ask_input("How many years are you investing? : ")
    interest = ask_input("What is the interest type ('simple' or 'compound')? : ",
                        True, ["simple", "compound"])

    interest_per /= 100 # divide by 100. in common with both simple and compound.
    if interest == 0: # simple interest.
        amount_with_interest = deposit * (1+interest_per*invest_years) # provided formula.
    else: # has to be compound.
        amount_with_interest = deposit * math.pow((1+interest_per), invest_years) # provided formula.
    print("\n * Your total amount with interest is: {}!".format(pound(amount_with_interest))) # print final answer.
    
else: # must be 'bond' as only 2 choices were presented.
    house_value = ask_input("What is the present value of the house? : ")
    interest_rate = ask_input("What is the interest rate? : ")
    repay_months = ask_input("What is the number of months you plan to repay the bond? : ")
    # being sure to divide by 100 first.
    interest_rate = (interest_rate/100) / 12
    repay_amount = (interest_rate*house_value) / (1 - (1+interest_rate) ** (-repay_months)) # provided formula.
    print("\n * You will have to repay (per month): {}!".format(pound(repay_amount)))
    
print("\nDone.")

