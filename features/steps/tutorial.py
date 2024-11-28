from behave import *
import pyautogui as pag
import subprocess as sp
import pytest
import time
import os
import pygetwindow as gw

def iniciar_aplicacion():
    """Inicia la aplicación antes de cada prueba y verifica que se haya cargado correctamente."""
    print("Iniciando la aplicación...")
    script_path = os.path.abspath("Ahorcado/AhorcadoApp.py")
    
    try:
        # Inicia el proceso
        process = sp.Popen(['python', script_path], stdout=sp.PIPE, stderr=sp.PIPE)
        time.sleep(1)  # Tiempo de espera para cargar la aplicación
        
        # Verifica si la ventana está abierta
        ventana_juego = None
        for ventana in gw.getAllTitles():
            if "Ahorcado" in ventana:
                ventana_juego = ventana
                break
        
        if ventana_juego is None:
            process.terminate()
            print("Error: La ventana del juego no se inició correctamente.")
            return None

        print("Aplicación iniciada correctamente.")
        return process
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        return None

def cerrar_aplicacion(process):
    """Cierra la aplicación después de la prueba."""
    if process:
        process.terminate()
        process.wait()
        print("Aplicación cerrada.")

@given('la palabra es {palabraTest}')
def step_impl(context,palabraTest):
    process = iniciar_aplicacion()
    
    textInput = pag.locateOnScreen("Ahorcado/textInput.png")
    pag.click(pag.center(textInput))
    pag.write(palabraTest)

    startButton = pag.locateOnScreen("Ahorcado/empezar_juego.png")

    pag.click(pag.center(startButton))



@when('jugador ingresa {palabraTest}')
def step_impl(context,palabraTest):
    # Localizar el campo de entrada para la palabra
    palabraInput = pag.locateOnScreen("Ahorcado/palabra_input.png")

    pag.click(pag.center(palabraInput))
    pag.write(palabraTest)

    # Localizar el botón para adivinar la palabra
    adivinarPalabraButton = pag.locateOnScreen("Ahorcado/adivinar_palabra.png")

    pag.click(pag.center(adivinarPalabraButton))

    print(f"El jugador ingresó la palabra: {palabraTest}")
    

@then('se muestra pantalla {mensaje}')
def step_impl(context,mensaje):
    ganasteMsg = pag.locateOnScreen("Ahorcado/ganaste.png")

    assert ganasteMsg is not pag.ImageNotFoundException