#Logan H's Budget Analysis

# 1st, I get a number of money someone has in a float
funds = float(input("Enter how much you have: "))

# 2nd, then I keep track of their budget, starting at 0
budget = 0

# 3rd, I start of loop, asking what needs to be budgeted and how much it is.
loop_budget = True

while loop_budget == True:
    question = input("What needs to be budgeted? ")
    number = float(input("How much will that cost you? "))
    budget += number

# 4th, the loop ends if the state is changed to false which is changed when there is nothing else
    answer = input("Do you have anything else that need's to be budgeted? (Y/N) ")
    if answer == "Y":
        loop_budget = True

    else:
        loop_budget = False

# 5th, I find the total left, display all the info and tell them if they are positive or negative.
total_left = funds - budget

print("Alright, your total funds are $", funds, ",")
print("you need to $", budget, " to survive ,")
print("and you are left with $", total_left, ".")

if total_left >= 0:
    print("Congrats, you will survive.")
else:
    print("You are going negative, better take out a loan.")
