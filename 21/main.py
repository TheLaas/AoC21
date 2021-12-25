import numpy as np
from typing import Tuple, Dict, NamedTuple

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

# Part 2
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
possible_rolls = np.array([
    [1, 1, 1],
    [1, 1, 2],
    [1, 1, 3],
    [1, 2, 1],
    [1, 2, 2],
    [1, 2, 3],
    [1, 3, 1],
    [1, 3, 2],
    [1, 3, 3],
    [2, 1, 1],
    [2, 1, 2],
    [2, 1, 3],
    [2, 2, 1],
    [2, 2, 2],
    [2, 2, 3],
    [2, 3, 1],
    [2, 3, 2],
    [2, 3, 3],
    [3, 1, 1],
    [3, 1, 2],
    [3, 1, 3],
    [3, 2, 1],
    [3, 2, 2],
    [3, 2, 3],
    [3, 3, 1],
    [3, 3, 2],
    [3, 3, 3],
])


def calc_dice_outcome_distribution(roll_outcomes: np.ndarray) -> Dict:
    sum_outcomes = {}
    for outcome in roll_outcomes:
        o_sum = sum(outcome)
        if o_sum in sum_outcomes:
            sum_outcomes[o_sum] += 1
        else:
            sum_outcomes[o_sum] = 1
    return sum_outcomes


class PState(NamedTuple):
    pos: int
    score: int


def update_player(p: PState, score_occ: int,  dice: int, dice_occ) -> Tuple[PState, int]:
    new_pos = update_pos(p.pos, dice)
    new_score = p.score + new_pos
    new_occ = score_occ * dice_occ
    return PState(new_pos, new_score), new_occ


def update_universes(universe: Dict, dice_distribution: Dict, wins: int, opponent_univ) -> Tuple[Dict, int]:
    p_universe = {}
    for p_curr, p_occ in universe.items():
        for dice, dice_occ in dice_distribution.items():
            p_new, p_occ_new = update_player(p_curr, p_occ, dice, dice_occ)
            if p_new.score >= 21:
                wins += p_occ_new * opponent_univ
            else:
                if p_new in p_universe:
                    p_universe[p_new] += p_occ_new
                else:
                    p_universe[p_new] = p_occ_new

    return p_universe, wins


dice_distr = calc_dice_outcome_distribution(possible_rolls)
p1_univ = {PState(players[0, 0], 0): 1}
p2_univ = {PState(players[1, 0], 0): 1}
p1_wins = 0
p2_wins = 0
while p1_univ and p2_univ:
    p1_univ, p1_wins = update_universes(p1_univ, dice_distr, p1_wins, sum(p2_univ.values()))
    p2_univ, p2_wins = update_universes(p2_univ, dice_distr, p2_wins, sum(p1_univ.values()))

result = max([p1_wins, p2_wins])
print(f"Part 2 {result}")
