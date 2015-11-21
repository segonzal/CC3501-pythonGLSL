from OpenGL.GL import *

# Este metodo regresa el contenido de un archivo en un string.
def dumpfile(filename):
    file = open(filename,'r')
    data = "".join([line for line in file])
    file.close()
    return data

# Esta funcion utilitaria de shaders nos permite conocer errores de compilacion
# de los shaders y facilitar el debugging
def createShader(code,type):
    # Creamos un nuevo shader del tipo especificado: VERTEX o FRAGMENT
    shader = glCreateShader(type)
    # Indicamos cual es su codigo fuente
    glShaderSource(shader,code)
    # Compilamos el shader
    glCompileShader(shader)

    # Chequeamos en caso de errores
    result = glGetShaderiv(shader,GL_COMPILE_STATUS)
    if (result!=1):
        # Podemos saber que shader fallo
        print "Couldn't compile",
        if type == GL_VERTEX_SHADER:
            print "vertex shader."
        elif type == GL_FRAGMENT_SHADER:
            print "fragment shader."
        else:
            print ", shader type not recognized."
        # Podemos conocer mas detalles del error
        print glGetShaderInfoLog(shader)
        glDeleteShader(shader)
        exit(1)
    return shader

class Shader:
    def __init__(self,filename):
        # Suponemos que los shaders a usar se llaman <filename>.vs y <filename>.fs
        # (VERTEX, FRAGMENT)
        self.code = (dumpfile(filename+".vs"),dumpfile(filename+".fs"))
        self.program = None

    def use(self):
		glUseProgram(self.program)

    def compile(self):
        vertex,fragment = self.code
        # pedimos espacio a la CPU para el programa
        self.program = glCreateProgram()

        # Creamos los vertex y fragment shaders
        vshader = createShader(vertex,GL_VERTEX_SHADER)
        fshader = createShader(fragment,GL_FRAGMENT_SHADER)

        # Hacemos el link entre nuestro programa y los shaders que usaremos
        glAttachShader(self.program,vshader)
        glAttachShader(self.program,fshader)

        # Une el programa creando los ejecutables
        glLinkProgram(self.program)

        # chequeamos que la union fue exitosa
        result = glGetProgramiv(self.program,GL_LINK_STATUS)
        if (result != GL_TRUE):
            print "Couldn't link program"
            glGetProgramInfoLog(self.program)
            glDeleteShader(vshader)
            glDeleteShader(fshader)
            glDeleteProgram(self.program)
            exit(1)

        # Podemos desacernos de estos.
        glDetachShader(self.program,vshader)
        glDetachShader(self.program,fshader)
