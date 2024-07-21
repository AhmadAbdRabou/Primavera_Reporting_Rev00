import pandas as pd

# Assuming that cal_data_df is your DataFrame

# Get index of row containing 'VIEW' in 'data' column
view_index = cal_data_df[cal_data_df['data'].str.contains('VIEW')].index[0]

# Select all rows after that index
selected_df = cal_data_df.iloc[view_index + 1:]

# If you want to include the 'VIEW' row too, use:
# selected_df = cal_data_df.iloc[view_index:]