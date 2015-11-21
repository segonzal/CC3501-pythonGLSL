import sys

from Controller import *
from View import *
from Model import *
from Shader import *

WIDTH = 640;
HEIGHT = 480

# Con fines pedagogicos vamos a forzar a este metodo a seguir al pie de la
# letra el MVC y el ciclo mainloop
def main(argc,argv):
    # inicializar subsistemas
    # son las cosas minimas necesarias para crear la ventana
    c = Controller()
    v = View((WIDTH,HEIGHT),(90.0, 0.1, 100.0))
    m = Model()

    # configurar la ventana
    v.init_GL((0.0, 0.5, 0.5, 1.0))
    # Creamos el Shader y se lo entregamos a la vista
    shader_program = Shader("basic_shader")
    shader_program.compile()
    v.useShader(shader_program)

    run = True
    while run:
        # actualizar subsistemas
        c.update()
        m.update()
        v.update()

        run = c.check_close()

    shader_program.delete()

    # cerrar subsistemas
    c.close()
    m.close()
    v.close()

if __name__ == '__main__':
    main(len(sys.argv),sys.argv)
