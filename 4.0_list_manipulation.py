"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight marketing campaign budgets in euros.
# 2. Process: Select the first budget, sort the budgets, and calculate the total.
# 3. Out: The whole list, the first budget, the sorted list, and the total budget.
# 4. What my list is about, and what I computed from it: Marketing campaign budgets. I calculate the total to understand the overall spending.


# Your code below
# Store the budgets for eight marketing campaigns in euros.
budgets = [500, 300, 800, 200, 600, 400, 700, 100]

# Display all the campaign budgets.
print("All budgets:", budgets)

# Display the first campaign budget.
print("First budget:", budgets[0])

# Display the budgets from smallest to largest.
print("Sorted budgets:", sorted(budgets))

# Add all the campaign budgets and display the total.
total_budget = sum(budgets)
print("Total budget in euros:", total_budget)

# Check the first three budgets against the hand-calculated total of 1600.
print("Test total:", sum(budgets[:3]))

# Test result: The first three budgets total 1600 by hand and in the program. Passed.