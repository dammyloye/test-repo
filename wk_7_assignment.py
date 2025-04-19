#Task 1

# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Map species to their names
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check the structure of the dataset
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Since there are no missing values, we don't need to clean the dataset
print("\nNo missing values found. Dataset is clean.")


#Task 2

# Compute basic statistics
print("Basic statistics:")
print(df.describe())

# Group by species and compute mean
grouped_df = df.groupby('species')[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].mean()

print("\nMean of each feature by species:")
print(grouped_df)


#Task 3

import matplotlib.pyplot as plt

# Bar chart
plt.figure(figsize=(8, 6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(df['sepal length (cm)'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
for species in df['species'].unique():
    species_df = df[df['species'] == species]
    plt.scatter(species_df['sepal length (cm)'], species_df['petal length (cm)'], label=species)

plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Line chart (simulating time series)
df['cumulative_sepal_length'] = df['sepal length (cm)'].cumsum()
plt.figure(figsize=(8, 6))
plt.plot(df['cumulative_sepal_length'], marker='o')
plt.title('Cumulative Sepal Length Over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Cumulative Sepal Length (cm)')
plt.show()