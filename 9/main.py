from common import reader
import numpy as np
from typing import List, Set, Tuple

# data = reader.get_map("test.csv")
data = reader.get_map("input.csv")


def find_minima_inside(ma: np.ndarray) -> List[int]:
    [rows, columns] = ma.shape
    minimas = []
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if ma[i - 1, j] > ma[i, j] < ma[i + 1, j] \
                    and ma[i, j - 1] > ma[i, j] < ma[i, j + 1]:
                minimas.append(ma[i, j])
    return minimas


def find_minima_boundary(ma: np.ndarray) -> List[int]:
    [rows, columns] = ma.shape
    minimas = []
    for j in range(0, columns):
        for i in [0, rows - 1]:
            if j == 0 and i == 0 and ma[i + 1, j] > ma[i, j] < ma[i, j + 1]:
                minimas.append(ma[i, j])
            elif j == columns - 1 and i == 0 and ma[i + 1, j] > ma[i, j] < ma[i, j - 1]:
                minimas.append(ma[i, j])
            elif j == 0 and i == rows - 1 and ma[i - 1, j] > ma[i, j] < ma[i, j + 1]:
                minimas.append(ma[i, j])
            elif j == columns - 1 and i == rows - 1 and ma[i - 1, j] > ma[i, j] < ma[i, j - 1]:
                minimas.append(ma[i, j])
            elif i == 0 and ma[i, j] < ma[i + 1, j] and ma[i, j - 1] > ma[i, j] < ma[i, j + 1]:
                minimas.append(ma[i, j])
            elif i == rows - 1 and ma[i - 1, j] > ma[i, j] and ma[i, j - 1] > ma[i, j] < ma[i, j + 1]:
                minimas.append(ma[i, j])
    for i in range(1, rows - 1):
        for j in [0, columns - 1]:
            if j == 0 and ma[i, j] < ma[i, j + 1] and ma[i - 1, j] > ma[i, j] < ma[i + 1, j]:
                minimas.append(ma[i, j])
            elif j == columns - 1 and ma[i, j - 1] > ma[i, j] and ma[i - 1, j] > ma[i, j] < ma[i + 1, j]:
                minimas.append(ma[i, j])
    return minimas


# Part 1
puzzle_input = np.array(data)
minimas = find_minima_inside(puzzle_input) + find_minima_boundary(puzzle_input)
print(f'Part 1 {sum(minimas) + len(minimas)}')


# Part 2
def find_basin_indices(map_array: np.ndarray) -> List[Tuple[int, int]]:
    [rows, columns] = map_array.shape
    basin_indices = []
    for i in range(0, rows):
        for j in range(0, columns):
            if map_array[i, j] != 9:
                basin_indices.append((i, j))
    return basin_indices


def cluster(indices: List[Tuple[int, int]]):
    clusters = []
    candidates: Set[Tuple[int, int]] = {indices.pop()}
    confirmed = []
    while len(indices) > 0:
        candidate = candidates.pop()
        new = [c for c in spawn_candidates(candidate) if c in indices]
        for c in new:
            indices.remove(c)
            candidates.add(c)
        confirmed.append(candidate)
        if len(candidates) == 0:
            clusters.append(confirmed)
            confirmed = []
            candidates.add(indices.pop())
    return clusters


def spawn_candidates(c: Tuple[int, int]) -> List[Tuple[int, int]]:
    return [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)]


indices = find_basin_indices(puzzle_input)
clusters = cluster(indices)
cluster_lengths = [len(c) for c in clusters]
cluster_lengths.sort(reverse=True)
result = cluster_lengths[0] * cluster_lengths[1] * cluster_lengths[2]
print(f'Part 2 {result}')
