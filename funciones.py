from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math

def lectura(archivo, lista):
    f = open("silabas.txt", "r")
    silabas = []
    lineas = f.readlines()
    for linea in lineas:
        silabas.append(int(linea))
    print(silabas)



def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    pass


def nuevaSilaba(silabas):
    pass

def quitar(candidata, silabasEnPantalla, posiciones):
    pass

def dameSilabas(candidata):
    pass


def esValida(candidata, silabasEnPantalla, lemario):
    pass

def Puntos(candidata):
        pass

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    pass
