#
# View
#

import math
import pygame
from pygame.locals import *
from pygame.locals import *
from OpenGL.GL import *

LIGHT_COLOR = (1,1,1)
LIGHT_POSITION = (10,10,10)

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
        self.buffer = None
        self.angle = 0

    def update(self,dt):
        # limpiamos la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # recalculamos el angulo para rotar las figuras
        self.angle += 0.0001*dt*360

        # Aplicamos las transformaciones lineales
        glTranslate(0,0,-20)
        glRotate(-self.angle,1,0.5,1)

        if self.model is not None:
            if self.model.has_changed:
                self.shader_program.bindBuffer(self.buffer,self.model)
                self.model.has_changed = False

            # Establecemos los valores de los uniformes
            self.shader_program.setUniform("lightCol",LIGHT_COLOR)
            self.shader_program.setUniform("lightPos",LIGHT_POSITION)

            # Activamos los atributos
            self.shader_program.enableVAA("position")
            self.shader_program.enableVAA("color")
            self.shader_program.enableVAA("normal")

            # Dibujamos el modelo usando triangulos
            glDrawArrays(GL_TRIANGLES, 0, self.model.size)

            # Desactivamos los atributos
            self.shader_program.disableVAA("normal")
            self.shader_program.disableVAA("color")
            self.shader_program.disableVAA("position")

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

        # reservamos un buffer de datos en la tarjeta grafica
        self.buffer = glGenBuffers(1)

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
