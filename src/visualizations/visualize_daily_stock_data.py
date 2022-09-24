import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import os

# Load data
ticker_symbol = "SPY"
ticker_df = pd.read_csv(
    f"data/processed/daily-stock-data/{ticker_symbol}.csv",
    parse_dates=["Date"],
    index_col="Date",
)

# Secure directory for saving data
figure_directory = f"{ticker_symbol}-daily-stock"
figure_path = f"reports/figures/{figure_directory}"

if not os.path.exists(figure_path):
    os.makedirs(figure_path)

ser = ticker_df["Close"]
diff_ser = ticker_df["D(Close)"][1:]

def plot_series(series, figures_folder):
    """
    Plots a series, its ACF and PACF, and saves the plots in the given path (figures_folder).
    """
    # Main series plot
    plt.figure(figsize=(10,4))
    plt.plot(series)
    plt.title(
        f"Stock price over time ({ticker_symbol})", 
        fontsize=20,
    )
    plt.ylabel(
        "Price",
        fontsize=16,
    )
    for year in range(2015, 2020):
        plt.axvline(
            pd.to_datetime(f"{year}-01-01"),
            color="k",
            linestyle="--",
            alpha=0.2,
        )
    plt.savefig(f"{figures_folder}/value.png")
    # ACF plot
    plot_acf(series)
    plt.savefig(f"{figures_folder}/ACF.png")
    # PACF plot
    plot_pacf(series)
    plt.savefig(f"{figures_folder}/PACF.png")


# SPY series
spy_path = f"{figure_path}/{ticker_symbol}"
if not os.path.exists(spy_path):
    os.makedirs(spy_path)

plot_series(ser, spy_path)

diff_spy_path = f"{figure_path}/{ticker_symbol}-diff"
if not os.path.exists(diff_spy_path):
    os.makedirs(diff_spy_path)

plot_series(diff_ser, diff_spy_path)