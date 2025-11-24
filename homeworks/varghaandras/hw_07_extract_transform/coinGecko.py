import pandas as pd
import requests
import os

# Set the output path
output_path = "/Users/i0287148/Library/CloudStorage/OneDrive-Sanofi/Documents/GitHub/python_hu3/homeworks/varghaandras/hw_07_extract_transform/"

# Check the directory exists
os.makedirs(output_path, exist_ok=True)

# STEP 1: Get data from CoinGecko API xxx
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# STEP 2: Missing values per column
missing_values = df.isnull().sum()

# STEP 3: Total market cap
total_market_cap = df['market_cap'].sum()

# STEP 4: Create top50_df by current_price
top50_df = df.sort_values(by='current_price', ascending=False).head(50)

# Sort by price_change_percentage_24h descending
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)

# Add change_direction column
def change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(change_direction)

# STEP 5: Export files to specified path
top50_file = os.path.join(output_path, "top50_crypto.csv")
report_file = os.path.join(output_path, "report.csv")

# Save top50_df
top50_df.to_csv(top50_file, index=False)

# Prepare report DataFrame
report_df = pd.DataFrame({
    'Metric': list(missing_values.index) + ['Total Market Cap'],
    'Value': list(missing_values.values) + [total_market_cap]
})

# Save report
report_df.to_csv(report_file, index=False)

print(f"Files saved to:\n{top50_file}\n{report_file}")

