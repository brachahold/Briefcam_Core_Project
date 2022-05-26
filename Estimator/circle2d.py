from Estimator.geo_estimator import GeoEstimator
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


class Circle2D(GeoEstimator):
    def __init__(self, x_data, y_data, n):
        super().__init__(x_data, y_data, n)
        self.num_points_per_model = 3

    def find_model(self, sample):
        pt1 = sample[0]
        pt2 = sample[1]
        pt3 = sample[2]
        A = np.array([[pt2[0] - pt1[0], pt2[1] - pt1[1]], [pt3[0] - pt2[0], pt3[1] - pt2[1]]])
        B = np.array([[pt2[0] ** 2 - pt1[0] ** 2 + pt2[1] ** 2 - pt1[1] ** 2],
                      [pt3[0] ** 2 - pt2[0] ** 2 + pt3[1] ** 2 - pt2[1] ** 2]])
        inv_A = inv(A)
        c_x, c_y = np.dot(inv_A, B) / 2
        c_x, c_y = c_x[0], c_y[0]
        r = np.sqrt((c_x - pt1[0]) ** 2 + (c_y - pt1[1]) ** 2)
        return c_x, c_y, r

    def eval_model(self, model):
        d = 0
        c_x, c_y, r = model
        for i in range(len(self.x_data)):
            dis = np.sqrt((self.x_data[i] - c_x) ** 2 + (self.y_data[i] - c_y) ** 2)
            if dis >= r:
                d += dis - r
            else:
                d += r - dis
        return d

    def get_plt_geo(self):
        return plt.Circle((self.best_model[0], self.best_model[1]), radius=self.best_model[2], color='r', fc='y', fill=False)
