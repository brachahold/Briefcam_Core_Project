from Tester.geo_tester import GeoTester
import matplotlib.pyplot as plt


class Line2D(GeoTester):
    def __init__(self, gt, es):
        super().__init__([gt.point[0], gt.point[1], gt.get_slope()], es.best_model)

    def get_plt_geo(self):
        return plt.axline((self.gt[0], self.gt[1]), slope=self.gt[2], color='g'), plt.axline((self.es[0], self.es[1]), slope=self.es[2], color='r')

    def calc_score(self):
        x_gt, y_gt, s_gt = self.gt
        x_es, y_es, s_es = self.es
        y_axis_gt = y_gt - s_gt * x_gt
        x_axis_gt = -y_axis_gt / s_gt
        y_axis_es = y_es - s_es * x_es
        x_axis_es = -y_axis_es / s_es
        x_dis = abs(x_axis_gt - x_axis_es)
        y_dis = abs(y_axis_gt - y_axis_es)
        s_dis = abs(s_gt - s_es)
        self.score = 0.7 * s_dis + 0.15 * x_dis + 0.15 * y_dis
