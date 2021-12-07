from common import reader
import numpy as np
from typing import Optional

input = reader.get_row_array("input.csv")
bingo_boards = reader.get_bingo_boards("bingo_boards.csv")


# Part 1
class Board:
    def __init__(self, board: np.ndarray):
        self.board = board
        self.marked_board = np.zeros((len(board), len(board[0])))

    def add_number(self, number):
        self.marked_board += self.board == number
        return self

    def got_bingo(self) -> bool:
        return self.marked_board.all(0).any() or self.marked_board.all(1).any()


board_data = np.array_split(bingo_boards, bingo_boards.shape[0]/5)
boards = [Board(data.to_numpy()) for data in board_data]
score = 0

for i in input:
    boards = [board.add_number(i) for board in boards]
    got_bingo = np.array([board.got_bingo() for board in boards])
    if got_bingo.any():
        winner: Board = boards[np.argmax(got_bingo)]
        score = sum(winner.board[winner.marked_board == 0]) * i
        break

print(f'Part1 {score}')

# Part 2
boards = [Board(data.to_numpy()) for data in board_data]
loser: Optional[Board] = None
for i in input:
    boards = [board.add_number(i) for board in boards]
    no_bingo = np.array([~board.got_bingo() for board in boards])
    if sum(no_bingo) == 1:
        loser: Board = boards[np.argmax(no_bingo)]
    if sum(no_bingo) == 0:
        score = sum(loser.board[loser.marked_board == 0]) * i
        break

print(f'Part2 {score}')