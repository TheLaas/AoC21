from __future__ import annotations
from functools import reduce
from typing import List, Dict, Tuple
import re

import pandas as pd

# data = pd.read_csv("test1.txt", delimiter='-', header=None)
# data = pd.read_csv("test2.txt", delimiter='-', header=None)
# data = pd.read_csv("test3.txt", delimiter='-', header=None)
data = pd.read_csv("input.txt", delimiter='-', header=None)


class Path:
    def __init__(self, history: List[str], small_locked: bool = False):
        self.history = history
        self.current = history[-1]
        self.small_locked = small_locked

    def split(self, node_connections: Dict) -> List[Path]:
        decendants = []
        connected_nodes = node_connections[self.current]
        for node in connected_nodes:
            if self.is_upper_case(node) or node not in self.history:
                decendants.append(Path(self.history + [node]))
        return decendants

    def split_extended(self, node_connections: Dict) -> List[Path]:
        decendants = []
        connected_nodes = node_connections[self.current]
        for node in connected_nodes:
            if self.is_upper_case(node) or node not in self.history:
                decendants.append(Path(self.history + [node], self.small_locked))
            elif not self.small_locked and node != "start" and node != "end":
                decendants.append(Path(self.history + [node], True))

        return decendants

    @staticmethod
    def is_upper_case(node: str) -> bool:
        m = re.search(r'[A-Z]', node)
        return m is not None


def create_node_graph(connection_data: pd.DataFrame) -> Dict:
    node_connections = {}
    for _, row in connection_data.iterrows():
        if row[0] in node_connections:
            node_connections[row[0]].append(row[1])
        else:
            node_connections[row[0]] = [row[1]]

        if row[1] in node_connections:
            node_connections[row[1]].append(row[0])
        else:
            node_connections[row[1]] = [row[0]]

    return node_connections


def filter_completed_paths(paths: List[Path], completed_paths: List[Path]) -> List[Path]:
    alive_paths = []
    for path in paths:
        if path.current == "end":
            completed_paths.append(path)
        else:
            alive_paths.append(path)
    return alive_paths


# Part 1
node_tree = create_node_graph(data)
paths = [Path(["start"])]
completed_paths = []
while len(paths) > 0:
    paths = reduce(lambda new_paths, path: new_paths + path.split(node_tree), paths, [])
    paths = filter_completed_paths(paths, completed_paths)

result = len(completed_paths)
print(f"Part 1: {result}")

# Part 2
paths = [Path(["start"])]
completed_paths = []
while len(paths) > 0:
    paths = reduce(lambda new_paths, path: new_paths + path.split_extended(node_tree), paths, [])
    paths = filter_completed_paths(paths, completed_paths)

result = len(completed_paths)
print(f"Part 2: {result}")
