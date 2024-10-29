class Ahorcado():

    palabra = ''
    vidas = 6
    letrasUsadas = []
    palabraescondida = ''

    def __init__(self, palabraInicial):
        self.definirPalabra(palabraInicial)
        self.palabraescondida =   " ".join(["_" for x in self.palabra])
        self.letrasUsadas = []
        self.vidas = 6

    def pruebaLetra(self,letra):
        if (not(self.fueUsada(letra))):
            mensaje = self.verificarLetra(letra)
            self.letrasUsadas.append(letra)
            return mensaje
        else:
            return 'USADA'


    def verificarLetra(self, a):
        posi = self.palabra.find(a)
        if (posi != -1):
            self.setPalabraEscondida(a)
            return 'CORRECTA'
        else:
            self.restarVida()
            return 'INCORRECTA'
        
    def verificarPalabra(self, a): 
        if (self.palabra == a):
            return 'CORRECTA'
        else:
            return 'INCORRECTA'
    
    def restarVida(self):
        self.vidas -= 1

    def definirPalabra(self, x):
        self.palabra = x
    
    def getPalabra(self):
        return self.palabra
    
    def fueUsada(self,letra):
        try:
            posicion = self.letrasUsadas.index(letra)
            return True
        except ValueError:
            return False
        
    def getPalabraEscondida(self):
        return self.palabraescondida
    
    def setPalabraEscondida(self, letra):
        self.palabraescondida = ' '.join([letra if i == letra else "_" for i in self.palabra])


#def main():
#    palabra = 'PALABRA'
#    juego = Ahorcado(palabra)
#    juego.setPalabraEscondida