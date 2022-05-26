from abc import ABC, abstractmethod
import pickle
import numpy as np
import matplotlib.pyplot as plt


class GeoEstimator(ABC):
    def __init__(self, x_data, y_data, n):
        self.x_data = x_data
        self.y_data = y_data
        self.n = n
        self.d_min = float('inf')
        self.best_model = None

    def random_sampling(self, n):
        sample = []
        save_ran = []
        count = 0
        while True:
            ran = np.random.randint(len(self.x_data))
            if ran not in save_ran:
                sample.append((self.x_data[ran], self.y_data[ran]))
                save_ran.append(ran)
                count += 1
                if count == n:
                    break
        return sample

    def execute_estimator(self):
        # find best model
        for i in range(self.n):
            model = self.find_model(self.random_sampling(self.num_points_per_model))
            d_temp = self.eval_model(model)
            if self.d_min > d_temp:
                self.best_model = model
                self.d_min = d_temp

    def plot(self):
        ax = plt.gca()
        ax.cla()
        plt.scatter(self.x_data, self.y_data, c='blue', marker='o', label='data')
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
