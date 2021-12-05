import csv
from typing import List, TypedDict


def get_array(path: str) -> List[int]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        return [int("".join(row)) for row in reader]


class Command(TypedDict):
    command: str
    value: int


def get_command_array(path: str) -> List[Command]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        return [{"command": "".join(row[0]), "value": int("".join(row[1]))} for row in reader]


if __name__ == "__main__":
    result = get_command_array('../2/input.csv')
    print(result)
