# Learn how to read CSV files and manipulate data frames using Pandas.

import pandas as pd

# Read the CSV file
df = pd.read_csv(input("Enter the path of the CSV file: "))
print(df)

# Display the first 5 rows of the data frame
print(df.head())

# Display the last 5 rows of the data frame
print(df.tail())

# Display the shape of the data frame
print(df.shape)

# Display the columns of the data frame
print(df.columns)

# Display the data types of the columns
print(df.dtypes)

# Display the summary statistics of the data frame
print(df.describe())


 