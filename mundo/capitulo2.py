from combate.batalha import Batalha
from combate.monstros import Goblin
from combate.monstros import Lobo
from utils.interface import limpar, capitulo, sucesso, aviso, info
from utils.efeitos import escrever, pausa
from utils.save import salvar
from mundo.capitulo3 import Capitulo3
from utils.escolhas import escolher


class Capitulo2:

    def __init__(self, jogador):

        self.jogador = jogador

    def iniciar(self):

        self.jogador.capitulo_atual = 2

        salvar(self.jogador)

        caminho = self.jogador.escolhas.get("caminho")

        if caminho == "floresta":

            self.capitulo_floresta()

        elif caminho == "caverna":

            self.capitulo_caverna()

    def capitulo_floresta(self):

        escolha = self.jogador.escolhas.get("floresta")

        if escolha == "fumaca":

            self.acampamento_bandido()

        elif escolha == "estrada":

            self.mercador_perdido()

    def capitulo_caverna(self):

        escolha = self.jogador.escolhas.get("caverna")

        if escolha == "iluminada":

            self.santuario_antigo()

        elif escolha == "escura":

            self.tunel_profundo()

    def acampamento_bandido(self):

        limpar()

        capitulo(2, "O Acampamento Abandonado")

        escrever("Você segue a fumaça.")
        pausa(1)

        escrever("Entre as árvores existe um pequeno acampamento abandonado.")
        pausa(1)

        aviso("Um saqueador aparece!")
        pausa(1)

        batalha = Batalha(self.jogador, Goblin())

        batalha.iniciar()

        if not self.jogador.esta_vivo():

            return

        sucesso("Após a luta você encontra algumas moedas.")
        sucesso("Você encontra um mapa antigo.")

        self.jogador.ouro += 20

        info("+20 Ouro")

        pausa(2)

        Capitulo3(self.jogador).iniciar()

    def mercador_perdido(self):

        limpar()

        capitulo(2, "O Mercador Perdido")

        escrever("Seguindo a estrada você encontra um mercador.")
        pausa(1)

        escrever("A carroça dele está quebrada.")

        print()

        info("1 - Ajudar")
        info("2 - Ignorar")

        while True:

            escolha = escolher(self.jogador, ["1", "2"])

            if escolha in ["1", "2"]:

                break

            aviso("Escolha apenas 1 ou 2.")

        if escolha == "1":

            sucesso("Você ajuda o mercador.")
            sucesso("Ele lhe entrega uma poção de vida.")

            self.jogador.adicionar_item("Poção de Vida")

        else:

            escrever("Você continua sua viagem sozinho.")

        pausa(2)

        Capitulo3(self.jogador).iniciar()

    def santuario_antigo(self):

        limpar()

        capitulo(2, "Santuário Esquecido")

        escrever("A passagem iluminada leva a um santuário antigo.")
        pausa(1)

        escrever("No centro existe um altar coberto por runas.")
        pausa(1)

        self.jogador.mana += 20

        if self.jogador.mana > self.jogador.mana_maxima:

            self.jogador.mana = self.jogador.mana_maxima

        sucesso("Sua energia foi restaurada.")

        info("+20 Mana")

        pausa(2)

        Capitulo3(self.jogador).iniciar()

    def tunel_profundo(self):

        limpar()

        capitulo(2, "Túnel Profundo")

        escrever("Você segue pela escuridão.")
        pausa(1)

        aviso("Um lobo faminto surge do túnel!")
        pausa(1)

        batalha = Batalha(self.jogador, Lobo())

        batalha.iniciar()

        if not self.jogador.esta_vivo():

            return

        sucesso("Após a vitória você encontra uma enorme porta de pedra.")

        escrever("Símbolos estranhos cobrem sua superfície.")

        pausa(2)

        Capitulo3(self.jogador).iniciar()
