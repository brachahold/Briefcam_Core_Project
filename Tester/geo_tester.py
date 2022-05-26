from abc import ABC, abstractmethod


class GeoTester(ABC):
    def __init__(self, gt, es):
        self.gt = gt
        self.es = es
        self.score = None
        self.calc_score()

    def plot(self):
        print(f'Score of {self.__class__.__name__} is: {self.score}')

    @abstractmethod
    def calc_score(self):
        raise NotImplementedError("Must override get_score")

    @staticmethod
    def get_general_score(t):
        return sum(map(lambda x: x.score, t))/len(t)


