from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class GeoTester(ABC):
    def __init__(self, gt, es):
        self.gt = gt
        self.es = es
        self.score = None
        self.calc_score()

    def __str__(self):
        return f'Score of {self.__class__.__name__} is: {self.score}'

    def plot(self, x_points, y_points):
        ax = plt.gca()
        ax.cla()
        plt.scatter(x_points, y_points, c='blue', marker='o', label='data')
        gt, est = self.get_plt_geo()
        ax.add_patch(gt)
        ax.add_patch(est)
        plt.show()

    @abstractmethod
    def calc_score(self):
        raise NotImplementedError("Must override get_score")

    @staticmethod
    def get_general_score(t):
        return sum(map(lambda x: x.score, t))/len(t)


