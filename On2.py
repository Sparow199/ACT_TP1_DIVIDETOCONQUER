# -*- coding: utf-8 -*-
import time
from reader import read

h = 20
l = 25

l, h, n, all_points = read('donneesPourTests/ex100_5980')

# all_points = sorted([(2, 5), (5, 17), (11, 4), (16, 6), (20, 1)], key=lambda x: x[0])
# h = 500
max_area = 0
max_rect = []

tic = time.time()

for i, (x1, y1) in enumerate(all_points[:-1]):
    min_h = h
    x_p1 = x1
    for j, (x2, y2) in enumerate(all_points[i+1:]):

        x_p2 = x2

        if x1 != all_points[j-1][0] and y2 < min_h:
            min_h = y2

        width = x_p2 - x_p1
        area = width * min_h

        if area > max_area:
            max_area = area
            max_rect = [(x1, 0), (x1, y1), (x2, y1), (x2,0)]

print("%.3f" % (time.time() - tic))
print(max_area, max_rect)

