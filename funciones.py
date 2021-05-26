from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math

#hola 

def lectura(archivo, lista):
    lineas = archivo.readlines()
    for linea in lineas:
        lineaSinSalto= linea[:-1]
        lista.append(lineaSinSalto)
    archivo.close()


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    pass

def nuevaSilaba(silabas):
    size = len(silabas)
    posicionAzarosa = random.randint(0,size - 1)
    silabaElegida = silabas[posicionAzarosa]
    return silabaElegida

def quitar(candidata, silabasEnPantalla, posiciones):
    pass

def obtenerSilabas():
    archivo = open("silabas.txt", "r")
    listaDeSilabas = []
    lineas = archivo.readlines()
    for linea in lineas:
        lineaSinSalto = linea[:-1]
        listaDeSilabas.append(lineaSinSalto)
    archivo.close()
    return listaDeSilabas

def dameSilabas(candidata):
    silabas = obtenerSilabas()
    silabasDeCandidata = []
    while len(candidata) >= 1:

        for i in range(5):
            posibleSilaba = candidata[0:i]
            if silabas.__contains__(posibleSilaba):
                silabasDeCandidata.append(posibleSilaba)
                candidata = candidata.replace(posibleSilaba, "")
                break
            elif len(posibleSilaba) >= 2 and len(candidata) >= 2 and len(silabasDeCandidata) >= 1:
                ultimoIndice = len(silabasDeCandidata) - 1
                ultimoElemento = silabasDeCandidata[ultimoIndice]
                silabasDeCandidata[ultimoIndice] = ultimoElemento + candidata[0]
                candidata = candidata.replace(candidata[0], "")
                break
            elif len(candidata) == 1:
                ultimoIndice = len(silabasDeCandidata) - 1
                ultimoElemento = silabasDeCandidata[ultimoIndice]
                silabasDeCandidata[ultimoIndice] = ultimoElemento + candidata
                candidata = ""
                break

    return silabasDeCandidata

def esValida(candidata, silabasEnPantalla, lemario):
    silabasDeCandidata = dameSilabas(candidata)
    estanTodas = True

    for silaba in silabasDeCandidata:
        estanTodas = estanTodas and silabasEnPantalla.__contains__(silaba)

    esUnaPalabraValida = estanTodas and lemario.__contains__(candidata)
    return esUnaPalabraValida

def Puntos(candidata):
    vocales = ["a","e","i","o","u"]
    letrasDificiles = ["j","k","q","w","x","y","z"]
    puntaje = 0

    for letra in candidata:
        if vocales.__contains__(letra):
            puntaje += 1
        elif letrasDificiles.__contains__(letra):
            puntaje += 5
        else:
            puntaje += 2

    return puntaje

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    puntajeObtenido = 0
    if esValida(candidata,silabasEnPantalla,lemario):
        quitar(candidata,silabasEnPantalla,posiciones)
        puntajeObtenido = Puntos(candidata)
    return puntajeObtenido


