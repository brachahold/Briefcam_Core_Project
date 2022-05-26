from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt


class GeoEstimator(ABC):
    def __init__(self, x_data, y_data, n):
        self.__x_data = x_data
        self.__y_data = y_data
        self.__n = n
        self.__d_min = float('inf')
        self.__best_model = None

    @property
    def best_model(self):
        return self.__best_model

    @property
    def x_data(self):
        return self.__x_data

    @property
    def y_data(self):
        return self.__y_data

    def random_sampling(self, n):
        sample = []
        save_ran = []
        count = 0
        while True:
            ran = np.random.randint(len(self.__x_data))
            if ran not in save_ran:
                sample.append((self.__x_data[ran], self.__y_data[ran]))
                save_ran.append(ran)
                count += 1
                if count == n:
                    break
        return sample

    def execute_estimator(self):
        # find best model
        for i in range(self.__n):
            model = self.find_model(self.random_sampling(self.num_points_per_model))
            d_temp = self.eval_model(model)
            if self.__d_min > d_temp:
                self.__best_model = model
                self.__d_min = d_temp

    def plot(self):
        ax = plt.gca()
        ax.cla()
        plt.scatter(self.__x_data, self.__y_data, c='blue', marker='o', label='data')
        ax.add_patch(self.get_plt_geo())
        plt.show()


    @abstractmethod
    def find_model(self, sample):
        raise NotImplementedError("Must override make_model")

    @abstractmethod
    def eval_model(self, model):
        raise NotImplementedError("Must override eval_model")

    @abstractmethod
    def get_plt_geo(self):
        raise NotImplementedError("Must override get_plt_geo")
