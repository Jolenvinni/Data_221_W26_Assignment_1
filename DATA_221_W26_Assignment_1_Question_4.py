'''
Question 4

Given a list of random values between 0 and 1 and a random value x:
• Sort the list.
• Find all indices where the list value is greater than or equal to x.
• Print the sorted list, the value of x, and the first matching index (if one exists)

'''

#Given code.
from random import random

values = [random() for i in range(20)]
x = random()


values.sort()

#First part of the output.
print(f"Sorted list: {values}")
print(f"x = {x}")

#The rest of the output.
#Goes through the indices of the list -
for index in range(len(values)):

    # - until the condition is met -
    if values[index] >= x:
        print(f"First matching index: {index}")
        break

# or until it finishes the list.
else:
    print("No matching index found.")


