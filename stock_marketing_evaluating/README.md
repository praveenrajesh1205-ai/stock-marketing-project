 Stock Market Dashboard

 Overview

This project is an interactive Stock Market Dashboard built using Python, Dash, Plotly, and Yahoo Finance. The dashboard allows users to analyze stock market data through dynamic visualizations and technical indicators.

Users can select different stocks and date ranges to view price trends, trading volume, moving averages, and RSI (Relative Strength Index).

 Features

* Interactive stock selection
* Custom date range filtering
* Real-time stock data from Yahoo Finance
* Stock price visualization
* Volume analysis
* 20-Day Moving Average (MA20)
* Relative Strength Index (RSI)
* Responsive web dashboard using Dash

 Stocks Included

* Samsung Electronics (005930.KS)
* Reliance Industries (RELIANCE.NS)
* Google (GOOGL)

Technologies Used

* Python
* Dash
* Plotly
* Pandas
* yFinance
* TA (Technical Analysis Library)

Installation

Install the required packages:

```bash
pip install dash plotly pandas yfinance ta
```

 Project Structure

```text
stock_marketing_evaluating/
│
├── dashboard.py
├── Data/
├── README.md
└── requirements.txt
```

 Running the Application

Run the dashboard using:

```bash
py dashboard.py
```

or

```bash
python dashboard.py
```

After execution, open the local server URL displayed in the terminal, typically:

```text
http://127.0.0.1:8050/
```

Dashboard Components

Stock Price Chart

Displays historical closing prices for the selected stock.

 Volume Chart

Shows trading volume over the selected period.

 Moving Average (MA20)

Displays the 20-day moving average alongside stock prices.

 RSI Indicator

Shows market momentum using the Relative Strength Index:

* RSI > 70 : Overbought
* RSI < 30 : Oversold

 Future Enhancements

* Additional technical indicators
* Candlestick charts
* Stock prediction models
* Portfolio tracking
* News sentiment analysis
* Export reports to PDF

 Author

Praveen

 License

This project is created for educational and learning purposes.