import numpy as np
import pandas as pd


# data = pd.read_csv("input.csv", header=None, delimiter=r"\s\|\s|\s", engine='python')
data = pd.read_csv("test.csv", header=None, delimiter=r"\s\|\s|\s", engine='python')

len_1 = 2
len_4 = 4
len_7 = 3
len_8 = 7

output_data = data.iloc[:, -4:]
total_number = 0
for _, row in output_data.iterrows():
    for _, item in row.iteritems():
        len_item = len(item)
        if len_item == len_1 or len_item == len_4 or len_item == len_7 or len_item == len_8:
            total_number += 1
print(total_number)