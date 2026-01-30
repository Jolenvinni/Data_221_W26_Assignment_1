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

    #Goes through and takes the words from the list.
    for string in list_of_strings:

        dictionary_of_the_strings[string] = {

            #Counts the word length.
            "length": len(string),

            #Checks if the length is even or odd.
            "parity": "even" if len(string) % 2 == 0 else "odd"
        }

    return dictionary_of_the_strings

#Output.
print(parity_list_of_strings(["data","science"]))

