import unittest
from Ahorcado import Ahorcado


class Test_Ahorcado(unittest.TestCase):

    def test_letra_correcta(self):
        "Testeo de letra correcta"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        self.assertEqual(juego.pruebaLetra("A"), "CORRECTA", msg="{0}, {1}")

    def test_letra_incorrecta(self):
        "Testeo de letra incorrecta"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        self.assertEqual(juego.pruebaLetra("C"), "INCORRECTA", msg="{0}, {1}")

    def test_palabra_correcta(self):
        "Testeo de palabra correcta"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        self.assertEqual(juego.verificarPalabra(palabra), "GANASTE", msg="{0}, {1}")

    def test_palabra_incorrecta(self):
        "Testeo de palabra incorrecta"
        palabra = "PALABRA"
        palabraErronea = "MANZANA"
        juego = Ahorcado(palabra)
        self.assertEqual(
            juego.verificarPalabra(palabraErronea), "PERDISTE", msg="{0}, {1}"
        )

    def test_resta_vida(self):
        "Testeo de restar vida"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.restarVida()
        self.assertEqual(juego.vidas, 5, msg="{0}, {1}")

    def test_definir_palabra_inicio(self):
        "Testeo de definicion de palabra inicial"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        self.assertEqual(palabra, juego.getPalabra(), msg="{0}, {1}")

    def test_acumular_letras_usadas(self):
        "Testeo de letras usadas"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        letraTest = "B"
        juego.pruebaLetra(letraTest)
        self.assertEqual(juego.fueUsada(letraTest), True, msg="{0}, {1}")

    def test_mostrar_largo_palabra(self):
        "Testeo de largo de palabra correcto"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        self.assertEqual(juego.getPalabraEscondida(), "_ _ _ _ _ _ _", msg="{0}, {1}")

    def test_mostrar_letra_correcta_en_lugar(self):
        "Testeo de mostrar letras adivinadas"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.pruebaLetra("A")
        self.assertEqual(juego.getPalabraEscondida(), "_ A _ A _ _ A", msg="{0}, {1}")

    def test_letra_ya_usada(self):
        "Testeo de letras ya utilizadas"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.pruebaLetra("A")
        self.assertEqual(juego.pruebaLetra("A"), "USADA", msg="{0}, {1}")

    def test_perder_por_vidas(self):
        "Testeo de perder juego por vidas"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.vidas = 0
        self.assertEqual(juego.pruebaLetra("Z"), "PERDISTE", msg="{0}, {1}")

    def test_ganar_por_letra(self):
        "Testeo de ganar juego adivinando letras"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.palabraescondida = "_ A L A B R A"
        self.assertEqual(juego.pruebaLetra("P"), "GANASTE", msg="{0}, {1}")

    def test_mostrar_letras_usadas(self):
        "Testeo de mostrar las letras ya utilizadas"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.pruebaLetra("S")
        juego.pruebaLetra("A")
        self.assertEqual(juego.getLetrasUsadas(), ["S", "A"], msg="{0}, {1}")

    def test_mostrar_letras_usadas_repetidas(self):
        "Testeo de mostrar las letras utilizadas y que no se repitan"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.pruebaLetra("S")
        juego.pruebaLetra("A")
        juego.pruebaLetra("S")
        self.assertEqual(juego.getLetrasUsadas(), ["S", "A"], msg="{0}, {1}")

    def test_resetear_juego(self):
        "Testeo de resetear juego completo"
        palabra = "PALABRA"
        juego = Ahorcado(palabra)
        juego.pruebaLetra("S")
        juego.pruebaLetra("A")
        juego.pruebaLetra("S")
        juego.reset()
        self.assertEqual(juego.getPalabra(), "", msg="{0}, {1}")
        self.assertEqual(juego.getPalabraEscondida(), "", msg="{0}, {1}")
        self.assertEqual(juego.getVidas(), 6, msg="{0}, {1}")
        self.assertEqual(juego.getLetrasUsadas(), [], msg="{0}, {1}")


if __name__ == "__main__":
    unittest.main()
