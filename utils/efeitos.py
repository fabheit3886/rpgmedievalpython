import time


def escrever(texto, velocidade=0.02):

    for letra in texto:

        print(letra, end="", flush=True)

        time.sleep(velocidade)

    print()


def pausa(segundos=1):

    time.sleep(segundos)


def suspense():

    escrever(".")

    pausa(0.5)

    escrever("..")

    pausa(0.5)

    escrever("...")

    pausa(0.5)
