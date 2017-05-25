# -*- coding: utf-8 -*-
from reader import read
import time

l, h, n, points = read('donneesPourTests/ex100_5980')

# h = 20
# l = 25
# points = sorted( [(2, 5), (5, 17), (11, 4), (16, 6), (20, 1)], key=lambda x: x[0])

all_points = [(0, 0)] + points + [(l, 0)]

max_area = 0
max_rect = []

# METHODE 01
tic = time.time()

for i, (left, y1) in enumerate(all_points[:-1]):
    for j, (right, y2) in enumerate(all_points[i+1:]):

        # Chercher la hauteur minimum entre left et right
        min_top = h
        for x3, top in all_points:
            if left < x3 < right:
                if 0 < top < min_top:
                    min_top = top

        # Calculer la surface
        area = (right - left) * min_top

        # Garder les coordonnées de la surface max
        if area > max_area:
            max_area = area
            max_rect = [(left, 0), (left, min_top), (right, min_top), (right, 0)]

print("%.3f" % (time.time() - tic))
print('Méthode 01: ', max_rect, max_area)
