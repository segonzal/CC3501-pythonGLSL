#
# Controller
#

import pygame
from pygame.locals import *
import sys


class Controller:
    def __init__(self):
        pygame.init()
        self.close_requested = False
        self.last_t = pygame.time.get_ticks()

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.close_requested = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.close_requested = True
        new_t = pygame.time.get_ticks()
        dt = new_t - self.last_t
        self.last_t = new_t
        return dt

    def close(self):
        pygame.quit()
        sys.exit()

    def check_close(self):
        return not self.close_requested
