# -*- coding:utf-8 -*-

import pickle
import numpy as np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import random
from util import *

def do_gen_optimize(points, iteration=1000, return_all_cost=True):
    order = list(range(len(points)))
    random.shuffle(order)
    length = [calc_path_length(points, order)]*(iteration+1)
    for i in range(1, iteration+1):
        n1 = np.random.randint(0, len(points))
        n2 = np.random.randint(0, len(points))
        while n2 == n1:
            n2 = np.random.randint(0, len(points))
        swaped_order = swap_order(order, n1, n2)
        l = calc_path_length(points, swaped_order)
        if length[i-1] > l:
            order = swaped_order
            length[i] = l
        else:
            length[i] = length[i-1]
    if return_all_cost:
        return order, length
    else:
        return order, length[-1]

if __name__ == "__main__":
    points = read_points()
    l = do_gen_optimize(points, iteration=100000, return_all_cost=True)
#    costs = Parallel(n_jobs=-1, verbose=10)([delayed(do_gen_optimize)(points, return_all_cost=False) for i in range(1000)])
    x = list(range(len(l[1])))
    plt.plot(x, l[1])
    plt.show()
