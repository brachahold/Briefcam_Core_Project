from Tester.circle2d import Circle2D
from Tester.line2d import Line2D
# from Tester.line3d import Line3D
# from Tester.plane3d import Plane3D


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
