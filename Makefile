download_SPY_data:
	python3 src/data_sources/download_yf_daily_stock.py

compute_diff:
	python3 src/etl/create_first_difference.py

generate_plots:
	python3 src/visualizations/visualize_daily_stock_data.py

