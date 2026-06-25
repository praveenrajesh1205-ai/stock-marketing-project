import os
import yfinance as yf
import matplotlib.pyplot as plt
from ta.momentum import RSIIndicator

os.makedirs("Data", exist_ok=True)

stock = yf.download("005930.KS", start="2024-01-01", end="2026-01-01")

stock.to_csv("Data/Samsung_Stock_Data.csv")

data = stock.copy()

if hasattr(data.columns, "nlevels") and data.columns.nlevels > 1:
    data.columns = data.columns.get_level_values(0)

data['MA20'] = data['Close'].rolling(window=20).mean()

close = data['Close'].astype(float)

rsi = RSIIndicator(close=close, window=14)
data['RSI'] = rsi.rsi()

plt.figure(figsize=(12, 6))
plt.plot(data["Close"])
plt.title("Samsung Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid()
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(data['Volume'])
plt.title("Volume Chart")
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close')
plt.plot(data['MA20'], label='MA20')
plt.legend()
plt.title("Moving Average (MA20)")
plt.grid()
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(data['RSI'], label='RSI')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.legend()
plt.title("RSI Indicator")
plt.grid()
plt.show()