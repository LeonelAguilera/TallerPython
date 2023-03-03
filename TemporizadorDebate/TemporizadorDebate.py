# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:19:23 2023

@author: MrWenas
"""

import time
from datetime import datetime as dt
from datetime import timedelta as td

def readValuesFromFile(list):
    turnos = open("nombres.txt", "r")
    for nombre in turnos:
        #print(nombre)
        list.append(nombre.replace("\n",""))
        #print("----------------")
#EndOf: readValuesFromFile

def getTimeDeltaStr(timedelta):
    s = timedelta.total_seconds()
    minutes, seconds = divmod(s, 60)
    return '{:02}:{:02}'.format(int(minutes), int(seconds))
#EndOf: printTimeDelta


class contadorTurnos:
    def __init__(self, tiempodeturno):
        self.tiempodeturno = tiempodeturno
        self.listaNombres = []
        #readValuesFromFile(self.listaNombres)
        self.currentIndex = 0
        self.currentTime = dt.now()
        self.turno = ""
        self.endTime = self.currentTime
        self.cancel = False
    
    def update(self):
        self.currentTime = dt.now()
        #Comprobar si debe ocurrir cambio de turno
        print(self.currentTime >= self.endTime)
        print(self.cancel)
        print((self.currentTime >= self.endTime) or self.cancel)
        print(self.currentIndex)
        print(len(self.listaNombres))
        if (self.currentTime >= self.endTime or self.cancel) and self.currentIndex < len(self.listaNombres):
            self.turno = self.listaNombres[self.currentIndex]
            self.currentIndex += 1
            self.cancel = False
            self.endTime = self.currentTime + td(seconds=self.tiempodeturno)
        #time.sleep(1)
        #delta = endTime-currentTime
        #print(turno + ": " + getTimeDeltaStr(delta))
        #EndOf: Comprobar si debe ocurrir cambio de turno
    
    def addSpeaker(self, speaker_name):
        self.listaNombres.append(speaker_name)
        
    def getPendingSpeakers(self):
        return self.listaNombres[self.currentIndex-1:]
    
    def getPendingSpeakersStr(self):
        namelist = ""
        for name in self.getPendingSpeakers():
            namelist += name + "\n"
        return namelist
    
    def getRemainingTimeStr(self):
        if self.endTime <= dt.now():
            return "00:00"
        return getTimeDeltaStr(self.endTime-dt.now())