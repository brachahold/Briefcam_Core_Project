from Generator.geo_generator import GeoGenerator
import random
import numpy as np
import matplotlib.pyplot as plt


class Line2D(GeoGenerator):
    def __init__(self, point=None, direction=None):
        super().__init__()
        if direction is None:
            point = np.random.rand(2) * 6 - 6 / 2
            direction = np.random.rand(2) * 6 - 6 / 2
        self.__point = point
        self.__direction = direction / np.linalg.norm(direction)  # normalize

    @property
    def point(self):
        return self.__point

    @property
    def direction(self):
        return self.__direction

    def get_plt_geo(self):
        return plt.axline((self.__point[0], self.__point[1]), slope=self.get_slope(), color='r')

    def get_rand_point_on_geometry(self):
        t = random.uniform(-10, 10)
        return self.__point + t * self.__direction

    def get_slope(self):
        p = self.__point + self.__direction
        m = p - self.__point
        return m[1] / m[0]

    def get_prpendicular(self, p):
        return p, -1 / self.get_slope()
