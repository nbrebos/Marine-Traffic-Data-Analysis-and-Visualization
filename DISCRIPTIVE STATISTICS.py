import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'vessels_data.csv'
df = pd.read_csv(csv_file_path)

# 1. Average Speed of Ships by Class of Ships
average_speed_by_class = df.groupby('Vessel Type - Generic')['Speed'].mean()
print("1. Average Speed of Ships by Class of Ships:")
print(average_speed_by_class)

# 2. Average Speed of Ships per Area
average_speed_per_area = df.groupby('Global Area')['Speed'].mean()
print("\n2. Average Speed of Ships per Area:")
print(average_speed_per_area)


# 3. Country with the Most Ships
most_ships_country = df['Owner Country'].value_counts().idxmax()
print("\n3. Country with the Most Ships:")
print(most_ships_country)

# 4. Ship with the Largest and Smallest Capacity
largest_capacity_ship = df[df['Capacity - Gt'] == df['Capacity - Gt'].max()]['Vessel Name'].values[0]
smallest_capacity_ship = df[df['Capacity - Gt'] == df['Capacity - Gt'].min()]['Vessel Name'].values[0]
print("\n4. Ship with the Largest Capacity:")
print(largest_capacity_ship)
print("   Ship with the Smallest Capacity:")
print(smallest_capacity_ship)

# 5. Port with the Most Traffic
most_traffic_port = df['Current Port'].append(df['Destination Port']).value_counts().idxmax()
print("\n5. Port with the Most Traffic:")
print(most_traffic_port)

# 6. Most Common Type of Ship
most_common_ship_type = df['Vessel Type - Generic'].value_counts().idxmax()
print("\n6. Most Common Type of Ship:")
print(most_common_ship_type)

most_common_ship_type = df['Vessel Type - Generic'].mode().iloc[0]
print("\n6. Most Common Type of Ship:")
print(most_common_ship_type)

# 7. Count of Ships on Open Sea and in Ports
ships_on_open_sea = len(df[df['Speed'] > 0])
ships_in_ports = len(df[df['Speed'] == 0])
print("\n7. Count of Ships on Open Sea and in Ports:")
print("   Ships on Open Sea:", ships_on_open_sea)
print("   Ships in Ports:", ships_in_ports)