class Ahorcado:

    palabra = ""
    vidas = 6
    letrasUsadas = []
    palabraescondida = ""

    def __init__(self, palabraInicial):
        self.reset(palabraInicial)
        # self.setVidas(6)
        # self.definirPalabra(palabraInicial)
        # self.setLetrasUsadas([])
        # self.getPalabraEscondida =   " ".join(["_" for x in self.getPalabra()])
        # self.setPalabraEscondida('')

    def pruebaLetra(self, letra):
        "Prueba una letra"
        if not self.fueUsada(letra):
            mensaje = self.verificarLetra(letra)
            self.letrasUsadas.append(letra)
            if self.getPalabraEscondida().replace(" ", "") == self.getPalabra():
                mensaje = "GANASTE"
            return mensaje

        return "USADA"

    def verificarLetra(self, a):
        "verificacion de letra"
        posi = self.getPalabra().find(a)
        if posi != -1:
            self.setPalabraEscondida(a)
            return "CORRECTA"
        self.restarVida()
        if self.getVidas() == -1:
            return "PERDISTE"
        return "INCORRECTA"

    def verificarPalabra(self, a):
        "verificacion de palabra"
        if self.getPalabra() == a:
            return "GANASTE"
        return "PERDISTE"

    def restarVida(self):
        "Restar vida"
        self.vidas -= 1

    def definirPalabra(self, x):
        "Definicion de palabra"
        self.palabra = x

    def getPalabra(self):
        "Get de palabra"
        return self.palabra

    def setVidas(self, x):
        "Setter de vidas"
        self.vidas = x

    def fueUsada(self, letra):
        "Verifica si la letra fue usada"
        try:
            posicion = self.getLetrasUsadas().index(letra)
            return True
        except ValueError:
            return False

    def getPalabraEscondida(self):
        "Getter de palabra a adivinar"
        return self.palabraescondida

    def setPalabraEscondida(self, letra):
        "Setter de palabra a adivinar"
        self.palabraescondida = " ".join(
            [
                i if (i == letra or self.getPalabraEscondida().find(i) != -1) else "_"
                for i in self.getPalabra()
            ]
        )

    def setLetrasUsadas(self, x):
        "Setter de array de letras usadas"
        self.letrasUsadas = x

    def getLetrasUsadas(self):
        "Getter de array de letras usadas"
        return self.letrasUsadas

    def getVidas(self):
        "Getter de vidas"
        return self.vidas

    def reset(self, palabra=""):
        "Reset de estados"
        self.setVidas(6)
        self.definirPalabra(palabra)
        self.setLetrasUsadas([])
        self.setPalabraEscondida("")
