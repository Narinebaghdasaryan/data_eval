import pandas as pd
import numpy as np

def read_file_with_pandas(file_name, column_name):
    csv_file_data=pd.read_csv(file_name)
    return csv_file_data[column_name]


def avg_arr(arr):
    return arr.mean()


def max_min_arr(arr):
    return arr.max(), arr.min()



