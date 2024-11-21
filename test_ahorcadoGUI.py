import pyautogui as pag
import subprocess as sp
import unittest
import time
import os
import signal


class Test_AhorcadoApp(unittest.TestCase):

    def setUp(self):
        self.process = sp.Popen(['python', 'AhorcadoApp.py'], stdout=sp.PIPE, stdder=sp.PIPE)
        time.sleep(2)
    
    def tearDown(self):
        if self.process.poll() is None:
            os.kill(self.process.pid, signal.SIGTERM)
            time.sleep(1)

    def test_ganar_letra(self):
        textInput = pag.locateOnScreen('textInput.png')
        pag.click(pag.center(textInput))
        pag.write("PALABRA")

        startButton = pag.locateOnScreen('empezar_juego.png')
        pag.click(pag.center(startButton))

        letraInput = pag.locateOnScreen("letra_input.png")
        pag.click(pag.center(letraInput))
        pag.write("A")

        letraButton = pag.locateOnScreen("adivinar_letra.png")
        pag.click(pag.center(letraButton))

        pag.click(pag.center(letraInput))
        pag.write("P")
        pag.click(pag.center(letraButton))

        pag.click(pag.center(letraInput))
        pag.write("L")
        pag.click(pag.center(letraButton))

        pag.click(pag.center(letraInput))
        pag.write("B")
        pag.click(pag.center(letraButton))

        pag.click(pag.center(letraInput))
        pag.write("R")
        pag.click(pag.center(letraButton))

        ganasteMsg = pag.locateOnScreen("ganaste.png")
        self.assertIsNotNone(ganasteMsg)


if __name__ == '__main__':
    unittest.main()