import pandas as pd

def add_indicators(data):
    data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

    data["MA20"] = data["Close"].rolling(window=20).mean()

    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    return data