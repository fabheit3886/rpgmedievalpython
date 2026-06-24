from utils.interface import titulo, destaque, info, limpar

from utils.efeitos import escrever, pausa


def creditos():

    limpar()

    titulo("CRÉDITOS")

    escrever("Você fecha o livro por um instante...")

    pausa(1)

    escrever("E relembra aqueles que tornaram")

    escrever("esta aventura possível.")

    pausa(1)

    print()

    destaque("CRÔNICAS DE ELDORIA")
    print()

    info("Desenvolvimento")
    print("Fábio Heitor")
    print("Állef Braz da Silva Santos")
    print("Isaías Marques da Silva")

    print()

    info("Professora responsável")
    print("Priscilla Suene de Santana Nogueira Silverio")

    print()
    info("Matéria")
    print("POO - Programação Orientada a Objetos")

    print()
    info("Agradecimentos")
    print("A todos que embarcaram nesta jornada.")

    pausa(1)

    print("""
═══════════════════════════════════════

"Cada herói escreve sua própria lenda."

═══════════════════════════════════════
""")

    input("\nPressione ENTER para retornar.")
