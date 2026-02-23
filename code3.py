# code3_conditions.py
# Learning decision-making with if/else
# Asking for user input
age = int(input("Enter your age: "))

# Decision-making
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Boolean example
is_student = input("Are you a student? (yes/no): ")

if is_student.lower() == "yes":
    print("Keep learning and growing!")

else:
    print("Lifelong learning is still important!")
