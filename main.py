# while True:
#     text = input("some text")
#     if text == "break":
#         break
#

import pandas as pd
import numpy as np

from utils.generic import read_file_with_pandas, max_min_arr, avg_arr


df=pd.read_csv("tourist - tourist.csv")

print(read_file_with_pandas("tourist - tourist.csv", "Days"))



print(max_min_arr(df["Days"]))
print(avg_arr(df["Days"]))