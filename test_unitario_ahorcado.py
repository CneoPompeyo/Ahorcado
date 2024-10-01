import unittest;
from Ahorcado import Ahorcado;

class Test_Ahorcado(unittest.TestCase):

    def test_letra_correcta(self):
        juego = Ahorcado()
        self.assertEqual(juego.verificarLetra('A'),'CORRECTA', msg='{0}, {1}')

    def test_letra_incorrecta(self):
        juego = Ahorcado()
        self.assertEqual(juego.verificarLetra("C"),'INCORRECTA', msg='{0}, {1}')

    def test_palabra_correcta(self):
        juego = Ahorcado()
        self.assertEqual(juego.verificarLetra('BANANA'),'CORRECTA', msg='{0}, {1}')

    def test_palabra_incorrecta(self):
        juego = Ahorcado()
        self.assertEqual(juego.verificarLetra("MANZANA"),'INCORRECTA', msg='{0}, {1}')

    def test_resta_vida(self):
        juego = Ahorcado()
        juego.restarVida()
        self.assertEqual(juego.vidas, 2, msg='{0}, {1}')

if __name__ == '__main__':
    unittest.main()