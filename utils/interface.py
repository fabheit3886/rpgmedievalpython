from colorama import init, Fore, Style

import os

init(autoreset=True)


def capitulo(numero, nome=""):

    titulo(f"CAPÍTULO {numero}")

    if nome:

        print(f"\n{nome}\n")


def limpar():

    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):

    print(Fore.MAGENTA + "\n" + "═" * 50)

    print(Fore.LIGHTMAGENTA_EX + texto.center(50))

    print(Fore.MAGENTA + "═" * 50 + Style.RESET_ALL)


def sucesso(texto):

    print(Fore.GREEN + texto + Style.RESET_ALL)


def erro(texto):

    print(Fore.RED + texto + Style.RESET_ALL)


def aviso(texto):

    print(Fore.YELLOW + texto + Style.RESET_ALL)


def info(texto):

    print(Fore.CYAN + texto + Style.RESET_ALL)


def barra(atual, maximo, tamanho=20):

    preenchido = int((atual / maximo) * tamanho)

    vazio = tamanho - preenchido

    return Fore.GREEN + "█" * preenchido + Fore.WHITE + "░" * vazio + Style.RESET_ALL


def capitulo(numero, nome):

    titulo(f"CAPÍTULO {numero}")

    print(f"\n{nome}\n")


def narracao(texto):

    print(Fore.YELLOW + texto + Style.RESET_ALL)


def opcao(texto):

    print(Fore.CYAN + texto + Style.RESET_ALL)


def magia(texto):

    print(Fore.BLUE + texto + Style.RESET_ALL)


def combate(texto):

    print(Fore.RED + texto + Style.RESET_ALL)


def destaque(texto):

    print(Fore.LIGHTMAGENTA_EX + texto + Style.RESET_ALL)


def barra_atributo(valor, tamanho=10):

    preenchido = "█" * valor

    vazio = "░" * (tamanho - valor)

    return f"{preenchido}{vazio} {valor}"


def ficha(jogador, classe):

    titulo("FICHA DO HERÓI")

    print("╔════════════════════════════════════════════╗")

    print(f"║ Nome: {jogador.nome:<35}║")

    print(f"║ Classe: {classe:<32}║")

    print("╠════════════════════════════════════════════╣")

    print(f"║ Vida: {jogador.vida:<35}║")

    print(f"║ Mana: {jogador.mana:<35}║")

    print("╠════════════════════════════════════════════╣")

    print(f"║ Força:        {barra_atributo(jogador.forca):<23}║")

    print(f"║ Agilidade:    {barra_atributo(jogador.agilidade):<23}║")

    print(f"║ Inteligência: {barra_atributo(jogador.inteligencia):<23}║")

    print("╚════════════════════════════════════════════╝")
