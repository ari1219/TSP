# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pickle

# params
num_of_points = 100

# make points
points = np.random.rand(num_of_points, 2)

# save points image
plt.scatter(points[:, 0], points[:, 1])
plt.savefig("figure/fig.png")

# save made points
with open("data/points.pickle", "bw") as f:
    pickle.dump(points, f)
