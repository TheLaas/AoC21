from common import reader
import numpy as np

# map_data = np.array(reader.get_map("test.txt"))
map_data = np.array(reader.get_map("input.txt"))


def increase_neighbours(octu_map: np.ndarray, row: int, column: int):
    (rows, columns) = octu_map.shape
    for i in range(0, 3):
        for j in range(0, 3):
            row_ind = row - 1 + i
            col_ind = column - 1 + j
            if 0 <= row_ind < rows and 0 <= col_ind < columns and octu_map[row_ind, col_ind] > 0:
                octu_map[row_ind, col_ind] += 1


def iterate_flashing(octu_map: np.ndarray):
    new_flashing = octu_map > 9
    if new_flashing.any():
        (rows, columns) = octu_map.shape
        for i in range(0, rows):
            for j in range(0, columns):
                if new_flashing[i, j]:
                    increase_neighbours(octu_map, i, j)
        octu_map[new_flashing] = 0
        iterate_flashing(octu_map)


def count_flashing(octu_map: np.ndarray) -> int:
    return sum(sum(octu_map == 0))


# Part 1
flashing_total = 0
for _ in range(0, 100):
    map_data += 1
    iterate_flashing(map_data)
    flashing_total += count_flashing(map_data)

print(f"Part 1: {flashing_total}")

# Part 2
# map_data = np.array(reader.get_map("test.txt"))
map_data = np.array(reader.get_map("input.txt"))
result = 0
while (map_data > 0).any():
    map_data += 1
    iterate_flashing(map_data)
    result += 1

print(f"Part 2: {result}")