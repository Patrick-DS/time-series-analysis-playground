import pandas as pd

ticker_symbol = "SPY"
date_column = "Date"
csv_path = f"data/external/daily-stock-data/{ticker_symbol}.csv"

# Load external data
df = pd.read_csv(csv_path, parse_dates=[date_column], index_col=date_column)

# Compute series required to generate graphs
def get_first_difference(time_series, lag=1):
    """
    Computes the first difference of a time series.
    """
    return time_series.diff(lag)[1:]

for column_name in ["Open", "Close", "High", "Low"]:
    df[f"D({column_name})"] = get_first_difference(df[column_name])

# Save generated data
df.to_csv(csv_path.replace("external", "processed"))