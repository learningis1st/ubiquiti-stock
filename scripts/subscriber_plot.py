import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import os

# Construct the file path, assuming the script is in the 'scripts' directory
# and the data is in the 'data' directory, both within the same project folder.
data_file_path = os.path.join("..", "data", "subreddit_subscriber_count_20250311.csv")


# Load the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(data_file_path)
except FileNotFoundError:
    print(f"Error: The file '{data_file_path}' was not found.")
    exit()  # Exit the program if the file is not found


# Check if the DataFrame is empty
if df.empty:
    print("Error: The CSV file is empty.")
    exit()


# Convert 'utcDay' to datetime objects (interpreting as days since an epoch, presumably 1970-01-01)
df['utcDay'] = pd.to_datetime(df['utcDay'], unit='D', origin='1970-01-01')  # Explicitly set origin

# Check for missing or incorrect data
if df['utcDay'].isnull().any():
    print("Warning: Some dates could not be converted.  Check the 'utcDay' column for invalid values.")

if df['count'].isnull().any():
    print("Warning: Missing values in the 'count' column.  Consider filling these with 0 or using interpolation.")

plt.figure(figsize=(12, 8))  # Larger figure size

# Plot the data with a more visually appealing style
plt.plot(df['utcDay'], df['count'], color='royalblue', linewidth=2, marker='o', markersize=3)

#plt.xlabel("Date")
plt.ylabel("Members")
plt.title("r/Ubiquiti Subscriber Count Over Time", fontsize=16)

plt.grid(True, linestyle='--', alpha=0.5)  # Add a subtle grid

# Format the x-axis to show dates more clearly
date_format = mdates.DateFormatter("%Y")
plt.gca().xaxis.set_major_formatter(date_format)  # Apply the format
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator()) # Automatically space the dates

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Set the y-axis to start at 0
plt.ylim(bottom=0)

# Add a shaded area representing the data range (optional)
plt.fill_between(df['utcDay'], df['count'], color='skyblue', alpha=0.2)


# Add Annotations for important events (optional - requires knowledge of the data)
# Example:
# peak_date = df['utcDay'][df['count'].idxmax()]
# peak_count = df['count'].max()
# plt.annotate(f'Peak: {peak_count:,.0f}', xy=(peak_date, peak_count), xytext=(peak_date, peak_count + 1000),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              fontsize=10)  # Adjust xytext for good placement


plt.tight_layout()
plt.show()
