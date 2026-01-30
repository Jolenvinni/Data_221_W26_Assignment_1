'''
Question 1

Write a Python program that multiplies consecutive integers starting from 1 until the product first
becomes greater than a given threshold value.

Your program should:
• Store the threshold value in a variable.
• Keep track of the current multiplier.
• Print the final product and the integer that caused the product to exceed the threshold.

'''

threshold = 100
product = 1
currentNumber = 1

#Factorial that exceeds the threshold.
while product <= threshold:

    currentNumber += 1
    product *= currentNumber

#Output.
print(f"Final product: {product}, Current multiplier: {currentNumber}")




