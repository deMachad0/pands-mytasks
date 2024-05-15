# Create a data from with data in 
# and print out the DataFrame
# and use head to print just 3 rows
# Author: Andre Machado

import pandas as pd

dictionary_data = {
    "Name": ["John" , "Mary", "Mark", "Mary", "Kate"],
    "Subject": ["math", "Programming", "SIEM", "Math", "Programming"],
    "Grade":[23.0, 66.0, 45.0, 33.9, 25]
}
df = pd.DataFrame(dictionary_data)
# printing 3 rows 
print(df.head(3))
# using decribe function
print(df.describe())
# using type function to see that outputs dataframe
print(type(df))

#Write this dataframe to a csv file grades2.csv
path = '../week10-pandas/'
filenameForGrades = path + 'grades2.csv'
df.to_csv(filenameForGrades)

#Write this dataframe to a excel file called grades2.xlsx
# Without the index
path = '../week10-pandas/'
excelFilenameForGrades = path + 'grades2.xlsx'
df.to_excel(excelFilenameForGrades, index=False, sheet_name='data')

# Add the prescription to another sheet calles 'summary'
with pd.ExcelWriter()