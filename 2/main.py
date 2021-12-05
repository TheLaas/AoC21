from common import reader
import numpy as np

commands = reader.get_command_array("input.csv")

# Part 1
forward_list = np.array([c["value"] for c in commands if c["command"] == "forward"])
down_list = np.array([c["value"] for c in commands if c["command"] == "down"])
up_list = np.array([-c["value"] for c in commands if c["command"] == "up"])

horizontal_pos = sum(forward_list)
depth_pos = sum(down_list) + sum(up_list)
print(f'Part1 {depth_pos * horizontal_pos}')

# Part 2
aim = 0
depth = 0
for c in commands:
    if c["command"] == "down":
        aim += c["value"]
    elif c["command"] == "up":
        aim -= c["value"]
    elif c["command"] == "forward":
        depth += aim * c["value"]

print(f'Part2 {depth * horizontal_pos}')
