__author__ = 'mllorens'
from OpenGL.GL import *


def compile_shader(vertex,fragment):
    # request program and shader slots from GPU
    program = glCreateProgram()
    vertexShader = glCreateShader(GL_VERTEX_SHADER)
    fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)

    # set shaders source
    glShaderSource(vertexShader,vertex)
    glShaderSource(fragmentShader,fragment)

    # compile shaders
    glCompileShader(vertexShader)
    glCompileShader(fragmentShader)

    # attach shader objects to the program
    glAttachShader(program,vertexShader)
    glAttachShader(program,fragmentShader)

    # build program
    glLinkProgram(program)

    # get rid of shaders (needed no more)
    glDetachShader(program,vertexShader)
    glDetachShader(program,fragmentShader)

    return program


def attribute(loc, _size, _type, normalized, stride, offset):
    """
    attribute(loc,size,type,normalized,stride,offset)

    loc: Specifies the index of the generic vertex attribute to be modified.
    size: Specifies the number of components per generic vertex attribute.
          Must be 1, 2, 3, 4.
    type: Specifies the data type of each component in the array.
          GL_BYTE, GL_UNSIGNED_BYTE, GL_SHORT, GL_UNSIGNED_SHORT, GL_INT,
          GL_UNSIGNED_INT, GL_FLOAT and GL_DOUBLE.
    normalized: Specifies whether fixed-point data values should be normalized (True) or
          converted directly as fixed-point values (False)
    stride: Specifies the byte offset between consecutive generic vertex attributes.
    offset: Specifies a offset of the first component of the first generic vertex attribute in the
            array in the data store of the buffer currently bound to the GL_ARRAY_BUFFER target.
    """
    # https://www.opengl.org/sdk/docs/man/html/glVertexAttribPointer.xhtml
    glEnableVertexAttribArray(loc)

    glVertexAttribPointer(loc, _size, _type, normalized, stride, ctypes.c_void_p(offset))

    glDisableVertexAttribArray(loc)


def uniform(loc, _type, *value):
    """
    uniform(name,type, value ... )

    loc: Specifies the index of the generic vertex attribute to be modified.
    type: 1f, 2f, 3f, 4f, 1i, 2i, 3i, 4i, 22f, 23f, 24f, 33f, 32f, 34f, 44f, 42f, 43f
    *value:
    For the scalar commands:
        [0][1][2][3] Specifies the new values to be used for the specified uniform variable.
                     ( v0, v1, v2, v3 )
    For the matrix array commands:
        [0] Specifies the number of elements that are to be modified.
            This should be 1 if the targeted uniform variable is not an array, and 1 or more if it is an array.
            ( count )
        [1] Specifies whether to transpose the matrix as the values are loaded into the uniform variable.
            ( transpose )
        [2] Specifies a pointer to an array of count values that will be used to update the specified uniform variable.
            ( value )
    """
    # http://pyopengl.sourceforge.net/documentation/manual-3.0/glUniform.html

    if _type == '1f':
        glUniform1f(loc, value[0])
    elif _type == '2f':
        glUniform2f(loc, value[0], value[1])
    elif _type == '3f':
        glUniform3f(loc, value[0], value[1], value[2])
    elif _type == '4f':
        glUniform4f(loc, value[0], value[1], value[2], value[3])

    elif _type == '1i':
        glUniform1i(loc, value[0])
    elif _type == '2i':
        glUniform2i(loc, value[0], value[1])
    elif _type == '3i':
        glUniform2i(loc, value[0], value[1], value[2])
    elif _type == '4i':
        glUniform2i(loc, value[0], value[1], value[2], value[3])

    # for matrices:  location , count , transpose , value
    elif _type == '22f':
        glUniformMatrix2fv(loc, value[0], value[1], value[2])
    elif _type == '23f':
        glUniformMatrix2x3fv(loc, value[0], value[1], value[2])
    elif _type == '24f':
        glUniformMatrix2x4fv(loc, value[0], value[1], value[2])
    elif _type == '33f':
        glUniformMatrix3fv(loc, value[0], value[1], value[2])
    elif _type == '32f':
        glUniformMatrix3x2fv(loc, value[0], value[1], value[2])
    elif _type == '34f':
        glUniformMatrix3x4fv(loc, value[0], value[1], value[2])
    elif _type == '44f':
        glUniformMatrix4fv(loc, value[0], value[1], value[2])
    elif _type == '42f':
        glUniformMatrix4x2fv(loc, value[0], value[1], value[2])
    elif _type == '43f':
        glUniformMatrix4x3fv(loc, value[0], value[1], value[2])

    else:
        raise ValueError("Unknown type " + _type)


def asign_attributes(vertex, _buffer, position_loc, color_loc, normal_loc):
    glBindBuffer(GL_ARRAY_BUFFER, _buffer)
    glBufferData(GL_ARRAY_BUFFER, vertex, GL_DYNAMIC_DRAW)

    # The size in bytes of a FLOAT is 4 bytes
    stride = 4 * (3+4+3)
    offset = 0
    attribute(position_loc, 3, GL_FLOAT, False, stride, offset)
    offset = 4*3
    attribute(color_loc, 3, GL_FLOAT, False, stride, offset)
    offset = 4*(3+4)
    attribute(normal_loc, 3, GL_FLOAT, False, stride, offset)