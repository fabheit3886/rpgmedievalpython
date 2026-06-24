from missoes.lista_missoes import lobos_estrada, goblins_saqueadores
from utils.escolhas import escolher

class Guilda:

    def abrir(self):

        print("""

=== GUILDA DOS AVENTUREIROS ===

1 - Lobos na Estrada
2 - Goblins Saqueadores

0 - Sair

""")

        escolha = input("Escolha: ")

        if escolha == "1":

            print(f"""

MISSÃO

{lobos_estrada.nome}

{lobos_estrada.descricao}

Recompensa:
80 XP
50 Ouro

""")

        elif escolha == "2":

            print(f"""

MISSÃO

{goblins_saqueadores.nome}

{goblins_saqueadores.descricao}

Recompensa:
120 XP
70 Ouro

""")
