# Ejercicio 2 parte 2
# Autor Mark Albrand
# CoAutor: Alejandro Azurdia
# Fecha: 6-03-2021
# Programa para dibujar una jirafa a base de figuras geométricas

from turtle import *


# Módulo 1: Figuras básicas

def triangulo_equilatero(base):  # Inicia en el lado inferior
    fillcolor("brown")
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

    end_fill()

    left(76)


def hexagono(base):  # Inicia en el lado inferior
    fillcolor("yellow")
    begin_fill()

    for i in range(6):
        forward(base)
        left(60)

    end_fill()


# Módulo 2: Partes del cuerpo

def piernas(base):  # 2 piernas, 3 Cuadrados c/u, separados por la longitud de un cuadrado
    cuadrado(base, color_relleno="brown")  # Asignación de color para mantener el patrón

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="yellow")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="brown")
    penup()
    right(90)
    forward(base * 2)
    left(90)
    forward(base * 2)
    pendown()

    cuadrado(base, color_relleno="yellow")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="brown")

    left(90)
    forward(base)
    right(90)

    cuadrado(base, color_relleno="yellow")


def cuerpo(base):  # Dos hexágonos, en el espacio entre ellos hay triángilos equiláteros
    hexagono(base)

    forward(base)
    triangulo_equilatero(base)

    forward(base)
    hexagono(base)

    left(120)
    forward(base * 2)
    right(120)
    forward(base)
    right(180)
    triangulo_equilatero(base)

    # Cola

    left(180)
    forward(base)
    right(60)
    forward(base)
    right(76 + 29)
    rombo_extendido(base, color_relleno="yellow")

# INICIO PROGRAMA PRINCIPAL
window = Screen()
window.bgcolor("white")
window.title("Jirafa")

base_de_figuras = 50

# rombo_extendido(50, color_relleno="brown") # Ejemplo para llamar funciones

# cuerpo(100) # Ejemplo para llamar funciones
piernas(base_de_figuras)

window.exitonclick()
