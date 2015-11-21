#
# View
#

import math
import pygame
from pygame.locals import *
from pygame.locals import *
from OpenGL.GL import *

def perspectiveGL(fovy, aspect, near, far):
    fH = math.tan(fovy/360.0) * math.pi * near
    fW = fH * aspect
    glFrustum(-fW, fW, -fH, fH, near, far)

class View:
    def __init__(self,(width,height),(fovy,near,far)):
        self.screen = pygame.display.set_mode((width,height),OPENGL | DOUBLEBUF)
        self.fovy_near_far = (fovy,near,far)
        self.shader_program = None
        self.model = None

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.model is not None:
            pass

        pygame.display.flip()

    def close(self):
        pass

    def init_GL(self,color):
        print 'OpenGL version: %s' % (glGetString(GL_VERSION))
        print 'GLSL version: %s' % (glGetString(GL_SHADING_LANGUAGE_VERSION))
        glClearColor(color[0],color[1],color[2],color[3])
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        self.reshape()

    def reshape(self):
        (fovy,near,far) = self.fovy_near_far
        (w,h) = self.screen.get_size()
        glViewport(0,0,w,h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        perspectiveGL(fovy,(w*1.0)/h,near,far)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def useShader(self,shader_program):
        self.shader_program = shader_program
        self.shader_program.use()
