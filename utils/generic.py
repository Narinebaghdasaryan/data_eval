import pandas as pd
import numpy as np

def read_file_with_pandas(file_name, column_name):
    try:
        csv_file_data=pd.read_csv(file_name )
        return csv_file_data[column_name]
    except KeyError:
        print("Key Error: Columns ->",list(csv_file_data.columns), f"Provided -> {column_name}")
        return None
    except FileNotFoundError:
        print("File not found ->", f"{file_name} error")
        return None


def dataframe_info_with_pandas(file_name):
    try:
        csv_file_info=pd.read_csv(file_name )
        return csv_file_info.info()
    except FileNotFoundError:
        print("No such file or directory: ->", f"{file_name}")


def dataframe_columns(file_name):
    try:
        csv_file_info=pd.read_csv(file_name)
        return list(csv_file_info.columns)
    except FileNotFoundError:
        print("No such file or directory: ->", f"{file_name}")



def avg_arr(arr):
    try:
      return arr.mean()
    except TypeError:
        print("Cannot perform reduction 'mean' with string dtype")


def max_min_arr(arr):
    return arr.max(), arr.min()



