#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Copyright 2013-2017 Recursos Python
#   www.recursospython.com
#
from functools import partial
import atexit
import os
import keyboard
MAP = {
    "space": " ",
    "\r": "\n"
}
maxeo=[]
Q = 0
W = 0
E = 0
R = 0
flag=False


# Ubicación y nombre del archivo que guarda las teclas presionadas.
FILE_NAME = "keys.txt"
# Determina si el archivo de salida es limpiado cada vez que se
# inicia el programa.
print('Press and release your desired shortcut: ')
shortcut = "ctrl+q"
shortcut1 = "ctrl+w"
shortcut2 = "ctrl+e"
shortcut3 = "ctrl+r"
#print('Shortcut selected:', shortcut)

def on_triggered():
	maxeo.append("q")
def on_triggered1():
	maxeo.append("w")
def on_triggered2():
	maxeo.append("e")
def on_triggered3():
	maxeo.append("r")
   # print("Triggered!")
keyboard.add_hotkey(shortcut, on_triggered)
keyboard.add_hotkey(shortcut1, on_triggered1)
keyboard.add_hotkey(shortcut2, on_triggered2)
keyboard.add_hotkey(shortcut3, on_triggered3)
CLEAR_ON_STARTUP = True
# Tecla para terminar el programa o None para no utilizar ninguna tecla.
TERMINATE_KEY = "esc"
def callback(output, is_down, event):
	#Contadores especificos para TiltLord
    global Q
    global W
    global E
    global R

    if event.event_type in ("up", "down"):
        key = MAP.get(event.name, event.name)
        modifier = len(key) > 1
        # Capturar únicamente los modificadores cuando están siendo
        # presionados.
        if not modifier and event.event_type == "down":
            return
        # Evitar escribir múltiples veces la misma tecla si está
        # siendo presionada.
        if modifier:
            if event.event_type == "down":
                if is_down.get(key, False):
                    return
                else:
                    is_down[key] = True
            elif event.event_type == "up":
                is_down[key] = False
            # Indicar si está siendo presionado.
            key = " [{} ({})] ".format(key, event.event_type)
        elif key == "\r":
            # Salto de línea.
            key = "\n"
      '''  if key=="q":
            Q+=1
        elif key=="w":
            W+=1
        elif key=="e":
            E+=1
        elif key=="r":
            R+=1'''

        # Escribir la tecla al archivo de salida.
       # output.write(key)
        # Forzar escritura.
       # output.flush()
def onexit(output):'''
    output.write("q= ")
    output.write(str(Q))
    output.write("\n")
    output.flush()
    output.write("w= ")
    output.write(str(W))
    output.write("\n")
    output.flush()
    output.write("e= ")
    output.write(str(E))
    output.write("\n")
    output.flush()
    output.write("r= ")
    output.write(str(R))
    output.write("\n")
    output.write("El orden en el que se realizaron los aumentos de nivel fue: \n")'''
    output.write((str)maxeo.count(q))
    output.write((str)maxeo.count(w))
    output.write((str)maxeo.count(e))
    output.write((str)maxeo.count(r))

    '''for x in maxeo:
        output.write(x)'''
    output.write((str)maxeo.index(q))
    output.write((str)maxeo.index(w))
    output.write((str)maxeo.index(e))
    output.write((str)maxeo.index(r))
    output.flush()
    output.close()
def main():
    # Borrar el archivo previo.
    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    # Indica si una tecla está siendo presionada.
    is_down = {}
    
    # Archivo de salida.
    output = open(FILE_NAME, "a")
    
    # Cerrar el archivo al terminar el programa.
    atexit.register(onexit, output)
    
    # Instalar el registrador de teclas.
    keyboard.hook(partial(callback, output, is_down))
    keyboard.wait(TERMINATE_KEY)
if __name__ == "__main__":
    main()
