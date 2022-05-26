from Tester.geo_tester import GeoTester
import matplotlib.pyplot as plt

class Circle2D(GeoTester):
    def __init__(self, gt, es):
        super().__init__([gt.center[0], gt.center[1], gt.radius], es.best_model)

    def get_plt_geo(self):
        return plt.Circle((self.gt[0], self.gt[1]), self.gt[2], color='g', fill=False), plt.Circle((self.es[0], self.es[1]), self.es[2], color='r', fill=False)

    def calc_score(self):
        x_gt, y_gt, r_gt = self.gt
        x_es, y_es, r_es = self.es
        x_dis = abs(x_gt - x_es)
        y_dis = abs(y_gt - y_es)
        r_dis = abs(r_gt - r_es)
        self.score = 0.7 * r_dis + 0.15 * x_dis + 0.15 * y_dis
