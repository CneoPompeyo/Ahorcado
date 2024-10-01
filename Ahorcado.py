class Ahorcado():

    palabra = 'BANANA'
    vidas = 3

    def verificarLetra(self, a):
        posi = self.palabra.find(a)
        if (posi != -1):
            return 'CORRECTA'
        else:
            return 'INCORRECTA'
        
    def verificarPalabra(self, a): 
        if (self.palabra == a):
            return 'CORRECTA'
        else:
            return 'INCORRECTA'
    
    def restarVida(self):
        self.vidas -= 1
