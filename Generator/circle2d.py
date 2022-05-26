from Generator.geo_generator import GeoGenerator
import random
from math import sqrt, pi, cos, sin
import numpy as np
import matplotlib.pyplot as plt


class Circle2D(GeoGenerator):
    def __init__(self, center=None, radius=None):
        super().__init__()
        if radius is None:
            center = np.random.rand(2) * 6 - 6 / 2
            radius = random.uniform(0, 1)
        self.__radius = radius
        self.__center = center

    @property
    def radius(self):
        return self.__radius

    @property
    def center(self):
        return self.__center

    def get_plt_geo(self):
        return plt.Circle((self.__center[0], self.__center[1]), self.__radius, color='r', fill=False)

    def get_rand_point_on_geometry(self):
        theta = random.random() * 2 * pi
        return np.array([self.__center[0] + cos(theta) * self.__radius, self.__center[1] + sin(theta) * self.__radius])

    def get_prpendicular(self, p):
        m = p - self.__center
        return p, m[1] / m[0]
