from utils.interface import sucesso, aviso
from utils.escolhas import escolher

class Estalagem:

    def descansar(self, jogador):

        custo = 5

        if jogador.ouro < custo:

            aviso("Você não possui ouro suficiente.")

            return

        jogador.ouro -= custo

        jogador.vida = jogador.vida_maxima
        jogador.mana = jogador.mana_maxima

        sucesso("""

Você passa a noite na estalagem.

Vida restaurada.
Mana restaurada.

""")
