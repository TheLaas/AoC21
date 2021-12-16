from common import reader
import numpy as np
from typing import Dict, List, Tuple

input_data = np.array(reader.get_map("input.txt"))


# Part 1
class Board:
    def __init__(self, cost_map: Dict, end_point):
        self.cost_map = cost_map
        self.board = {key: float('inf') for key, _ in cost_map.items()}
        self.end_point = end_point

    def check_and_update_best_track(self, track: Tuple[int, Tuple[int, int]]):
        pos = track[1]
        cost = track[0] + self.cost_map[pos]
        if cost < self.board[pos]:
            self.board[pos] = cost
            return cost, pos

    def get_end_point_cost(self):
        return self.board[self.end_point]


def spawn_new(current_tracks: List[Tuple[int, Tuple[int, int]]]):
    new_tracks = []
    for tr in current_tracks:
        if tr:
            new_tracks.append((tr[0], (tr[1][0] + 1, tr[1][1])))
            new_tracks.append((tr[0], (tr[1][0] - 1, tr[1][1])))
            new_tracks.append((tr[0], (tr[1][0], tr[1][1] + 1)))
            new_tracks.append((tr[0], (tr[1][0], tr[1][1] - 1)))
    return new_tracks


def do_search(cost_data):
    [rows, columns] = cost_data.shape
    map_data = {idx: value for idx, value in np.ndenumerate(cost_data)}

    board = Board(map_data, (rows - 1, columns - 1))
    init_pos = (0, 0)
    tracks = [(0, init_pos)]
    while len(tracks) > 0:
        tracks = [board.check_and_update_best_track(track) for track in tracks]
        tracks = spawn_new(tracks)
        tracks = [track for track in tracks if track[1] in map_data]
        tracks.sort(key=lambda x: x[0])
    return board.get_end_point_cost() - map_data[(0, 0)]


print(f"Part 1 {do_search(input_data)}")


# Part 2
def fold_right(data: np.ndarray, times: int):
    fold = data
    for i in range(0, times):
        fold = fold + 1
        fold[fold > 9] = 1
        data = np.c_[data, fold]
    return data


def fold_down(data: np.ndarray, times: int):
    fold = data
    for i in range(0, times):
        fold = fold + 1
        fold[fold > 9] = 1
        data = np.r_[data, fold]
    return data


extended_input = fold_right(input_data, 4)
extended_input = fold_down(extended_input, 4)

print(f"Part2 {do_search(extended_input)}")
