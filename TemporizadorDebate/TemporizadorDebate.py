# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:19:23 2023

@author: MrWenas
"""

def readValuesFromFile(list):
    turnos = open("nombres.txt", "r")
    for nombre in turnos:
        #print(nombre)
        list.append(nombre.replace("\n",""))
        #print("----------------")
#EndOf: readValuesFromFile

listaNombres = []
readValuesFromFile(listaNombres)
print(listaNombres)