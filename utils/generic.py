import pandas as pd
import numpy as pd

def read_file_with_pandas(file_name):
    csv_file_data=pd.read_csv(file_name)
    return csv_file_data


def arr_mijin(arr):
    return arr.mean()


