from common import reader
import numpy as np

depth_data = np.array(reader.get_array("input.csv"))
difference_to_prev = depth_data[1:] - depth_data[:-1]
increased_from_prev = difference_to_prev > 0

number_of_increased_from_prev = sum(increased_from_prev)
print(number_of_increased_from_prev)