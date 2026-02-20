import pandas as pd
import numpy as np

from utils.generic import read_file_with_pandas, max_min_arr, avg_arr, dataframe_info_with_pandas, read_column_with_pandas, dataframe_columns


while True:
    text = input("Input file name ->  ")
    if text == "break":
        break

    read_dataframe = read_file_with_pandas(text)

    if read_dataframe is None:
        continue

    print(read_dataframe.head(5))

    print(dataframe_columns(read_dataframe))

    column_name = input("Input column name -> ")

    column_data = read_column_with_pandas(read_dataframe, column_name)

    print(dataframe_info_with_pandas(read_dataframe))

    if column_data is not None:
        print(max_min_arr(column_data))
        print('mijin', avg_arr(column_data))

