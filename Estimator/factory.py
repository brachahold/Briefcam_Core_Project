from Estimator.circle2d import Circle2D
from Estimator.line2d import Line2D

class Factory:
    def __init__(self):
        self.__classes = {
            "Circle2D": Circle2D,
            "Line2D": Line2D,
            # "Line3D": Line3D,
            # "Plane3D": Plane3D
        }

    def creation(self, name, *args):
        return self.__classes.get(name)(*args)