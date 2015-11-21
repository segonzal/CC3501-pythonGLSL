__author__ = 'mllorens'
import numpy

class Cube:
    def __init__(self, point_1, point_2, color):
        self.color = color
        self.vertex_a = point_1
        self.vertex_b = point_2
        self.vertex_array = None
        self.create_cube()

    def create_cube(self):
        array = numpy.zeros(36, [("position", numpy.float32, 3),
                                 ("color", numpy.float32, 4),
                                 ("normal", numpy.float32,3)])
        array["position"] = [(self.vertex_a[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_a[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_a[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_b[1], self.vertex_b[2]),
                             (self.vertex_a[0], self.vertex_a[1], self.vertex_b[2]),
                             (self.vertex_b[0], self.vertex_a[1], self.vertex_b[2])]
        array["color"][:] = self.color
        array["normal"][0: 6] = (+1.0,  0.0,  0.0)
        array["normal"][6:12] = (-1.0,  0.0,  0.0)
        array["normal"][12:18] = (0.0, +1.0,  0.0)
        array["normal"][18:24] = (0.0, -1.0,  0.0)
        array["normal"][24:30] = (0.0,  0.0, +1.0)
        array["normal"][30:36] = (0.0,  0.0, -1.0)

        self.vertex_array = array

    def get_vertex_array(self):
        return self.vertex_array

    def get_length(self):
        return len(self.vertex_array)

