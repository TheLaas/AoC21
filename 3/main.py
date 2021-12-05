from common import reader
import numpy as np


def bin_to_int(bin_str: str) -> int:
    return int(bin_str, 2)


def calc_ones(array: np.ndarray, bit: int) -> str:
    ones_in_bit_pos = array & bit > 0
    if sum(ones_in_bit_pos) > len(array)/2:
        return '1'
    else:
        return '0'


def binary_complement(bin: str):
    return ['1' if b == '0' else '0' for b in bin]


# Part 1
bin_array = reader.get_bin_array("input.csv")
int_array = np.array([bin_to_int(b) for b in bin_array])
significant_bytes = len(bin_array[0])

gamma = []

for i in range(0, significant_bytes):
    gamma.insert(0, calc_ones(int_array, 1 << i))

gamma_int = bin_to_int("".join(gamma))
epsilon_int = bin_to_int("".join(binary_complement(gamma)))
print(f'Part1 {gamma_int * epsilon_int}')