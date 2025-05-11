import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Config
TICKER = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2024-12-31"
MA_WINDOW = 20

# Fetch data
data = yf.download(TICKER, start=START_DATE, end=END_DATE)

# Print out the columns to debug
print("Columns after download:")
print(data.columns)

# Calculate moving average
data[('MA', TICKER)] = data[('Close', TICKER)].rolling(window=MA_WINDOW).mean()  # Multi-index for MA

# Debugging: Check if 'MA' is properly created
print("Columns after calculating 'MA':")
print(data.columns)

# Debugging: Check if the 'MA' column exists in the DataFrame
print("First few rows after calculating 'MA':")
print(data[[('Close', TICKER), ('MA', TICKER)]].head(25))

# Drop rows where 'MA' is NaN (proper reference for multi-index columns)
data = data.dropna(subset=[('MA', TICKER)])

# Generate signals (Buy when Close < MA)
data["Signal"] = (data[('Close', TICKER)] < data[('MA', TICKER)]).astype(int)

# Create position change to plot Buy and Sell signals
data["Position"] = data["Signal"].diff()

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(data[('Close', TICKER)], label="Close Price", alpha=0.5)
plt.plot(data[('MA', TICKER)], label=f"{MA_WINDOW}-day MA", linestyle="--")

# Plot Buy signals
plt.plot(data[data["Position"] == 1].index,
         data[('MA', TICKER)][data["Position"] == 1],
         "^", markersize=10, color='g', label='Buy Signal')

# Plot Sell signals
plt.plot(data[data["Position"] == -1].index,
         data[('MA', TICKER)][data["Position"] == -1],
         "v", markersize=10, color='r', label='Sell Signal')

plt.legend()
plt.title(f"{TICKER} Mean Reversion Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()
