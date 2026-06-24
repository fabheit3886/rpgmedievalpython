import random

falas = [
    "Ouvi dizer que existem ruínas antigas ao norte.",
    "Os mercadores estão assustados com os ataques nas estradas.",
    "Dizem que um dragão dorme além das montanhas.",
    "A Guilda dos Aventureiros procura novos recrutas.",
    "Já ouviu falar nas Ruínas de Arkan?",
]


def conversar():

    fala = random.choice(falas)

    print(f"""

Morador de Eldoria

"{fala}"

""")
