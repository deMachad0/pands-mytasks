#Analysing grades.csv

import pandas as pd
import matplotlib.pyplot as plt

path = '../week10-pandas/'
filenameForGrades = path + 'grades.csv'

df = pd.read_csv(filenameForGrades)
# remove from the file(grades.csv) values that are missing
df.dropna(inplace=True)
# remove the duplicate values from the list
df.drop_duplicates(inplace=True)

df = df.pivot_table(values='grade',index=['name','subject'],aggfunc='max').reset_index()
print(df)

# getting the average
# meanValues = df.groupby('subject').mean()
# another way to get the mean values
meanValues = df.groupby('subject').describe()
print(meanValues)

# Using pivot to rename index, columns and values in the graphic
df = df.pivot(index='name', columns='subject', values='grade')
# transforming csv file into a graphic using plot and bar() = option
df.plot.bar()
plt.show()