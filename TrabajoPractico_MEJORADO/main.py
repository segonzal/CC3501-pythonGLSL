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
    #m = Model(Cube((-5,-5,-5),(5,5,5)))
    m = Model(Triangle((5,5,-15),(-5,-5,-15),(5,-5,-15)))

    # configurar la ventana
    v.init_GL((0.0, 0.5, 0.5, 1.0))
    # Creamos el Shader
    shader_program = Shader("basic_shader")
    shader_program.compile()

    # Configuramos las ubicaciones de los uniformes
    shader_program.uniform_location = {
        "lightPos": glGetUniformLocation(shader_program.program, "lightPos"),
        "lightCol": glGetUniformLocation(shader_program.program, "lightCol")
    }
    # Configuramos las ubicaciones de los atributos
    shader_program.bindAttributeLocation({
        "position": 0,
        "color": 1,
        "normal": 2
    })

    # Le entregamos los shaders a la vista para que los use
    v.useShader(shader_program)

    # Le entregamos el modelo a la vista
    v.model = m

    run = True
    while run:
        # actualizar subsistemas
        dt = c.update()
        m.update(dt)
        v.update(dt)

        run = c.check_close()

    shader_program.delete()

    # cerrar subsistemas
    c.close()
    m.close()
    v.close()

if __name__ == '__main__':
    main(len(sys.argv),sys.argv)
