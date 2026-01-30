'''
Question 3

Define a function that computes xy. Then, given a list of pairs (x, y):
• Use a for loop with argument unpacking to call the function.
• Skip any pair where the exponent y is negative.
• Store the valid results in a list and print the list.

'''

def list_of_x_to_the_power_of_y(nums):

    list_of_results = []

    #Goes through and takes x,y from the list.
    for x, y in nums:

        #Skips the current item:
        if y < 0:
            continue

        #Applies x to the power of y if otherwise.
        result = x ** y
        list_of_results.append(result)

    return list_of_results

#Output.
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

print(list_of_x_to_the_power_of_y(pairs))
