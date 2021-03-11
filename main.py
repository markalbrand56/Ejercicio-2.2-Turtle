# Ejercicio 2 parte 2
# Autor Mark Albrand
# CoAutor: Alejandro Azurdia
# Fecha: 6-03-2021
# Programa para dibujar una jirafa a base de figuras geométricas

from turtle import *


# Módulo 1: Figuras básicas

def triangulo_equilatero(base):  # Inicia en el lado inferior
    fillcolor("#61210B")
    begin_fill()

    for i in range(3):
        forward(base)
        left(120)

    end_fill()


def cuadrado(base, color_relleno):  # Inicia en el lado inferior
    fillcolor(color_relleno)
    begin_fill()

    for i in range(4):
        forward(base)
        left(90)

    end_fill()


def rombo_regular(base):  # Inicia en medio de la figura. Dos triángulos equiláteros
    fillcolor("#FFBF00")
    begin_fill()

    left(120)
    forward(base)
    left(120)
    forward(base)
    left(60)
    forward(base)
    left(120)
    forward(base)

    end_fill()


def rombo_extendido(lado, color_relleno):  # Inicia en la esquina inferior. Dos triangulos isóceles. Posición Vertical
    fillcolor(color_relleno)
    begin_fill()

    left(76)
    forward(lado)

    left(29)
    forward(lado)

    left(76 * 2)
    forward(lado)

    left(29)
    forward(lado)

    left(90)

    end_fill()


def hexagono(base):  # Inicia en el lado inferior
    fillcolor("#FFBF00")
    begin_fill()

    for i in range(6):
        forward(base)
        left(60)

    end_fill()


# ---------------------------------------------------------------------------------------------------------
# Módulo 2: Partes del cuerpo

def piernas(base):  # 2 piernas, 3 Cuadrados c/u, separados por la longitud de un cuadrado
    cuadrado(base, color_relleno="#61210B")  # Asignación de color para mantener el patrón

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="#FFBF00")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="#61210B")
    penup()
    right(90)
    forward(base * 2)
    left(90)
    forward(base * 2)
    pendown()

    cuadrado(base, color_relleno="#FFBF00")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="#61210B")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="#FFBF00")


def cola(base):  # Se mueve a la posición donde se usa el rombo extendido para hacer la cola
    penup()
    lt(90)
    fd(base)
    rt(90)
    fd(base)

    lt(60)
    fd(base)

    rt(226)

    pendown()
    rombo_extendido(base, "#61210B")

    penup()
    lt(30)
    fd(base)
    rt(60)
    fd(base)
    lt(180)
    pendown()


def torso(base):  # dos hexágonos regulares (amarillos) y dos triángulos (cafes)

    hexagono(base)

    bk(base)

    triangulo_equilatero(base)

    lt(60)
    fd(base * 2)
    rt(240)

    triangulo_equilatero(base)

    fd(base)

    hexagono(base)


def cuello(base):  # tres rombos no regulares (dos cafes, uno amarillo) y dos rombos regulares (amarillos)

    fd(base)
    lt(60)
    fd(base)
    lt(104)

    rombo_extendido(base, "#61210B")

    lt(90)
    fd(base)
    rt(29)
    fd(base)
    rt(60)

    rombo_regular(base)

    lt(60)
    fd(base)
    lt(120)
    fd(base)
    lt(104)

    rombo_extendido(base, "#61210B")

    lt(90)
    fd(base)
    rt(29)
    fd(base)
    rt(60)

    rombo_regular(base)

    lt(60)
    fd(base)
    lt(120)
    fd(base)
    lt(104)

    rombo_extendido(base, "#FFBF00")


def cabeza(base):  # Dos rombos no regulares (amarillos) y un triángulo equilatero (cafe)

    lt(90)
    triangulo_equilatero(base)
    rt(16)
    rombo_extendido(base, "#FFBF00")

    lt(60)
    fd(base)
    lt(30)
    fd(base)
    lt(102)

    rombo_extendido(base, "#FFBF00")


# --------------------------------------------------------------------------------------------------------------
# INICIO PROGRAMA PRINCIPAL
window = Screen()
window.bgcolor("white")
window.title("Jirafa")
speed("fastest")
base_de_figuras = 40

piernas(base_de_figuras)
cola(base_de_figuras)
torso(base_de_figuras)
cuello(base_de_figuras)
cabeza(base_de_figuras)

window.exitonclick()
