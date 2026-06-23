from combate.batalha import Batalha
from combate.monstros import Goblin
from combate.monstros import Lobo


class Capitulo2:

    def __init__(self, jogador):

        self.jogador = jogador

    def iniciar(self):

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

        print("""

CAPÍTULO 2

Você segue a fumaça.

Entre as árvores existe um pequeno
acampamento abandonado.

De repente um saqueador aparece.

""")

        batalha = Batalha(self.jogador, Goblin())

        batalha.iniciar()

        if not self.jogador.esta_vivo():
            return

        print("""

Após a luta você encontra
algumas moedas e um mapa.

Fim do Capítulo 2.

""")

    def mercador_perdido(self):

        print("""

CAPÍTULO 2

Seguindo a estrada você encontra
um mercador com a carroça quebrada.

""")

        print("""
1 - Ajudar
2 - Ignorar
""")

        escolha = input("Escolha: ")

        if escolha == "1":

            print("""

O mercador agradece.

Você recebe uma recompensa.

""")

        else:

            print("""

Você continua viagem sozinho.

""")

    def santuario_antigo(self):

        print("""

CAPÍTULO 2

A passagem iluminada leva a um
santuário esquecido.

No centro existe um altar.

""")

        self.jogador.mana += 20

        print("""
Sua mana aumentou em 20.
""")

    def tunel_profundo(self):

        print("""

CAPÍTULO 2

Você segue pela escuridão.

Um lobo faminto surge do túnel.

""")

        batalha = Batalha(self.jogador, Lobo())

        batalha.iniciar()

        if not self.jogador.esta_vivo():
            return

        print("""

Após a vitória você encontra
uma estranha porta de pedra.

Fim do Capítulo 2.

""")
