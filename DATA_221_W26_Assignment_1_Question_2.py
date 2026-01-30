'''
Question 2
Define a function that receives a list of strings and returns a dictionary with the following structure:

• Each key is a string from the list.

• Each value is another dictionary containing:
    – The length of the string
    – Whether the length is even or odd

'''


def parity_list_of_strings(list_of_strings):

    dictionary_of_the_strings = {}

    for string in list_of_strings:

        dictionary_of_the_strings[string] = {
            "length": len(string),
            "parity": "even" if len(string) % 2 == 0 else "odd"
        }

    return dictionary_of_the_strings

print(parity_list_of_strings(["data","science"]))

