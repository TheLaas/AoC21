from common import reader
import numpy as np


def bin_to_int(bin_str: str) -> int:
    return int(bin_str, 2)


def most_common_bit(array: np.ndarray, bit: int) -> str:
    ones_in_bit_pos = array & bit > 0
    if sum(ones_in_bit_pos) > len(array)/2:
        return '1'
    elif sum(ones_in_bit_pos) < len(array)/2:
        return '0'
    else:
        return 'e'


def binary_complement(bin_str: str):
    return ['1' if b == '0' else '0' for b in bin_str]


bin_array = reader.get_bin_array("input.csv")
int_array = np.array([bin_to_int(b) for b in bin_array])
significant_bits = len(bin_array[0])


# Part 1
gamma = []

for i in range(0, significant_bits):
    gamma.insert(0, most_common_bit(int_array, 1 << i))

gamma_int = bin_to_int("".join(gamma))
epsilon_int = bin_to_int("".join(binary_complement(gamma)))
print(f'Part1 {gamma_int * epsilon_int}')


# Part 2
def oxygen_gen_rating(array: np.ndarray, start_bit) -> int:
    bit = most_common_bit(array, start_bit)
    ones = array & start_bit > 0
    if bit == '1' or bit == 'e':
        criteria_filter = ones
    else:
        criteria_filter = ~ones
    if sum(criteria_filter) == 1:
        return array[criteria_filter]
    else:
        return oxygen_gen_rating(array[criteria_filter], start_bit >> 1)


def CO2_scrub_rating(array: np.ndarray, start_bit) -> int:
    bit = most_common_bit(array, start_bit)
    ones = array & start_bit > 0
    if bit == '0':
        criteria_filter = ones
    else:
        criteria_filter = ~ones
    if sum(criteria_filter) == 1:
        return array[criteria_filter]
    else:
        return CO2_scrub_rating(array[criteria_filter], start_bit >> 1)


oxygen = oxygen_gen_rating(int_array, 1 << (significant_bits - 1))
CO2 = CO2_scrub_rating(int_array, 1 << (significant_bits - 1))
life_support_rating = CO2 * oxygen
print(oxygen)
print(CO2)
print(f'Part2 {life_support_rating}')
