import json
from datetime import datetime, timedelta
import numpy as np
import os
import matplotlib.pyplot as plt

# Construct the path to the JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_directory, '..', 'data', 'EQ_UI_prices_download.json')

try:
    with open(data_file_path, 'r') as f:
        stock_data = json.load(f)
    print("Stock data loaded successfully from:", data_file_path)  # Confirmation message
except FileNotFoundError:
    print(f"Error: Stock data file not found at: {data_file_path}")
    stock_data = []  # Or handle the error as appropriate, e.g., exit the script
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from file: {data_file_path}")
    stock_data = [] # Or handle the error as appropriate
except Exception as e:
    print(f"An unexpected error occurred while loading stock data: {e}")
    stock_data = []


revenue_data = {
    "Q1 2011": 34.1, "Q2 2011": 45.1, "Q3 2011": 51.2, "Q4 2011": 67.6,
    "Q1 2012": 79.2, "Q2 2012": 87.8, "Q3 2012": 91.7, "Q4 2012": 94.9,
    "Q1 2013": 61.5, "Q2 2013": 74.9, "Q3 2013": 83.2, "Q4 2013": 101.2,
    "Q1 2014": 129.7, "Q2 2014": 138.4, "Q3 2014": 148.3, "Q4 2014": 156.0,
    "Q1 2015": 150.1, "Q2 2015": 153.1, "Q3 2015": 147.5, "Q4 2015": 145.3,
    "Q1 2016": 151.4, "Q2 2016": 161.9, "Q3 2016": 167.4, "Q4 2016": 185.7,
    "Q1 2017": 204.8, "Q2 2017": 213.5, "Q3 2017": 218.4, "Q4 2017": 228.6,
    "Q1 2018": 245.9, "Q2 2018": 250.8, "Q3 2018": 250.4, "Q4 2018": 269.8,
    "Q1 2019": 282.9, "Q2 2019": 307.3, "Q3 2019": 284.9, "Q4 2019": 286.6,
    "Q1 2020": 323.3, "Q2 2020": 308.3, "Q3 2020": 337.4, "Q4 2020": 315.5,
    "Q1 2021": 473.5, "Q2 2021": 479.4, "Q3 2021": 467.2, "Q4 2021": 477.9,
    "Q1 2022": 458.9, "Q2 2022": 431.6, "Q3 2022": 358.1, "Q4 2022": 443.1,
    "Q1 2023": 498.1, "Q2 2023": 493.6, "Q3 2023": 457.8, "Q4 2023": 491.1,
    "Q1 2024": 463.1, "Q2 2024": 465.0, "Q3 2024": 493.0, "Q4 2024": 507.5,
    "Q1 2025": 550.3, "Q2 2025": 599.9
}

# Report Dates
report_dates = {
    "Q1 2012": datetime(2011, 11, 10),
    "Q2 2012": datetime(2012, 1, 31),
    "Q3 2012": datetime(2012, 5, 1),
    "Q4 2012": datetime(2012, 8, 9),
    "Q1 2013": datetime(2012, 11, 8),
    "Q2 2013": datetime(2013, 2, 7),
    "Q3 2013": datetime(2013, 5, 9),
    "Q4 2013": datetime(2013, 8, 8),
    "Q1 2014": datetime(2013, 11, 7),
    "Q2 2014": datetime(2014, 2, 6),
    "Q3 2014": datetime(2014, 5, 8),
    "Q4 2014": datetime(2014, 8, 7),
    "Q1 2015": datetime(2014, 11, 6),
    "Q2 2015": datetime(2015, 2, 5),
    "Q3 2015": datetime(2015, 5, 7),
    "Q4 2015": datetime(2015, 8, 6),
    "Q1 2016": datetime(2015, 11, 5),
    "Q2 2016": datetime(2016, 2, 4),
    "Q3 2016": datetime(2016, 5, 5),
    "Q4 2016": datetime(2016, 8, 4),
    "Q1 2017": datetime(2016, 11, 3),
    "Q2 2017": datetime(2017, 2, 9),
    "Q3 2017": datetime(2017, 5, 4),
    "Q4 2017": datetime(2017, 8, 3),
    "Q1 2018": datetime(2017, 11, 9),
    "Q2 2018": datetime(2018, 2, 8),
    "Q3 2018": datetime(2018, 5, 10),
    "Q4 2018": datetime(2018, 8, 24),
    "Q1 2019": datetime(2018, 11, 9),
    "Q2 2019": datetime(2019, 2, 8),
    "Q3 2019": datetime(2019, 5, 10),
    "Q4 2019": datetime(2019, 8, 9),
    "Q1 2020": datetime(2019, 11, 8),
    "Q2 2020": datetime(2020, 2, 7),
    "Q3 2020": datetime(2020, 5, 8),
    "Q4 2020": datetime(2020, 8, 21),
    "Q1 2021": datetime(2020, 11, 6),
    "Q2 2021": datetime(2021, 2, 5),
    "Q3 2021": datetime(2021, 5, 7),
    "Q4 2021": datetime(2021, 8, 27),
    "Q1 2022": datetime(2021, 11, 5),
    "Q2 2022": datetime(2022, 2, 4),
    "Q3 2022": datetime(2022, 5, 6),
    "Q4 2022": datetime(2022, 8, 26),
    "Q1 2023": datetime(2022, 11, 4),
    "Q2 2023": datetime(2023, 2, 3),
    "Q3 2023": datetime(2023, 5, 5),
    "Q4 2023": datetime(2023, 8, 25),
    "Q1 2024": datetime(2023, 11, 3),
    "Q2 2024": datetime(2024, 2, 9),
    "Q3 2024": datetime(2024, 5, 10),
    "Q4 2024": datetime(2024, 8, 23),
    "Q1 2025": datetime(2024, 11, 8),
    "Q2 2025": datetime(2025, 2, 7)
}

quarterly_prices = {}

for quarter_year, revenue in revenue_data.items():
    report_date = report_dates.get(quarter_year)
    if not report_date:
        print(f"Warning: No report date found for {quarter_year}. Skipping.")
        quarterly_prices[quarter_year] = None
        continue

    # Define the window: 3 months prior to report date
    start_date = report_date - timedelta(days=90)
    end_date = report_date #Report date
    #print (f"Start date {start_date} and end date {end_date} for {quarter_year}")

    quarter_prices = []
    for day_data in stock_data:
        timestamp = day_data['time']
        date = datetime.fromtimestamp(timestamp)
        if start_date <= date <= end_date:
            quarter_prices.append(day_data['close'])

    if quarter_prices:
        quarterly_prices[quarter_year] = np.mean(quarter_prices)
    else:
        quarterly_prices[quarter_year] = None # No stock data for this quarter


# Prepare data for correlation calculation
revenue_values = []
price_values = []
valid_quarters = []

for quarter_year in revenue_data:
    if quarterly_prices[quarter_year] is not None:
        revenue_values.append(revenue_data[quarter_year])
        price_values.append(quarterly_prices[quarter_year])
        valid_quarters.append(quarter_year)

# Calculate Pearson correlation
if len(revenue_values) > 1:  # Need at least two values to calculate correlation
    correlation_coefficient = np.corrcoef(revenue_values, price_values)[0, 1]
else:
    correlation_coefficient = None
    print("Not enough data points to calculate correlation.")


print("Quarterly Revenue Data:", revenue_data)
print("\nQuarterly Average Stock Prices:", quarterly_prices)

if correlation_coefficient is not None:
    print(f"\nPearson Correlation Coefficient between Revenue and Stock Price: {correlation_coefficient:.2f}")
else:
    print("\nPearson Correlation Coefficient could not be calculated.")


n = 4  # Show every 4th label
plt.figure(figsize=(12, 6)) #increased for visibility
plt.plot(valid_quarters, revenue_values, label='Revenue (Millions)')
plt.plot(valid_quarters, price_values, label='Average Stock Price')
#plt.xlabel("Quarter")
#plt.ylabel("Value")
plt.title("Revenue vs. Average Stock Price Over Quarters")
plt.xticks(valid_quarters[::n], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
