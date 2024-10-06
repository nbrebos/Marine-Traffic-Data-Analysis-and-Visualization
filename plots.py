import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'vessels_data.csv'
df = pd.read_csv(csv_file_path)

# Κατανομή των πλοίων ανά κατηγορία και Γενική περιοχή
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Global Area')
plt.title("Κατανομή Πλοίων ανά Γενική Περιοχή")
plt.xticks(rotation=90)
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file
# Κατανομή των πλοίων ανά κατηγορία και τοπική περιοχή
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Vessel Type - Generic')
plt.title("Κατανομή Πλοίων ανά Κατηγορία")
plt.xticks(rotation=90)
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file

plt.figure(figsize=(12, 8))
sns.countplot(data=df, y='Global Area', hue='Local Area')
plt.title("Κατανομή Πλοίων ανά Γενική Περιοχή και Τοπική Περιοχή")
plt.xlabel("τοπική Περιοχή")
plt.ylabel("Γενική Περιοχή")
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file


plt.figure(figsize=(12, 8))
sns.countplot(data=df, y='Vessel Type - Generic', hue='Local Area')
plt.title("Κατανομή Πλοίων ανά Κατηγορία και Τοπική Περιοχή")
plt.xlabel("Κατηγορία")
plt.ylabel("Τοπική Περιοχή")
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file



#plt.figure(figsize=(10, 6))
#sns.scatterplot(data=df, x='Vessel Type - Generic', y='Speed', hue='Global Area')
#plt.title("Συσχέτιση Τύπου Πλοίου και Ταχύτητας")
#plt.xticks(rotation=90)
#plt.show()

# Create a scatterplot
#plt.figure(figsize=(12, 8))
#sns.scatterplot(data=df, x='Vessel Type - Generic', y='Speed', hue='Vessel Type - Generic')
# Customize the plot
#plt.title('Συσχέτιση Τύπου Πλοίου και Ταχύτητας')
#plt.xlabel('Vessel Type - Generic')
#plt.ylabel('Speed')
#plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
#plt.legend(title='Vessel Type - Generic', loc='upper right')
# Show the plot
#plt.tight_layout()
#plt.show()


filtered_df = df[df['Speed'] > 0]
mean_speed_by_type = filtered_df.groupby('Vessel Type - Generic')['Speed'].mean().reset_index()
# Create a bar chart
plt.figure(figsize=(12, 8))
sns.barplot(data=mean_speed_by_type, x='Vessel Type - Generic', y='Speed', ci=None, palette='viridis')
# Customize the plot
plt.title('Mean Speed by Ship Type')
plt.xlabel('Vessel Type - Generic')
plt.ylabel('Mean Speed')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
# Show the plot
plt.tight_layout()
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file



# Pivot the data to create a matrix of ship types by area
ship_area_pivot = df.pivot_table(index='Vessel Type - Generic', columns='Global Area', values='Vessel Name', aggfunc='count', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(ship_area_pivot, cmap='YlGnBu', annot=True, fmt='d')
plt.title("Είδη Πλοίων ανά Περιοχή")
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file


# Create a pivot table to count the occurrences of ship types in each area
pivot_table = df.pivot_table(index='Global Area', columns='Vessel Type - Generic', aggfunc='size', fill_value=0)
# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt='d', linewidths=0.5)
plt.title('Ships by Area and Ship Type')
plt.xlabel('Vessel Type - Generic')
plt.ylabel('Global Area')
plt.xticks(rotation=90)
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Built', y='Capacity - Gt')
plt.title("Σχέση Χρονολογίας Κατασκευής και Μεταφορικής Ικανότητας")
plt.show()
plt.savefig('correlation_matrix.png')  # Save the plot as a PNG file
