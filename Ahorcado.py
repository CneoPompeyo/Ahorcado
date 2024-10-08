class Ahorcado():

    palabra = 'BANANA'
    vidas = 3
    letrasUsadas = []
    palabraescondida = ""

    def __init__(self, palabraInicial):
        self.definirPalabra(palabraInicial)
        self.palabraescondida =   " ".join(["_" for x in self.palabra])

    def pruebaLetra(self,letra):
        self.verificarLetra(letra)
        self.letrasUsadas.append(letra)

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
        #return [i for i, elemento in enumerate(lista) if elemento == palabra]