import unittest;
from Ahorcado import Ahorcado;

class Test_Ahorcado(unittest.TestCase):

    def test_letra_correcta(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        self.assertEqual(juego.verificarLetra('A'),'CORRECTA', msg='{0}, {1}')

    def test_letra_incorrecta(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        self.assertEqual(juego.verificarLetra("C"),'INCORRECTA', msg='{0}, {1}')

    def test_palabra_correcta(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        self.assertEqual(juego.verificarLetra(palabra),'CORRECTA', msg='{0}, {1}')

    def test_palabra_incorrecta(self):
        palabra = 'PALABRA'
        palabraErronea = 'MANZANA'
        juego = Ahorcado(palabra)
        self.assertEqual(juego.verificarLetra(palabraErronea),'INCORRECTA', msg='{0}, {1}')

    def test_resta_vida(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        juego.restarVida()
        self.assertEqual(juego.vidas, 2, msg='{0}, {1}')

    def test_definir_palabra_inicio(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        self.assertEqual(palabra, juego.getPalabra(), msg='{0}, {1}')

    def test_acumular_letras_usadas(self):
        palabra = 'PALABRA'
        juego = Ahorcado(palabra)
        letraTest = 'B'
        juego.pruebaLetra(letraTest)
        self.assertEqual(juego.fueUsada(letraTest),True , msg='{0}, {1}')

if __name__ == '__main__':
    unittest.main()