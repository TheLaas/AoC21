import csv
from typing import List


def get_array(path: str) -> List[int]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        return [int("".join(row)) for row in reader]


if __name__ == "__main__":
    print("Running code")
    result = get_array('../1/input.csv')
    print(result)