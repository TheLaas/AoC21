from functools import reduce

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", header=None, delimiter=r"\s\|\s|\s", engine='python')
# data = pd.read_csv("test.csv", header=None, delimiter=r"\s\|\s|\s", engine='python')

len_1 = 2
len_4 = 4
len_7 = 3
len_8 = 7

# Part 1
output_data = data.iloc[:, -4:]
total_number = 0
for _, row in output_data.iterrows():
    for _, item in row.iteritems():
        len_item = len(item)
        if len_item == len_1 or len_item == len_4 or len_item == len_7 or len_item == len_8:
            total_number += 1
print(f'Part1 {total_number}')

# Part 2
segments = {
    "a": 1 << 0,
    "b": 1 << 1,
    "c": 1 << 2,
    "d": 1 << 3,
    "e": 1 << 4,
    "f": 1 << 5,
    "g": 1 << 6
}


def char_to_bin(char) -> int:
    return segments[char]


def str_to_bin(s: str) -> int:
    return reduce(lambda a, b: a | char_to_bin(b), s, 0)


def string_intersection(s1: str, known: int) -> int:
    return str_to_bin(s1) & known


input_data: pd.DataFrame = data.iloc[:, :-4]
output_data: pd.DataFrame = data.iloc[:, -4:]

result = []

for i, row in input_data.iterrows():
    res = np.zeros(10)
    res = res.astype(int)
    unknown_list = row.tolist()
    list_5 = []
    list_6 = []
    output = []
    for unknown in unknown_list:
        if len(unknown) == len_1:
            res[1] = str_to_bin(unknown)
        elif len(unknown) == len_4:
            res[4] = str_to_bin(unknown)
        elif len(unknown) == len_7:
            res[7] = str_to_bin(unknown)
        elif len(unknown) == len_8:
            res[8] = str_to_bin(unknown)
        elif len(unknown) == 5:
            list_5.append(unknown)
        elif len(unknown) == 6:
            list_6.append(unknown)

    for unknown in list_6:
        if string_intersection(unknown, res[1]) != res[1]:
            res[6] = str_to_bin(unknown)
        elif string_intersection(unknown, res[4]) == res[4]:
            res[9] = str_to_bin(unknown)
        else:
            res[0] = str_to_bin(unknown)

    for unknown in list_5:
        if string_intersection(unknown, res[1]) == res[1]:
            res[3] = str_to_bin(unknown)
        elif string_intersection(unknown, res[6]) == str_to_bin(unknown):
            res[5] = str_to_bin(unknown)
        else:
            res[2] = str_to_bin(unknown)

    output = output_data.iloc[i, :].tolist()
    multiplier = 1000
    number = 0
    for unknown in output:
        digit = np.argmax(str_to_bin(unknown) == res)
        number += digit * multiplier
        multiplier /= 10
    result.append(number)

print(f'Part2 {sum(result)}')