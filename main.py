import pandas as pd
import numpy as np

from utils.generic import read_file_with_pandas, max_min_arr, avg_arr


while True:
    text = input("some file name")
    if text == "break":
        break


    col=(read_file_with_pandas(text, input()))
    if col is not None:
        print(max_min_arr(col))
        print(avg_arr(col))