import pandas as pd
import numpy as np

from utils.generic import read_file_with_pandas, max_min_arr, avg_arr, dataframe_info_with_pandas, dataframe_columns


while True:
    text = input("some file name")
    if text == "break":
        break

    print(dataframe_columns(text))

    dataframe_info=dataframe_info_with_pandas(text)

    print(dataframe_info)



    col=(read_file_with_pandas(text, input("column name")))
    if col is not None:
        print(max_min_arr(col))
        print(avg_arr(col))

