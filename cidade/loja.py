from utils.interface import sucesso, erro
from utils.escolhas import escolher


class Loja:

    itens = {
        "1": ("Poção de Vida", 15),
        "2": ("Poção de Mana", 20),
        "3": ("Elixir Maior", 40),
    }

    def abrir(self, jogador):

        while True:

            print("""

LOJA DE ROLAND

1 - Poção de Vida - 15 ouro
2 - Poção de Mana - 20 ouro
3 - Elixir Maior - 40 ouro

4 - Sair

""")

            escolha = escolher(jogador, ["1", "2", "3", "4"])

            if escolha == "4":

                break

            if escolha not in self.itens:

                erro("Opção inválida.")

                continue

            item, preco = self.itens[escolha]

            if jogador.ouro < preco:

                erro("Ouro insuficiente.")

                continue

            jogador.ouro -= preco

            jogador.adicionar_item(item)

            sucesso(f"{item} comprado.")
