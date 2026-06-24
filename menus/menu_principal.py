import random
import time
from utils.interface import limpar, titulo, aviso
from utils.efeitos import escrever

frases = [
    "As estrelas observam seu destino.",
    "Rumores de guerra ecoam pelo reino.",
    "Algo antigo despertou nas profundezas.",
    "Nem todas as lendas terminam em glória.",
    "Os ventos carregam o cheiro da aventura.",
    "O destino aguarda um novo herói.",
    "As páginas deste livro ainda estão em branco.",
]


def barra_carregamento():

    print()

    for i in range(21):

        barra = "█" * i
        vazio = "░" * (20 - i)

        print(f"\r[{barra}{vazio}] {i*5}%", end="", flush=True)

        time.sleep(0.08)

    print("\n")


def animacao_inicial():

    limpar()

    escrever("Inicializando Crônicas de Eldoria...")

    time.sleep(0.5)

    barra_carregamento()

    carregamentos = [
        "Carregando mapas...",
        "Carregando criaturas...",
        "Carregando lendas...",
        "Carregando destinos...",
        "Carregando segredos antigos...",
    ]

    for texto in carregamentos:

        escrever(texto)

        time.sleep(0.5)

    escrever("Carregando jogador...")

    time.sleep(1)

    escrever("Jogador não encontrado.")

    time.sleep(1)

    escrever("Criando nova lenda...")

    time.sleep(1.5)

    limpar()


def livro():

    frames = [
        """
                ╭────────────╮
                │            │
                ╰────────────╯
        """,
        """
            ╭────────────────────╮
            │                    │
            ╰────────────────────╯
        """,
        """
        ╔══════════════════════════════╗
        ║                              ║
        ║                              ║
        ║                              ║
        ╚══════════════════════════════╝
        """,
    ]

    for frame in frames:

        limpar()

        print(frame)

        time.sleep(0.3)

    limpar()


def menu():

    animacao_inicial()

    livro()

    frase = random.choice(frases)

    print("""
╔══════════════════════════════════════╗
║                                      ║
║         CRÔNICAS DE ELDORIA          ║
║                                      ║
╚══════════════════════════════════════╝
""")

    escrever(f'"{frase}"')

    print()

    print("1 - Novo Capítulo")

    print("2 - Continuar Leitura")

    print("3 - Bestiário")

    print("4 - Créditos")

    print("5 - Fechar o Livro")

    while True:

        escolha = input("\nEscolha: ")

        if escolha in ["1", "2", "3", "4", "5"]:

            return escolha

        print("\nOpção inválida.")


def creditos():

    limpar()

    titulo("CRÉDITOS")

    print("""
Crônicas de Eldoria

Desenvolvido por:
Fábio Heitor

Projeto de RPG em Python
""")

    input("\nPressione ENTER para voltar...")


def bestiario():

    limpar()

    titulo("BESTIÁRIO")

    print("""
Monstros registrados:

• Goblin
• Lobo Selvagem
• Urso Tibers
""")

    input("\nPressione ENTER para voltar...")


def continuar_leitura():

    limpar()

    titulo("CONTINUAR LEITURA")

    aviso("Sistema de salvamento ainda não implementado.")

    input("\nPressione ENTER para voltar...")
