class Ahorcado():
    palabra = 'BANANA'

    def verificarLetra(self, a):
        posi = self.palabra.find(a)
        if (posi != -1):
            return 'CORRECTA'
        else:
            return 'INCORRECTA'