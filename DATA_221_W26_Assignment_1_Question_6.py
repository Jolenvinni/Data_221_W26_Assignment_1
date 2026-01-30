'''
Question 6

Define a function that receives a list of numbers and returns a dictionary where:
• Each key is a unique value from the list.
• Each value is the percentage of elements in the list that are less than or equal to that key.
The resulting dictionary should be sorted by key before being returned.

'''



def convert_list_of_numbers_to_dictionary(list_of_numbers):

    dictionary_of_numbers = {}

    for current_item in list_of_numbers:
        count_of_similar_items = 0
        for compared_item in list_of_numbers:

            if compared_item <= current_item:
                count_of_similar_items += 100 / len(list_of_numbers)
                dictionary_of_numbers[current_item] = f"{round(count_of_similar_items, 2)}%"

    return dict(sorted(dictionary_of_numbers.items()))

numbers = [3, 1, 2, 3, 4, 2]

print(convert_list_of_numbers_to_dictionary(numbers))