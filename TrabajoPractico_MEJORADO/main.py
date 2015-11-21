import sys

from Controller import *
from View import *
from Model import *

WIDTH = 640;
HEIGHT = 480

# Con fines pedagogicos vamos a forzar a este metodo a seguir al pie de la
# letra el MVC y el ciclo mainloop
def main(argc,argv):
    # inicializar subsistemas
    # son las cosas minimas necesarias para crear la ventana
    c = Controller()
    v = View(WIDTH,HEIGHT)
    m = Model()

    # configurar la ventana
    v.init_GL((0.0, 0.5, 0.5, 1.0))


    run = True
    while run:
        # actualizar subsistemas
        c.update()
        m.update()
        v.update()

        run = c.check_close()

    # cerrar subsistemas
    c.close()
    m.close()
    v.close()

if __name__ == '__main__':
    main(len(sys.argv),sys.argv)
