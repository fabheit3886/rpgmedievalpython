from mundo.capitulo1 import Capitulo1


class Historia:

    def __init__(self, jogador):

        self.jogador = jogador

    def iniciar(self):

        capitulo = Capitulo1(self.jogador)

        capitulo.iniciar()
