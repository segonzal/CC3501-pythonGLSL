__author__ = 'mllorens'
from pygame.locals import *
from OpenGL.GL import *
import pygame
import math
from Controller import Shaders_Methods

class WindowGL:
    def __init__(self, width, height, _color):
        self.width = width
        self.height = height
        self.screen = None
        self.clean_color = _color
        self.init_screen()
        self.reshape()
        self.angle = 0
        self.R = 20
        self.color = 0xffffff

    def perspectiveGL(self, fovy, aspect, near, far):
        fH = math.tan(fovy/360.0) * math.pi * near
        fW = fH * aspect
        glFrustum(-fW, fW, -fH, fH, near, far)

    def init_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height),
                                         OPENGL | DOUBLEBUF,
                                         24)
        pygame.mouse.set_visible(False)
        glClearColor(self.clean_color[0],
                     self.clean_color[1],
                     self.clean_color[2],
                     self.clean_color[3])
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        self.screen = screen



    def reshape(self):
        width, height = self.screen.get_size()

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        self.perspectiveGL(90.0, width/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def draw(self, uni_col_loc, uni_loc, position_loc, color_loc, normal_loc, cube_lenght):
        # DRAW ON SCREEN
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslate(0,0,-20)
        glRotate(-self.angle*10,1,0.5,1)

        # ACTUALIZAMOS CADA UNIFORM CON NUEVOS VALORES

        r = ((self.color) % 10) / 10.0
        g = ((self.color/10) % 10) / 10.0
        b = ((self.color/100) % 10) / 10.0

        Shaders_Methods.uniform(uni_col_loc, '3f', r, g, b)
        Shaders_Methods.uniform(uni_loc, '3f',
                self.R*math.cos(self.angle),
                0, self.R*math.sin(self.angle))

        self.angle += 0.025
        self.color += 0.01
        self.color %= 1000

        glEnableVertexAttribArray(position_loc)
        glEnableVertexAttribArray(color_loc)
        glEnableVertexAttribArray(normal_loc)

        glDrawArrays(GL_TRIANGLES, 0, cube_lenght)

        glDisableVertexAttribArray(position_loc)
        glDisableVertexAttribArray(color_loc)
        glDisableVertexAttribArray(normal_loc)
        pygame.display.flip()
