from AhorcadoApp import AhorcadoApp
import tkinter as tk
import pyautogui
import time


def main():

    app = AhorcadoApp()
    app.root.lift()

    palabra = "PALABRA"

    seleccionar(app, app.palabraInput,1)
    
    for i, char in enumerate(palabra):
        escribir(app, char, i+1)

    ejecutar(app, app.startButton, 9)

    seleccionar(app, app.letraInput,10)

    for i, char in enumerate(palabra):
        escribir(app,char,11+(i*2))
        ejecutar(app, app.adivinarLetraButton, 12+(i*2))

    app.loop()

def escribir(app, char, delay):
    app.root.after(delay * 1000, lambda char=char: pyautogui.press(char))

def ejecutar(app, objeto, delay):
    app.root.after(delay * 1000, objeto.invoke)

def seleccionar(app, objeto, delay):
    app.root.after(delay * 1000, objeto.focus_set)



if __name__ == "__main__":
    main()

