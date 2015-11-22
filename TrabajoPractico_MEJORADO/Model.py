#
# Model
#

import numpy as np

class Model:
    def __init__(self,figure):
        self.array = None
        self.size = 0
        self.att_sz = (0,0,0)
        self.figure = figure
        self.has_changed = True

    def update(self,dt):
        if self.has_changed:
            self.size = self.figure.size
            (psz,csz,nsz) = self.att_sz = self.figure.att_sz

            array = np.zeros(self.size, [
                ("position", np.float32, psz),
                ("color", np.float32, csz),
                ("normal", np.float32, nsz)])
            array["position"]= self.figure.position
            array["color"] = self.figure.color
            array["normal"] = self.figure.normal
            self.array = array

    def close(self):
        pass

class Triangle:
    def __init__(self,a,b,c):
        self.position = [a,b,c]
        self.color = [(0,0,1,1)]*3
        norm = np.cross(np.array(b)-np.array(a),np.array(c)-np.array(b))
        self.normal = [(norm[0], norm[1], norm[2])]*3
        self.size = 3
        self.att_sz = (3,4,3)

class Cube:
    def __init__(self,a,b):
        self.position = [
            (a[0], a[1], a[2]),(a[0], a[1], b[2]),(a[0], b[1], b[2]),
            (a[0], b[1], b[2]),(a[0], b[1], a[2]),(a[0], a[1], a[2]),

            (b[0], a[1], a[2]),(b[0], b[1], b[2]),(b[0], a[1], b[2]),
            (b[0], b[1], b[2]),(b[0], a[1], a[2]),(b[0], b[1], a[2]),

            (b[0], a[1], a[2]),(b[0], a[1], b[2]),(a[0], a[1], b[2]),
            (a[0], a[1], b[2]),(a[0], a[1], a[2]),(b[0], a[1], a[2]),

            (b[0], b[1], a[2]),(a[0], b[1], b[2]),(b[0], b[1], b[2]),
            (a[0], b[1], b[2]),(b[0], b[1], a[2]),(a[0], b[1], a[2]),

            (a[0], a[1], a[2]),(a[0], b[1], a[2]),(b[0], b[1], a[2]),
            (b[0], b[1], a[2]),(b[0], a[1], a[2]),(a[0], a[1], a[2]),

            (a[0], a[1], b[2]),(b[0], b[1], b[2]),(a[0], b[1], b[2]),
            (b[0], b[1], b[2]),(a[0], a[1], b[2]),(b[0], a[1], b[2])]
        self.color = [(0,0,1,1)]*36
        self.normal = []
        self.normal.extend( [(+1.0,  0.0,  0.0)]*6 )
        self.normal.extend( [(-1.0,  0.0,  0.0)]*6 )
        self.normal.extend( [( 0.0, +1.0,  0.0)]*6 )
        self.normal.extend( [( 0.0, -1.0,  0.0)]*6 )
        self.normal.extend( [( 0.0,  0.0, +1.0)]*6 )
        self.normal.extend( [( 0.0,  0.0, -1.0)]*6 )
        self.size = 36
        self.att_sz = (3,4,3)
