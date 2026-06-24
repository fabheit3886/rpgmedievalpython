class Loja:

    def __init__(self, jogador):

        self.jogador = jogador

    def abrir(self):

        while True:

            print("""

===== LOJA =====

Seu ouro: {}
            
1 - Poção de Vida (30)
2 - Poção de Mana (25)
3 - Sair

""".format(self.jogador.ouro))

            escolha = input("Escolha: ")

            if escolha == "1":

                self.comprar_pocao_vida()

            elif escolha == "2":

                self.comprar_pocao_mana()

            elif escolha == "3":

                break

    def comprar_pocao_vida(self):

        if self.jogador.ouro < 30:

            print("\nOuro insuficiente.")

            return

        self.jogador.ouro -= 30

        self.jogador.inventario.append("Poção de Vida")

        print("\nPoção comprada!")

    def comprar_pocao_mana(self):

        if self.jogador.ouro < 25:

            print("\nOuro insuficiente.")

            return

        self.jogador.ouro -= 25

        self.jogador.inventario.append("Poção de Mana")

        print("\nPoção comprada!")
