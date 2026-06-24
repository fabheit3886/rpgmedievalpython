from itens.equipamentos import espada_ferro, armadura_couro
from utils.escolhas import escolher

class Ferreiro:

    def abrir(self, jogador):

        while True:

            print("""

FERREIRO BJORN

1 - Espada de Ferro (100 ouro)
2 - Armadura de Couro (80 ouro)

0 - Sair

""")

            escolha = input("Escolha: ")

            if escolha == "0":

                break

            if escolha == "1":

                if jogador.ouro >= 100:

                    jogador.ouro -= 100

                    jogador.forca += espada_ferro.ataque

                    print("Ataque aumentado!")

            elif escolha == "2":

                if jogador.ouro >= 80:

                    jogador.ouro -= 80

                    jogador.defesa += armadura_couro.defesa

                    print("Defesa aumentada!")
