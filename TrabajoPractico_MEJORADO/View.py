#
# View
#

import pygame
from pygame.locals import *

class View:
    def __init__(self,width,height):
        self.screen = pygame.display.set_mode((width,height),OPENGL | DOUBLEBUF,24)
        pygame.mouse.set_visible(False)

    def update(self):
        pass

    def close(self):
        pass

    def init_GL(self,color):
        pass
