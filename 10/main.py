from functools import reduce

from common import reader
import numpy as np

# data = reader.get_lines("test.txt")
data = reader.get_lines("input.txt")

closing_characters = [']', '}', '>', ')']
closing_by_open = {'(': ')', '[': ']', '<': '>', '{': '}'}
score = {']': 57, '}': 1197, '>': 25137, ')': 3}


def find_first_illegal(string:str) -> int:
    open_characters = []
    for char in string:
        if char in closing_characters:
            if char != closing_by_open[open_characters.pop()]:
                return score[char]
        else:
            open_characters.append(char)
    return 0


# Part 1
total_score = 0
for line in data:
    total_score += find_first_illegal(line)

print(f'Part 1 {total_score}')

# Part 2
score_2 = {'[': 2, '{': 3, '<': 4, '(': 1}


def find_closing_sequence(string: str) -> int:
    open_characters = []
    for char in string:
        if char in closing_characters:
            open_characters.pop()
        elif char == '\n':
            continue
        else:
            open_characters.append(char)
    open_characters.reverse()
    return reduce(lambda total, c: total * 5 + score_2[c], open_characters, 0)


scores = []
for line in data:
    if find_first_illegal(line) > 0:
        continue
    else:
        scores.append(find_closing_sequence(line))
scores.sort()
index = int(np.floor(len(scores)/2))
print(f'Part 2 {scores[index]}')