from functools import reduce

from common import reader
from typing import List, Tuple

lines = reader.get_lines("test.txt")


def separate_input(lines: List[str]) -> Tuple[str, List[List[str]]]:
    enh_algo = lines.pop(0)[:-1]
    input_image = []
    for line in lines:
        if line != '\n':
            row = []
            for c in line[:-1]:
                row.append(c)
            input_image.append(row)
    return enh_algo, input_image


def translate_9_grid_region(region: List[List[str]]) -> int:
    bin_str = ""
    for i in range(0, 3):
        for j in range(0, 3):
            if region[i][j] == '#':
                bin_str += '1'
            else:
                bin_str += '0'
    return int(bin_str, 2)


def iterate_image(input_image: List[List[str]], enh_algo: str, padding_symbol: str) -> List[List[str]]:
    rows = len(input_image)
    cols = len(input_image[0])
    enhanced_image = []
    for i in range(-1, rows + 1):
        enhanced_image.append([])
        for j in range(-1, cols + 1):
            region = get_9_grid_region(i, j, input_image, padding_symbol)
            index = translate_9_grid_region(region)
            symbol = enh_algo[index]
            enhanced_image[i + 1].append(symbol)
    return enhanced_image


def calc_active_pixels(image: List[List[str]]) -> int:
    rows = len(image)
    cols = len(image[0])
    active_pixels = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if image[i][j] == "#":
                active_pixels += 1
    return active_pixels


def get_9_grid_region(x_ind: int, y_ind: int, image: List[List[str]], padding_symbol: str) -> List[List[str]]:
    rows = len(image)
    cols = len(image[0])
    region = [['.', '.', '.'] for i in range(0, 3)]
    for i in range(0, 3):
        for j in range(0, 3):
            im_x = x_ind + i - 1
            im_y = y_ind + j - 1
            if 0 <= im_x < rows and 0 <= im_y < cols:
                region[i][j] = image[im_x][im_y]
            else:
                region[i][j] = padding_symbol
    return region


enhance_algo, input_image = separate_input(lines)

# Part 1
new_image = iterate_image(input_image, enhance_algo, '.')
final_image = iterate_image(new_image, enhance_algo, '#')

result = calc_active_pixels(final_image)
print(f"Part 1: {result}")

