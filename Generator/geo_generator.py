from abc import ABC, abstractmethod
import random
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


class GeoGenerator(ABC):
    def __init__(self):
        self.__points = []

    def plot(self):
        ax = plt.gca()
        ax.cla()
        x = [i[0] for i in self.__points]
        y = [i[1] for i in self.__points]
        plt.scatter(x, y)
        ax.add_patch(self.get_plt_geo())
        plt.show()

    def generate_noise_points(self, num, sigma, limit):
        for n in range(num):
            original = self.get_rand_point_on_geometry()
            point, slope = self.get_prpendicular(original)
            dis = self.__get_rand_dis_inlier_outlier(sigma, limit)
            self.__points.append(self.__get_point_by_dis(point, slope, dis))

    @property
    def points(self):
        return self.__points

    def __get_point_by_dis(self, point, slope, dis):
        dx = sqrt(dis / (slope ** 2 + 1)) if dis >= 0 else -sqrt(-dis / (slope ** 2 + 1))
        dy = slope * dx
        return np.array([point[0] + dx, point[1] + dy])

    def __get_rand_dis_inlier_outlier(self, sigma, limit):
        inlier = True if random.randint(0, 4) else False  # in 80% the point will be inlier and in 20% outlier
        return random.uniform(-sigma, sigma) if inlier else random.uniform(-limit, limit)

    @abstractmethod
    def get_rand_point_on_geometry(self):
        raise NotImplementedError("Must override get_rand_point_on_geometry")

    @abstractmethod
    def get_prpendicular(self, p):
        raise NotImplementedError("Must override get_prpendicular")

    @abstractmethod
    def get_plt_geo(self):
        raise NotImplementedError("Must override get_plt_geo")
