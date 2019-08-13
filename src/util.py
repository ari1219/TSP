# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pickle
import copy

# read points file
def read_points():
    with open("data/points.pickle", "br") as f:
        points = pickle.load(f)
    return points

# calc path length
def calc_path_length(points, order):
    l = 0.
    for i in range(len(order)-1):
        l += np.linalg.norm(points[order[i]]-points[order[i+1]])
    l += np.linalg.norm(points[order[-1]]-points[order[0]])
    return l

# swap order
def swap_order(order, n1, n2):
    swap = copy.deepcopy(order)
    swap[n1] = order[n2]
    swap[n2] = order[n1]
    return swap

# for debug
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5]
    a = swap_order(x, 0, 2)
    print(x, a)
