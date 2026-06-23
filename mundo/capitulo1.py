from combate.monstros import Goblin
from combate.monstros import Lobo
from combate.batalha import Batalha


class Capitulo1:

    def __init__(self, jogador):

        self.jogador = jogador

    def escolher(self, opcoes):

        while True:

            escolha = input("\nEscolha: ")

            if escolha in opcoes:

                return escolha

            print(
                f"\nOpção inválida. Escolha uma das opções: {', '.join(opcoes)}"
            )

    def iniciar(self):

        print("""

CAPÍTULO 1

Após dias viajando,
você chega a uma encruzilhada.

À esquerda existe uma floresta.

À direita existe uma caverna.

""")

        print("1 - Floresta")
        print("2 - Caverna")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.caminho_floresta()

        elif escolha == "2":

            self.caminho_caverna()

    def caminho_floresta(self):

        self.jogador.escolhas["caminho"] = "floresta"

        print("""

Você segue pela floresta.

Após alguns minutos,
ouve passos entre as árvores.

Um lobo salta dos arbustos!

""")

        monstro = Lobo()

        batalha = Batalha(
            self.jogador,
            monstro
        )

        batalha.iniciar()

        if not self.jogador.esta_vivo():
            return

        print("""

Após derrotar o lobo,
você encontra uma estrada antiga.

Ao longe, uma fumaça sobe entre as árvores.

1 - Investigar a fumaça
2 - Seguir pela estrada

""")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.jogador.escolhas["floresta"] = "fumaca"

            print("""

Você segue em direção à fumaça.

Continua no Capítulo 2...

""")

        elif escolha == "2":

            self.jogador.escolhas["floresta"] = "estrada"

            print("""

Você segue pela estrada.

Continua no Capítulo 2...

""")

    def caminho_caverna(self):

        self.jogador.escolhas["caminho"] = "caverna"

        print("""

Você entra na caverna.

O ar é frio e úmido.

Algo se move na escuridão.

Um goblin aparece!

""")

        monstro = Goblin()

        batalha = Batalha(
            self.jogador,
            monstro
        )

        batalha.iniciar()

        if not self.jogador.esta_vivo():
            return

        print("""

Após derrotar o goblin,
você encontra duas passagens.

1 - Seguir pela passagem iluminada
2 - Seguir pela passagem escura

""")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.jogador.escolhas["caverna"] = "iluminada"

            from mundo.capitulo2 import Capitulo2
            capitulo = Capitulo2(
                self.jogador
            )
            capitulo.iniciar()

        elif escolha == "2":

            self.jogador.escolhas["caverna"] = "escura"

            from mundo.capitulo2 import Capitulo2
            capitulo = Capitulo2(
                self.jogador
            )
            capitulo.iniciar()
