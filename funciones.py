from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math

def lectura(archivo, lista):
    lineas = archivo.readlines()
    for linea in lineas:
        lista.append(linea)


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    pass

def nuevaSilaba(silabas):
    size = len(silabas)
    posicionAzarosa = random.randint(0,size - 1)
    silabaElegida = silabas[posicionAzarosa]
    return silabaElegida

def quitar(candidata, silabasEnPantalla, posiciones):
    pass

# def dameSilabas(candidata):
#     vocales = ["a","e","i","o","u"]
#     for i in candidata:
#


def esValida(candidata, silabasEnPantalla, lemario):
    pass

def Puntos(candidata):
        pass

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    pass
