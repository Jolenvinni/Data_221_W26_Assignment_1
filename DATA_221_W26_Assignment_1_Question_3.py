'''
Question 3

Define a function that computes xy. Then, given a list of pairs (x, y):
• Use a for loop with argument unpacking to call the function.
• Skip any pair where the exponent y is negative.
• Store the valid results in a list and print the list.

'''

def list_of_x_to_the_power_of_y(nums):

    list_of_results = []

    for x, y in nums:

        if y < 0:
            continue
        result = x ** y
        list_of_results.append(result)

    return list_of_results

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

print(list_of_x_to_the_power_of_y(pairs))
