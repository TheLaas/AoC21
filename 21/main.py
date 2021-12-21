import numpy as np
from typing import Tuple

# Test
# players = np.array([
#     # Starting pos, score
#     [4, 0],
#     [8, 0]
#                     ])
# Input
players = np.array([
    # Starting pos, score
    [10, 0],
    [6, 0]
                    ])


def roll_dice(current_dice: int) -> Tuple[int, int]:
    result = 0
    for i in range(1, 4):
        current_dice %= 100
        current_dice += 1
        result += current_dice
    return result, current_dice


def update_pos(current_pos: int, dice_score: int) -> int:
    return (current_pos + dice_score - 1) % 10 + 1


# Part 1:
dice = 0
rounds = 0
while all(players[:, 1] < 1000):
    for player in players:
        dice_score, dice = roll_dice(dice)
        player[0] = update_pos(player[0], dice_score)
        player[1] += player[0]
        rounds += 3
        if player[1] >= 1000:
            break

result = rounds * min(players[:, 1])
print(f"Part 1 {result}")
