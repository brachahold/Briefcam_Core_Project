from Tester.geo_tester import GeoTester


class Circle2D(GeoTester):
    def __init__(self, gt, es):
        super().__init__([gt.center[0], gt.center[1], gt.radius], es.best_model)

    def calc_score(self):
        x_gt, y_gt, r_gt = self.gt
        x_es, y_es, r_es = self.es
        x_dis = abs(x_gt - x_es)
        y_dis = abs(y_gt - y_es)
        r_dis = abs(r_gt - r_es)
        self.score = 0.7 * r_dis + 0.15 * x_dis + 0.15 * y_dis
