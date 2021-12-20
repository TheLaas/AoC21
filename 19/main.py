from functools import reduce

from common import reader
import numpy as np
import re
from typing import Dict, List, Tuple

lines = reader.get_lines("input.txt")

permutation = [
    [0, 1, 2],
    [1, 0, 2],
    [1, 2, 0],
    [0, 2, 1],
    [2, 0, 1],
    [2, 1, 0]
]
sign = [
    [[1, 1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1]],  # [0, 1, 2]
    [[-1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, -1, -1]],  # [1, 0, 2]
    [[-1, -1, 1], [1, -1, -1], [1, 1, 1], [-1, 1, -1]],  # [1, 2, 0]
    [[1, -1, 1], [-1, -1, -1], [-1, 1, 1], [1, 1, -1]],  # [0, 2, 1]
    [[1, 1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1]],  # [2, 0, 1]
    [[1, -1, 1], [-1, -1, -1], [-1, 1, 1], [1, 1, -1]]   # [2, 1, 0]
]


def get_scanner_detections(lines: List[str]) -> Dict[str, List[List[int]]]:
    found_scanners = {}
    name = ''
    for line in lines:
        if line == '\n':
            continue
        elif "---" in line:
            m = re.match('(---\s)([A-Za-z]*\s[0-9]+)(\s---)', line)
            name = m.group(2)
        elif name in found_scanners:
            coord = line[:-1].split(',')
            found_scanners[name].append([int(c) for c in coord])
        else:
            coord = line[:-1].split(',')
            found_scanners[name] = [[int(c) for c in coord]]
    return found_scanners


def compare_beacons(beacons_ref: np.ndarray, beacons_unknown: np.ndarray) -> int:
    return reduce(lambda count, unknown_vec: count + 1 if any((unknown_vec == beacons_ref).all(1)) else count,
                  beacons_unknown, 0)


def iterate_offsets(beacons_ref: np.ndarray, beacons_unknown: np.ndarray) -> Tuple[bool, np.ndarray, np.ndarray]:
    for vec_ref in beacons_ref:
        for vec_unknown in beacons_unknown:
            offset = vec_unknown - vec_ref
            offseted_beacons = beacons_unknown - offset
            number_of_matching = compare_beacons(beacons_ref, offseted_beacons)
            if number_of_matching >= 12:
                return True, offseted_beacons, offset
    return False, beacons_unknown, np.array([0, 0, 0])


def iterate_permutations(beacons_ref: np.ndarray, beacons_unknown: np.ndarray) -> Tuple[bool, np.ndarray, np.ndarray]:
    for i in range(0, 6):
        for j in range(0, 4):
            permuted_beacons = beacons_unknown[:, permutation[i]] * np.array(sign[i][j])
            match, offseted_beacons, offset = iterate_offsets(beacons_ref, permuted_beacons)
            if match:
                return True, offseted_beacons, offset
    return False, beacons_unknown, np.array([0, 0, 0])


def find_uniques(scanners: Dict) -> int:
    rows =  reduce(lambda total, new_rows: np.vstack((total, new_rows)), scanners.values(), np.array([float('inf'), float('inf'), float('inf')]))
    return len(np.unique(rows, axis=0)) - 1


scanners = get_scanner_detections(lines)
scanners = {key: np.array(value) for key, value in scanners.items()}
checked = {"scanner 0": []}
offsets = {"scanner 0": np.array([0, 0, 0])}
known: List[str] = ["scanner 0"]
while len(known) != len(scanners):
    for name, beacons in scanners.items():
        if name not in known:
            print(f"unknown: {name}")
            for ref in known:
                if name not in checked[ref]:
                    print(f"ref: {ref}")
                    match, aligned_beacons, offset_to_scan0 = iterate_permutations(scanners[ref], beacons)
                    checked[ref].append(name)
                    if match:
                        scanners[name] = aligned_beacons
                        known.append(name)
                        checked[name] = []
                        offsets[name] = offset_to_scan0
                        print(f"known {known}")
                        break

result = find_uniques(scanners)

# Part 1
print(f"Part 1 {result}")


# Part 2
def manhattan_dist(offsets: Dict) -> int:
    largest_man = 0
    for offset in offsets.values():
        for offset_inner in offsets.values():
            manhattan = sum(abs(offset - offset_inner))
            if manhattan > largest_man:
                largest_man = manhattan
    return largest_man

result = manhattan_dist(offsets)
print(f"Part 2: {result}")