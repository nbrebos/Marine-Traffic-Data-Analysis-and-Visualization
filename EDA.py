import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Data
csv_file_path = 'vessel_data.csv'
df = pd.read_csv(csv_file_path)
# Initial Data Exploration
print("First Few Rows of the Dataset:")
# Print all columns
pd.set_option('display.max_columns', None)
head = df.head()
plt.figure(figsize=(10, 6))
plt.text(0.1, 0.9, str(head), fontsize=12)
plt.axis('off')
plt.savefig('head.png', bbox_inches='tight', pad_inches=0.1)
print("\n")
# Step 3: Data Information
info = df.info()
print("\nData Information:")
print(info)
plt.figure(figsize=(10, 6))
plt.text(0.1, 0.9, str(info), fontsize=12)
plt.axis('off')
plt.savefig('info.png', bbox_inches='tight', pad_inches=0.1)
print("Basic Statistics of Numerical Columns:")
print(df.describe())
plt.figure(figsize=(10, 6))
plt.text(0.1, 0.9, str(df.describe()), fontsize=12)
plt.axis('off')
plt.savefig('describe.png', bbox_inches='tight', pad_inches=0.1)
print("\n")
# Data Cleaning
print("Missing Values in the Dataset:")
print(df.isnull().sum())
plt.figure(figsize=(10, 6))
plt.text(0.1, 0.9, str(df.isnull().sum()), fontsize=12)
plt.axis('off')
plt.savefig('missing_values.png', bbox_inches='tight', pad_inches=0.1)
print("\n")
print("Number of Duplicate Rows:")
print(df.duplicated().sum())
plt.figure(figsize=(10, 6))
plt.text(0.1, 0.9, str(df.duplicated().sum()), fontsize=12)
plt.axis('off')
plt.savefig('duplicate_rows.png', bbox_inches='tight', pad_inches=0.1)
print("\n")

# Find rows with missing or zero values
rows_with_missing_or_zero = (df == 0) | df.isna()
# Iterate through the DataFrame to print rows and columns with missing or zero values
for index, row in rows_with_missing_or_zero.iterrows():
    for column, has_issue in row.iteritems():
        if has_issue:
            print(f"Row {index}, Column {column} has missing or zero value: {df.at[index, column]}")

#Preprocessing#
# fix types of columns
print(df.dtypes)
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Speed'] = df['Speed'].astype(float)
df['Speed'] = df['Speed'].fillna(0.0)
df['Built'] = df['Built'].fillna(0).astype(int)
df['Built'] = df['Built'].astype(int)
df['Capacity - Gt'] = df['Capacity - Gt'].fillna(0).astype(int)
df['Capacity - Gt'] = df['Capacity - Gt'].astype(int)
#split the string and get the right string next to "-"
df['Global Area']=df['Global Area'].str.split("-").str[1].str.strip()

# Get the list of categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
# Loop through the categorical columns and print unique values and their counts
for column in categorical_columns:
    print(f"Column: {column}")
    unique_values = df[column].value_counts()
    print(unique_values)
    print("\n")

#NON- numerical columns
plt.figure(figsize=(12, 12))
df['Vessel Type - Generic'].value_counts().plot(kind='pie', autopct='', labels= None, labeldistance=1.1).set_ylabel('')  # Remove the default ylabel
plt.title('Frequency of Vessel Type')
plt.xlabel('Vessel Type - Generic')
# Create a custom legend
custom_legend = [
    f'{label} ({percentage:.1f}%)'
    for label, percentage in zip(df['Vessel Type - Generic'].value_counts().index, df['Vessel Type - Generic'].value_counts(normalize=True) * 100)
]
# Place the legend in the upper left corner
plt.legend(custom_legend, loc='upper right')
plt.title('Frequency of Vessel Type')
plt.savefig('Frequency of Vessel Type pie chart.png')
plt.show()


# Create a horizontal bar chart for a categorical column
plt.figure(figsize=(12, 8))
df['Global Area'].value_counts().plot(kind='barh')
plt.title('Distribution of Global Area')
plt.xlabel('Count')
plt.ylabel('Global Area')
plt.savefig('Distribution of Global Area.png')
plt.show()


# Select only the numerical columns
numerical_cols = df.select_dtypes(include=['number'])
# Create scatter plots using Seaborn's pairplot
sns.pairplot(numerical_cols)
# Save the plot to an image file
plt.savefig('scatter_plots.png')
plt.show()

# Calculate the average year built by ship class
average_year_built_by_class = df.groupby('Vessel Type - Generic')['Built'].mean()
# Create a line plot
plt.figure(figsize=(12, 6))
average_year_built_by_class.plot(kind='line', marker='o', linestyle='-')
plt.title('Average Year Built by Ship Class')
plt.xlabel('Ship Class')
plt.ylabel('Average Year Built')
plt.grid(True)  # Add a grid for reference
plt.savefig('Average_Year_Built_by_Ship_Class_Line_Plot.png')
plt.show()

# Step 7: Correlation Analysis (Example: Correlation matrix)
correlation_matrix = df[df['Speed'] != 0.0].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)
# Create a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file
plt.show()



# Create a count plot to show the relationship between two categorical columns
#plt.figure(figsize=(12, 12))
#sns.countplot(data=df, x='Vessel Type - Generic', hue='Owner Country').legend(title='Owner Country', bbox_to_anchor=(1.05, 1), loc='upper right')
#plt.title('Vessel Type (Generic) Distribution by Owner Country')
#plt.xlabel('Category')
#plt.ylabel('Count')
#plt.savefig('Vessel Type (Generic) Distribution by Owner Country.png')



# Create a scatter plot for two numerical variables (e.g., 'Speed' vs. 'Gross Tonnage')
#plt.scatter(df['Speed'], df['Capacity - Gt'], c='blue', alpha=0.5)
#plt.xlabel('Speed')
#plt.ylabel('Capacity - Gt')
#plt.title('Scatter Plot: Speed vs. Capacity - Gt')
#plt.show()
