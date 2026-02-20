import pandas as pd

def read_file_with_pandas(file_name):

    try:
        csv_file_data = pd.read_csv(file_name)
        return csv_file_data
    except FileNotFoundError:
        print("File not found ->", f"{file_name} error")
        return None


def read_column_with_pandas(csv_file_data, column_name):
    if csv_file_data is None:
        return None
    try:
        return  csv_file_data[column_name]
    except KeyError:
        print("Key Error: Columns ->", list(csv_file_data.columns), f"Provided -> {column_name}")
        return None

def dataframe_info_with_pandas(csv_file_data):
    if csv_file_data is None:
        return None
    return  csv_file_data.info()



def dataframe_columns(csv_file_data):
    if csv_file_data is None:
        return None
    return csv_file_data.columns


def avg_arr(column_name):
    try:
      return column_name.mean()
    except TypeError:
        print("Cannot perform reduction 'mean' with string dtype")


def max_min_arr(column_name):
    return (f'max_value is in -> {column_name.max()} column  and min value is in ->  {column_name.min()} column')



