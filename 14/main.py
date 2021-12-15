import pandas as pd
from typing import Tuple, Dict
from collections import Counter


def read_input(path: str) -> Tuple[str, Dict]:
    with open(path) as file:
        starting_template = file.readline()
        starting_template = starting_template[:-1]
        insertion_table = pd.read_csv(file, delimiter=r'\s->\s', header=None, engine='python')
        lookup_table = {row[0]: row[1] for _, row in insertion_table.iterrows()}
        return starting_template, lookup_table


def insert(polymer: str, lookup: Dict):
    new_polymer = ""
    for i in range(0, len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += lookup[polymer[i:i + 2]]
    return new_polymer + polymer[-1]


# Part 1
# polymer_template, pair_insertion = read_input("test.txt")
polymer_template, pair_insertion = read_input("input.txt")
for i in range(0, 10):
    polymer_template = insert(polymer_template, pair_insertion)
result = Counter(polymer_template).most_common()
print(f"Part 1 {result[0][1] - result[-1][1]}")


# Part 2
def read_input2(path: str) -> Tuple[str, Dict]:
    with open(path) as file:
        starting_template = file.readline()
        starting_template = starting_template[:-1]
        insertion_table = pd.read_csv(file, delimiter=r'\s->\s', header=None, engine='python')
        pair_spawn_table = {row[0]: (row[0][0] + row[1], row[1] + row[0][1]) for _, row in insertion_table.iterrows()}
        return starting_template, pair_spawn_table


class Polymer:
    def __init__(self, template: str, pair_spawn_table: Dict):
        self.template = template
        self.pair_spawn_table = pair_spawn_table
        self.pair_count = {}
        self.first_letter = template[0]
        self.last_letter = template[-1]

    def init_pair_count(self):
        for i in range(0, len(self.template) - 1):
            key = self.template[i:i + 2]
            if key in self.pair_count:
                self.pair_count[key] += 1
            else:
                self.pair_count[key] = 1

    def insert(self):
        new_count = {}
        for key in self.pair_count:
            (spawn1, spawn2) = self.pair_spawn_table[key]
            if spawn1 in new_count:
                new_count[spawn1] += self.pair_count[key]
            else:
                new_count[spawn1] = self.pair_count[key]
            if spawn2 in new_count:
                new_count[spawn2] += self.pair_count[key]
            else:
                new_count[spawn2] = self.pair_count[key]
        self.pair_count = new_count

    def count(self):
        count_result: Dict = {}
        for key in self.pair_count:
            [key1, key2] = key
            if key1 in count_result:
                count_result[key1] += self.pair_count[key]
            else:
                count_result[key1] = self.pair_count[key]
            if key2 in count_result:
                count_result[key2] += self.pair_count[key]
            else:
                count_result[key2] = self.pair_count[key]
        count_result[self.first_letter] += 1
        count_result[self.last_letter] += 1
        count_result = {key: int(value / 2) for key, value in count_result.items()}
        return count_result


polymer_template, pair_spawn = read_input2("input.txt")
polymer = Polymer(polymer_template, pair_spawn)
polymer.init_pair_count()
for i in range(0, 40):
    polymer.insert()
result = Counter(polymer.count()).most_common()
print(f"Part 2 {result[0][1] - result[-1][1]}")
