__author__ = 'mllorens'
from pygame.locals import *
from OpenGL.GL import *
import pygame
from View import WindowGL
import Shaders_Methods
from Model import Cube
import sys


class Main_Controller:
    def __init__(self, width, height, _color, vertex_shader, fragment_shader):
        self.window = WindowGL.WindowGL(width, height, _color)
        self.vertex = vertex_shader
        self.fragment = fragment_shader
        self.program = Shaders_Methods.compile_shader(self.vertex, self.fragment)

        glUseProgram(self.program)
        self.position_loc = 0
        self.color_loc = 1
        self.normal_loc = 2

        glBindAttribLocation(self.program, self.position_loc, "position")
        glBindAttribLocation(self.program, self.color_loc, "color")
        glBindAttribLocation(self.program, self.normal_loc, "normal")

        self.cube = Cube.Cube((-5, -5, -5), (5, 5, 5), (0, 0, 1, 1.0))
        self.buffer = glGenBuffers(1)

        Shaders_Methods.asign_attributes(self.cube.get_vertex_array(),
                                         self.buffer,
                                         0, 1, 2)
        self.uni_loc = glGetUniformLocation(self.program, "lightPos")
        self.uni_col_loc = glGetUniformLocation(self.program, "lightCol")

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        self.window.draw(self.uni_col_loc,
                         self.uni_loc,
                         self.position_loc,
                         self.color_loc,
                         self.normal_loc,
                         self.cube.get_length())
