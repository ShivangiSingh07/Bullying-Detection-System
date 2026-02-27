# code5_while_loop.py
# Topic: While Loop in Python
# A while loop is used when we want to repeat a task until a condition becomes false.

# -------------------------------
# Example 1: Counting from 1 to 5
count = 1
while count <= 5:   # loop runs as long as count is less than or equal to 5
    print("Iteration:", count)
    count += 1      # increase count by 1 each time

# -------------------------------
# Example 2: Asking user until correct input
# This loop will keep asking until the user types "yes"
answer = ""
while answer.lower() != "yes":
    answer = input("Type 'yes' to continue: ")
print("You typed yes, loop ended!")

# -------------------------------
# Example 3: Using break to stop early
num = 1
while num <= 10:
    if num == 5:
        print("Breaking at", num)
        break       # exit loop completely
    print("Number:", num)
    num += 1

# -------------------------------
# Example 4: Using continue to skip one iteration
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue    # skip printing number 5
    print("Number:", num)

# Practice ideas:
# - Try making a loop that prints numbers from 10 down to 1.
# - Create a guessing game where the loop continues until the user guesses the right number.

