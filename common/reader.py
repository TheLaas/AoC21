import csv
from typing import List, TypedDict


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


if __name__ == "__main__":
    result = get_row_array('../6/input.csv')
    print(result)
