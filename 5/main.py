import numpy as np
import pandas as pd


data = pd.read_csv("input.csv", header=None, delimiter=r",|\s->\s", engine='python')
# data = pd.read_csv("test.csv", header=None, delimiter=r",|\s->\s", engine='python')

min_x = min([min(data[0]), min(data[2])])
min_y = min([min(data[1]), min(data[3])])

data[0] = data[0] - min_x
data[2] = data[2] - min_x

data[1] = data[1] - min_y
data[3] = data[3] - min_y

max_x = max([max(data[0]), max(data[2])])
max_y = max([max(data[1]), max(data[3])])


class Canvas:
    def __init__(self, x_lim, y_lim):
        self.canvas = np.zeros([y_lim + 1, x_lim + 1])

    def add_horizontal_line(self, p1, p2):
        v = p1[1]
        start = min([p1[0], p2[0]])
        end = max([p1[0], p2[0]]) + 1
        for i in range(start, end):
            self.canvas[v][i] += 1

    def add_vertical_line(self, p1, p2):
        h = p1[0]
        start = min([p1[1], p2[1]])
        end = max([p1[1], p2[1]]) + 1
        for i in range(start, end):
            self.canvas[i][h] += 1

    def add_line(self, p1, p2):
        grad = p2 - p1
        length = max(abs(grad))
        grad = grad / length
        x_ind = p1[0]
        y_ind = p1[1]
        for _ in range(0, length + 1):
            self.canvas[y_ind][x_ind] += 1
            x_ind = int(x_ind + grad[0])
            y_ind = int(y_ind + grad[1])


# Part 1
is_vertical = (data[0] - data[2]) == 0
is_horizontal = (data[1] - data[3]) == 0
vertical = data[is_vertical]
horizontal = data[is_horizontal]

canvas = Canvas(max_x, max_y)

for _, row in vertical.iterrows():
    p1 = row[0:2].to_numpy()
    p2 = row[2:4].to_numpy()
    canvas.add_vertical_line(p1, p2)

for _, row in horizontal.iterrows():
    p1 = row[0:2].to_numpy()
    p2 = row[2:4].to_numpy()
    canvas.add_horizontal_line(p1, p2)

print(f'Part1 {sum(sum(canvas.canvas > 1))}')

# Part 2
canvas = Canvas(max_x, max_y)
for _, row in data.iterrows():
    p1 = row[0:2].to_numpy()
    p2 = row[2:4].to_numpy()
    canvas.add_line(p1, p2)

print(f'Part2 {sum(sum(canvas.canvas > 1))}')