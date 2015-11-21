#
# Model
#

class Model:
    def __init__(self,generator):
        self.positions = None
        self.normals = None
        self.colors = None
        self.size = 0
        self.generator = generator

    def update(self):
        if self.generator.has_changed():
            self.generator.generate(self)

    def close(self):
        pass

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.changed = True

    def has_changed(self):
        return self.changed

    def generate(self,model):
        self.changed = False
