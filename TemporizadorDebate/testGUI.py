#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from TemporizadorDebate import contadorTurnos

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 

class Aplicacion():
    def __init__(self):
        self.back = contadorTurnos(30)
        self.raiz = Tk()
        self.raiz.geometry('300x200')
        self.raiz.configure(bg = 'gray')
        self.raiz.title('Reunión Junta')
        
        self.newName = StringVar()
        self.current_name_list = StringVar()
        self.remaining_time_str = StringVar(value = "00:00")
        
        self.name_list = ttk.Label(self.raiz, textvariable=self.current_name_list, padding=(5,5))
        self.remaining_time = ttk.Label(self.raiz, textvariable=self.remaining_time_str, padding=(5,5))
        self.name_entry = ttk.Entry(self.raiz, textvariable=self.newName, width=30)
        self.añadir_usuario = ttk.Button(self.raiz, text="Añadir", padding=(5,5), command=self.aceptar)
        
        self.name_list.grid(column=0, row=0, rowspan=5)
        self.remaining_time.grid(column=1, row=0, rowspan=3)
        self.name_entry.grid(column=1, row=4, rowspan=1)
        self.añadir_usuario.grid(column=1, row=5)
        
        self.raiz.after(500, self.updateRemainingTime)
        self.raiz.mainloop()

    def aceptar(self):
        #print(self.newName)
        self.back.addSpeaker(self.newName.get())
        self.newName.set("")
        self.current_name_list.set(self.back.getPendingSpeakersStr())
        self.back.update()
        
    def updateRemainingTime(self):
        self.back.update()
        self.remaining_time_str.set(self.back.getRemainingTimeStr())
        self.current_name_list.set(self.back.getPendingSpeakersStr())
        self.raiz.after(500, self.updateRemainingTime)
# Define la función main() que es en realidad la que indica 
# el comienzo del programa. Dentro de ella se crea el objeto 
# aplicación 'mi_app' basado en la clase 'Aplicación':

def main():
    mi_app = Aplicacion()
    print("Patata")
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':
    main()