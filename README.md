# Mean Reversion Strategy - Trading Model

This repository contains a Python script that executes a **Mean Reversion Strategy** to trade stocks. It assumes that asset price will revert back to their previous mean and thus, there is a buy/sell based on the comparison between the moving average of the stock and the current price of the stock.

The model obtains the historical stock prices through **Yahoo Finance API** and calculates the moving average. The model produces a buy/sell signal depending on whether the current stock price is above or below the moving average.

## Features
- Obtain the stock data from Yahoo Finance.
- Calculate a simple moving average (SMA) for a given stock.
- Generate buy signals in case the stock price goes below the moving average.
- Generate sell signals when the stock price is above the moving average.
- Plot the stock price, moving average, and buy/sell signals.

## Requirements

Ensure that you have the following Python libraries installed:

- `yfinance`: For downloading stock data from Yahoo Finance.
- `pandas`: For data manipulation and calculation.
- `matplotlib`: For plotting the results.

For installing the required libraries, use the following command:

```bash
pip install yfinance pandas matplotlib
```
