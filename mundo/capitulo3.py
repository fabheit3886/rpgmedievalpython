from cidade.loja import Loja
from cidade.estalagem import Estalagem
from cidade.guilda import Guilda
from cidade.npc import conversar
from mundo.capitulo4 import Capitulo4
from utils.escolhas import escolher
from utils.interface import capitulo
from utils.efeitos import escrever
from utils.save import salvar

class Capitulo3:

    def __init__(self, jogador):

        self.jogador = jogador

    def iniciar(self):
        self.jogador.capitulo_atual = 3
        salvar(self.jogador)
        capitulo(3, "Eldoria")

        escrever(
            "Após dias de viagem, os muros da cidade de Eldoria finalmente surgem diante de você."
        )

        escrever("Mercadores, aventureiros e guardas circulam pelas ruas.")

        while True:

            print("""

╔════════════════════╗
║      ELDORIA       ║
╚════════════════════╝

1 - Loja do Mercador
2 - Estalagem
3 - Guilda dos Aventureiros
4 - Conversar com habitantes
5 - Seguir viagem

""")

            escolha = escolher(self.jogador, ["1", "2", "3", "4", "5"])

            if escolha == "1":

                Loja().abrir(self.jogador)

            elif escolha == "2":

                Estalagem().descansar(self.jogador)

            elif escolha == "3":

                Guilda().abrir()

            elif escolha == "4":

                conversar()

            elif escolha == "5":

                escrever(
                    "Ao amanhecer, você deixa Eldoria em direção às Ruínas de Arkan..."
                )

                Capitulo4(self.jogador).iniciar()

                break
