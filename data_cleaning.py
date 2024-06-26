# Perform simple data cleaning tasks such as handling missing values and removing duplicates.

import pandas as pd

# Read the CSV file
df = pd.read_csv(input("Enter the path of the CSV file: "))
print(df)

# Display the first 5 rows of the data frame
print(df.head())

# Display the last 5 rows of the data frame
print(df.tail())

# handle missing values

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Display the cleaned data frame
print(df_cleaned)

# Remove duplicates
df_no_duplicates = df_cleaned.drop_duplicates()

# Display the data frame without duplicates
print(df_no_duplicates)

# Display the shape of the data frame
print(df_no_duplicates.shape)

# Display the columns of the data frame
print(df_no_duplicates.columns)

# Display the data types of the columns
print(df_no_duplicates.dtypes)

# Display the summary statistics of the data frame
print(df_no_duplicates.describe())

# Save the cleaned data frame to a new CSV file
df_no_duplicates.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved to cleaned_data.csv")
