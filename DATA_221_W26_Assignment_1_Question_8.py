'''
Question 8

Install the pandas package and import it using the alias pd. Then:
• Create a DataFrame using the provided column data.
• Add a new column derived from existing columns.
• Print the final DataFrame.

'''

import pandas as pd

data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210],
}

#Creates dataframe.
generic_data_frame = pd.DataFrame(data)

#Creates a new column from the quotient of (column B / column A).
generic_data_frame["D"] = generic_data_frame['B'] / generic_data_frame['A']

#Output.
print(generic_data_frame)