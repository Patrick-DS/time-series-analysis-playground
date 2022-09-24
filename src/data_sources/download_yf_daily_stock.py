import os
import yfinance as yf

ticker_symbol = "SPY"
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(
    period="1d",
    start="2015-1-1",
    end="2020-1-1",
)

if not os.path.exists("data/external/daily-stock-data"):
    os.makedirs("data/external/daily-stock-data")

ticker_df.to_csv(f"data/external/daily-stock-data/{ticker_symbol}.csv")