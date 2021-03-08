# Ejercicio 2 parte 2
# Autor Mark Albrand
# CoAutor: Alejandro Azurdia
# Fecha: 6-03-2021
# Programa para dibujar una jirafa a base de figuras geométricas

from turtle import *


def triangulo_equilatero(base):
    fillcolor("yellow")
    begin_fill()

    for i in range(3):
        forward(base)
        left(120)

    end_fill()


def cuadrado(base, color_relleno):
    fillcolor(color_relleno)
    begin_fill()

    for i in range(4):
        forward(base)
        left(90)

    end_fill()


def rombo_regular(base):  # dos triángulos equiláteros
    fillcolor("yellow")
    begin_fill()

    penup()
    forward(base)
    pendown()

    left(120)
    forward(base)
    left(120)
    forward(base)
    left(60)
    forward(base)
    left(120)
    forward(base)

    end_fill()


def rombo_extendido(lado, color_relleno):  # dos triangulos isóceles
    fillcolor(color_relleno)
    begin_fill()

    left(76)
    forward(lado)

    left(29)
    forward(lado)

    left(76*2)
    forward(lado)

    left(29)
    forward(lado)

    end_fill()


def hexagono(base):
    fillcolor("yellow")
    begin_fill()

    for i in range(6):
        forward(base)
        left(60)

    end_fill()