from __future__ import annotations
from typing import List
from common import reader
import numpy as np

initial_array = np.array(reader.get_row_array("input.csv"))
# initial_array = np.array([3, 4, 3, 1, 2])


# Part 1
def count_down_day_to_birth(array: np.ndarray) -> np.ndarray:
    return array - 1


def add_births(array: np.ndarray) -> np.ndarray:
    birthed = array < 0
    new_births = np.array([8 for birth in birthed if birth])
    return np.concatenate([array, new_births])


count_down = initial_array
for i in range(0, 80):
    count_down = count_down_day_to_birth(count_down)
    count_down = add_births(count_down)
    count_down[count_down < 0] = 6


print(f'Part1 {len(count_down)}')


# Part2
class Lantern:
    def __init__(self, days_til_birth, occurrence):
        self.days_til_birth = days_til_birth
        self.occurrence = occurrence

    def count_down(self):
        self.days_til_birth -= 1
        return self

    def spawn(self) -> Lantern:
        return Lantern(8, self.occurrence)

    def merge(self, lantern: Lantern):
        self.occurrence += lantern.occurrence

    def wrap(self):
        if self.days_til_birth < 0:
            self.days_til_birth = 6
        return self


def merge_common(lanterns: List[Lantern], common_days_til_birth: int) -> List[Lantern]:
    uncommon = [lantern for lantern in lanterns if lantern.days_til_birth != common_days_til_birth]
    common = [lantern for lantern in lanterns if lantern.days_til_birth == common_days_til_birth]
    if len(common) > 0:
        new_lantern = Lantern(common_days_til_birth, 0)
        for lantern in common:
            new_lantern.merge(lantern)
        return uncommon + [new_lantern]
    else:
        return uncommon


unique, counts = np.unique(initial_array, return_counts=True)
init = dict(zip(unique, counts))
lanterns = [Lantern(int(d), o) for d, o in init.items()]

for i in range(0, 256):
    lanterns = [lantern.count_down() for lantern in lanterns]
    new_lanterns = [lantern.spawn() for lantern in lanterns if lantern.days_til_birth < 0]
    lanterns += new_lanterns
    lanterns = [lantern.wrap() for lantern in lanterns]
    lanterns = merge_common(lanterns, 6)

number_of_lanterns = sum([l.occurrence for l in lanterns])
print(number_of_lanterns)