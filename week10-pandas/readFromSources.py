# reading in dictionary objects
# the attribute names will be column names
# the index is automatically made

import pandas as pd

dataAsDictOfList = {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. Wiiliam Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]
}
df = pd.DataFrame(dataAsDictOfList)
# change the index
# df = pd.DataFrame(dataAsDictOfList, index=["a","b","c"])

print(df)
# analysis of the written data
# print(df.describe())

# or with just lists
dataAsLists = [[1, 2, 100, "male"],
               [2, 4, 100, "male"],
               [3, 8, 100, "female"]]

df = pd.DataFrame(dataAsLists)
# adding colums
df = pd.DataFrame(dataAsLists, columns=["x", "y", "percent", "sex"])

print(df)