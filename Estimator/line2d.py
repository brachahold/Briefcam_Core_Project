from Estimator.geo_estimator import GeoEstimator
import numpy as np
import matplotlib.pyplot as plt


class Line2D(GeoEstimator):
    def __init__(self, x_data, y_data, n):
        super().__init__(x_data, y_data, n)
        self.num_points_per_model = 2

    def find_model(self, sample):
        pt1 = sample[0]
        pt2 = sample[1]
        slope = (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
        return pt1[0], pt1[1], slope

    def eval_model(self, model):
        d = 0
        x, y, m = model
        n = y - m * x
        for i in range(len(self.x_data)):
            dis = abs((m * self.x_data[i] - self.y_data[i] + n) / np.sqrt(m ** 2 + 1))
            d += dis
        return d

    def get_plt_geo(self):
        return plt.axline((self.best_model[0], self.best_model[1]), slope=self.best_model[2], color='r')
