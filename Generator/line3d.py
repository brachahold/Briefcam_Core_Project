from geometry import Geometry
from Generator.geometry import Geometry
import random
import numpy as np
import matplotlib.pyplot as plt


class Line3D(Geometry):
    def __init__(self, point=None, direction=None):
        super().__init__()
        if direction is None:
            point = np.random.rand(3) * 6 - 6 / 2
            direction = np.random.rand(3) * 6 - 6 / 2
        self.__point = point
        self.__direction = direction / np.linalg.norm(direction)  # normalize

    def get_plt_geo(self):
        return plt.axline((self.__point[0], self.__point[1]), slope=self.__get_slope(), color='r')

    def get_rand_point_on_geometry(self):
        t = random.uniform(-10, 10)
        return self.__point + t * self.__direction

    def __get_slope(self):
        p = self.__point + self.__direction
        m = p - self.__point
        return m[1] / m[0]

    def get_prpendicular(self, p):
        return p, -1 / self.__get_slope()







