from common import reader
import numpy as np

depth_data = np.array(reader.get_array("input.csv"))

# Part 1
difference_to_prev = depth_data[1:] - depth_data[:-1]
increased_from_prev = difference_to_prev > 0

number_of_increased_from_prev = sum(increased_from_prev)
print(f'Part1: {number_of_increased_from_prev}')

# Part 2
aggregated_depth = depth_data[:-2] + depth_data[1:-1] + depth_data[2: ]
difference_to_prev = aggregated_depth[1:] - aggregated_depth[:-1]
increased_from_prev = difference_to_prev > 0

number_of_increased_from_prev = sum(increased_from_prev)
print(f'Part2: {number_of_increased_from_prev}')

