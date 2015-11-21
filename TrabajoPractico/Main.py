__author__ = 'mllorens'
from Controller import Main_Controller
from Controller import Shaders

controller = Main_Controller.Main_Controller(640,
                                             480,
                                             (0.0, 0.5, 0.5, 1.0),
                                             Shaders.VERTEX,
                                             Shaders.FRAGMENT)
while True:
    controller.update()
