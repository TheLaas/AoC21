import csv
from typing import List, TypedDict
import pandas as pd


def get_array(path: str) -> List[int]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        return [int("".join(row)) for row in reader]


def get_bin_array(path: str) -> List[str]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        return ["".join(row) for row in reader]


def get_row_array(path: str) -> List[int]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        string_list = next(reader)
        return [int(item) for item in string_list]


class Command(TypedDict):
    command: str
    value: int


def get_command_array(path: str) -> List[Command]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        return [{"command": "".join(row[0]), "value": int("".join(row[1]))} for row in reader]


def get_bingo_boards(path: str) -> pd.DataFrame:
    return pd.read_csv(path, header=None, delimiter=r"\s+")


def get_map(path: str) -> List[List[int]]:
    with open(path) as map_file:
        lines = map_file.readlines()
        return [[int(char) for char in line if char != '\n'] for line in lines]


def get_lines(path: str) -> List[str]:
    with open(path) as file:
        return  file.readlines()


if __name__ == "__main__":
    result = get_lines('../10/test.txt')
    print(result)