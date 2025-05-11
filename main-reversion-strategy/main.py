import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


TICKER = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2024-12-31"
MA_WINDOW = 20

data = yf.download(TICKER, start=START_DATE, end=END_DATE)

print("Columns after download:")
print(data.columns)

data[('MA', TICKER)] = data[('Close', TICKER)].rolling(window=MA_WINDOW).mean()  # Multi-index for MA

print("Columns after calculating 'MA':")
print(data.columns)

print("First few rows after calculating 'MA':")
print(data[[('Close', TICKER), ('MA', TICKER)]].head(25))

data = data.dropna(subset=[('MA', TICKER)])

data["Signal"] = (data[('Close', TICKER)] < data[('MA', TICKER)]).astype(int)

data["Position"] = data["Signal"].diff()

plt.figure(figsize=(14, 7))
plt.plot(data[('Close', TICKER)], label="Close Price", alpha=0.5)
plt.plot(data[('MA', TICKER)], label=f"{MA_WINDOW}-day MA", linestyle="--")

plt.plot(data[data["Position"] == 1].index,
         data[('MA', TICKER)][data["Position"] == 1],
         "^", markersize=10, color='g', label='Buy Signal')

plt.plot(data[data["Position"] == -1].index,
         data[('MA', TICKER)][data["Position"] == -1],
         "v", markersize=10, color='r', label='Sell Signal')

plt.legend()
plt.title(f"{TICKER} Mean Reversion Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()
