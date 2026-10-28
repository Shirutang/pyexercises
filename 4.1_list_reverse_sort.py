"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The same eight marketing campaign budgets used in exercise 4.0.
# 2. Process:Display the original, reversed, ascending, and descending orders.
# 3. Out:Four arrangements of the budgets, followed by the unchanged original list.
# 4. My four orders, and which ones modify the original:Original, reversed, ascending, and descending.



# Your code below

# Store the same campaign budgets as in exercise 4.0.
budgets = [500, 300, 800, 200, 600, 400, 700, 100]

# Display the budgets in their original order.
print("Original order:", budgets)

# Create a reversed copy without changing the original list.
reversed_budgets = budgets[::-1]
print("Reversed order:", reversed_budgets)

# Create an ascending copy without changing the original list.
ascending_budgets = sorted(budgets)
print("Ascending order:", ascending_budgets)

# Create a descending copy without changing the original list.
descending_budgets = sorted(budgets, reverse=True)
print("Descending order:", descending_budgets)

# Display the original list again to check that its order is unchanged.
print("Original list at the end:", budgets)
