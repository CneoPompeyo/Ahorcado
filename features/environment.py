from behave import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

from Ahorcado import Ahorcado


def esperarElemento(dr, id):
    "Espera a localizar el elemento"
    try:
        wait = WebDriverWait(dr, 5)  # Tiempo máximo de espera: 5 segundos
        elemento = wait.until(EC.element_to_be_clickable((By.ID, id)))
        return elemento
    except StaleElementReferenceException or TimeoutException:
        elemento = WebDriverWait(
            dr,
            timeout=5,
            ignored_exceptions=(TimeoutException, StaleElementReferenceException),
        ).until(EC.presence_of_element_located((By.ID, id)))
        print(f"El botón {id} no se pudo hacer click después de esperar 10 segundos")
        return elemento


def iniciar_aplicacion():
    "inicia la aplicacion"
    print("Iniciando la aplicación...")

    options = Options()
    options.add_argument("--headless")  # Ejecutar Chrome en modo headless
    options.add_argument("--disable-gpu")  # Desactivar la aceleración por GPU
    options.add_argument("--no-sandbox")  # Evitar problemas de sandboxing

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/")

    while driver.execute_script("return document.readyState") != "complete":
        pass

    print("Aplicación iniciada correctamente.")
    return driver


def cerrar_aplicacion(driver):
    "Cierra la aplicación después de la prueba."
    if driver:
        driver.quit()
        print("Aplicación cerrada.")


def palabraInicial(dr, palabraTest):
    "Input de palabra a adivinar"
    input = esperarElemento(dr, "palabra")
    input.click()
    input.send_keys(palabraTest)

    startBoton = esperarElemento(dr, "iniciar")
    startBoton.click()


def adivinaPalabra(dr, palabraTest):
    "Localizar el campo de entrada para la palabra"
    input = esperarElemento(dr, "palabra-completa")
    input.click()
    input.send_keys(palabraTest)

    boton = esperarElemento(dr, "adivina-palabra")
    boton.click()


@fixture
def before_scenario(context, scenario):
    "Iniciar aplicacion antes de cada escenario"
    context.driver = iniciar_aplicacion()


def after_scenario(context, scenario):
    "Cerrar aplicacion luego de cada escenario"
    cerrar_aplicacion(context.driver)


def before_step(context, step):
    "Acciones a realizar antes de cada step"
    dr = context.driver
    if "Reiniciar juego luego de" in context.scenario.name:
        if step.step_type == "given" and "se muestra mensaje" in step.name:
            palabraInicial(dr, "PALABRA")
            if "perder" in context.scenario.name:
                adivinaPalabra(dr, "MANZANA")
            else:
                adivinaPalabra(dr, "PALABRA")
