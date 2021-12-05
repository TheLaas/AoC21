from common import reader
import numpy as np

depth_data = np.array(reader.get_array("input.csv"))


def change_to_prev(array: np.ndarray) -> np.ndarray:
    return array[1:] - array[:-1]


def number_of_increased_from_prev(array: np.ndarray) -> int:
    difference_to_prev = change_to_prev(array)
    return sum(difference_to_prev > 0)


# Part 1
print(f'Part1: {number_of_increased_from_prev(depth_data)}')

# Part 2
aggregated_depth = depth_data[:-2] + depth_data[1:-1] + depth_data[2: ]
print(f'Part2: {number_of_increased_from_prev(aggregated_depth)}')

