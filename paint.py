"""
Juego: Paint
Programador 1: Josué Fuentes
Programador 2: Alex Flores
Fecha: 10 / mayo / 2022
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    #Partimos de los 360 grados que tiene un circulo y lo dividimos entre 10 para hacer una equivalencia
    for count in range(36):
        #Se limita la distancia de la linea
        forward(10)
        #De los 100 al dividirlo, lo marcamos a 10 para la equivalencia
        left(10)


def rectangle(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()  
    begin_fill()

    #Se limitan en total 4 lados, divididos en 2 por el eje x y el y
    for count in range(2):
        #Se marca el lado x del rectángulo
        forward(start.x)
        left(90)
        #Se marca el lado y del rectángulo
        forward(end.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    #Se limita un rango de 3 grios (los lados)
    for count in range(3):
        forward(end.x - start.x)
        #Su ángulo de giro sera de 120 para formar tríangulo equilatero
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Se agrega el color naranja
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
