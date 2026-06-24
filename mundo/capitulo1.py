from combate.monstros import Goblin
from combate.monstros import Lobo
from combate.batalha import Batalha
from mundo.capitulo2 import Capitulo2
from utils.interface import titulo, limpar, sucesso, aviso, info, capitulo
from utils.save import salvar
from utils.efeitos import escrever, pausa
from utils.escolhas import escolher


class Capitulo1:

    def __init__(self, jogador):

        self.jogador = jogador

    def escolher(self, opcoes):

        while True:

            escolha = escolher(self.jogador, ["1", "2"])

            if escolha in opcoes:

                return escolha

            aviso(f"Escolha apenas: {', '.join(opcoes)}")

    def iniciar(self):
        self.jogador.capitulo_atual = 1
        salvar(self.jogador)
        capitulo(1, "A encruzilhada")

        escrever("Após dias viajando, você chega a uma encruzilhada.")

        pausa(1)

        escrever("À esquerda existe uma floresta.")

        pausa(1)

        escrever("À direita existe uma caverna.")

        print()

        info("1 - Floresta")
        info("2 - Caverna")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.caminho_floresta()

        elif escolha == "2":

            self.caminho_caverna()

    def caminho_floresta(self):

        self.jogador.escolhas["caminho"] = "floresta"

        limpar()

        titulo("FLORESTA")

        escrever("Você segue pela floresta.")

        pausa(1)

        escrever("Após alguns minutos, ouve passos entre as árvores.")

        pausa(1)

        aviso("Um lobo salta dos arbustos!")

        pausa(1)

        batalha = Batalha(self.jogador, Lobo())

        batalha.iniciar()

        if not self.jogador.esta_vivo():

            return

        limpar()

        titulo("APÓS A BATALHA")

        escrever("Após derrotar o lobo, você encontra uma estrada antiga.")

        pausa(1)

        escrever("Ao longe, uma fumaça sobe entre as árvores.")

        print()

        info("1 - Investigar a fumaça")

        info("2 - Seguir pela estrada")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.jogador.escolhas["floresta"] = "fumaca"

        else:

            self.jogador.escolhas["floresta"] = "estrada"

        pausa(1)

        capitulo = Capitulo2(self.jogador)

        capitulo.iniciar()

    def caminho_caverna(self):

        self.jogador.escolhas["caminho"] = "caverna"

        limpar()

        titulo("CAVERNA")

        escrever("Você entra na caverna.")

        pausa(1)

        escrever("O ar é frio e úmido.")

        pausa(1)

        escrever("Algo se move na escuridão.")

        pausa(1)

        aviso("Um goblin aparece!")

        pausa(1)

        batalha = Batalha(self.jogador, Goblin())

        batalha.iniciar()

        if not self.jogador.esta_vivo():

            return

        limpar()

        titulo("APÓS A BATALHA")

        escrever("Após derrotar o goblin, você encontra duas passagens.")

        print()

        info("1 - Seguir pela passagem iluminada")

        info("2 - Seguir pela passagem escura")

        escolha = self.escolher(["1", "2"])

        if escolha == "1":

            self.jogador.escolhas["caverna"] = "iluminada"

        else:

            self.jogador.escolhas["caverna"] = "escura"

        pausa(1)

        capitulo = Capitulo2(self.jogador)

        capitulo.iniciar()
