from common import reader
import numpy as np

position_data = np.array(reader.get_row_array("input.csv"))
# position_data = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])


# Part 1
def dist_to_point(pos: int, array: np.ndarray) -> int:
    return sum(abs(array - pos))


def is_min(pos: int, array: np.ndarray, f) -> bool:
    return f(pos - 1, array) > f(pos, array) < f(pos + 1, array)


def derivative(pos: int, array: np.ndarray, f) -> float:
    return f(pos, array) - f(pos - 1, array)


init_guess = np.round(np.mean(position_data))
guess = init_guess
epsilon = 0.5

for _ in range(0, 1000):
    if is_min(guess, position_data, dist_to_point):
        print("min found")
        break
    guess -= epsilon * derivative(guess, position_data, dist_to_point)
    guess = round(guess)
print(f'Part1 {dist_to_point(guess, position_data)}')


# Part 2
def a_sum(diff: int) -> float:
    return diff * (diff + 1) / 2


def dist_2_point(pos: int, array: np.ndarray) -> float:
    dist = 0
    for i in array:
        dist += a_sum(abs(pos - i))
    return dist


best_i = min(position_data)
best = dist_2_point(best_i, position_data)

for i in range(min(position_data) + 1, max(position_data) + 1):
    guess = dist_2_point(i, position_data)
    if guess < best:
        best = guess
        best_i = i
print(f'Part2: {best} at {best_i}')
