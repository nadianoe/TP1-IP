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
    size = len(silabas)
    posicionAzarosa = random.randint(0,size - 1)
    silabaElegida = silabas[posicionAzarosa]
    return silabaElegida


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
