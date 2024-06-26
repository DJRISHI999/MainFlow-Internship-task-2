# Practice basic data manipulation operations like filtering, sorting, and grouping data.

# Importing the required libraries
import pandas as pd

# Load the data
data = pd.read_csv(input("Enter the path of the file: "))

# manipulate the data
# Fetch the name of columns

print(data.columns)

# Manipulate the data
# Filter the data
column_name = input("Enter the column name: ")
column_value = int(input("Enter the column value: "))

filtered_data = data[data[column_name] == column_value]

print(filtered_data)

# Sort the data
column_name = input("Enter the column name: ")
sorted_data = data.sort_values(by=column_name, ascending=True)

print(sorted_data)

# Group the data
column_name = input("Enter the column name: ")
grouped_data = data.groupby(column_name).size().reset_index(name='Count')

print(grouped_data)

