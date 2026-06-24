from utils.interface import titulo, info, aviso, limpar

from utils.efeitos import escrever, pausa


def bestiario():

    limpar()

    titulo("BESTIÁRIO DE ELDORIA")

    escrever("As páginas revelam criaturas já conhecidas...")

    pausa(1)

    print("""
╔══════════════════════════════════════╗
║ GOBLIN                               ║
╠══════════════════════════════════════╣
║ Vida: 50                             ║
║ Ataque: 10                           ║
║ Defesa: 3                            ║
║ Nível: 1                             ║
║                                      ║
║ Pequeno, traiçoeiro e oportunista.   ║
╚══════════════════════════════════════╝
""")

    pausa(0.5)

    print("""
╔══════════════════════════════════════╗
║ LOBO SELVAGEM                        ║
╠══════════════════════════════════════╣
║ Vida: 80                             ║
║ Ataque: 15                           ║
║ Defesa: 5                            ║
║ Nível: 2                             ║
║                                      ║
║ Predador veloz das florestas.        ║
╚══════════════════════════════════════╝
""")

    pausa(0.5)

    print("""
╔══════════════════════════════════════╗
║ MONGE CEGO                           ║
╠══════════════════════════════════════╣
║ Vida: 120                            ║
║ Ataque: 18                           ║
║ Defesa: 8                            ║
║ Nível: 4                             ║
║                                      ║
║ Guerreiro disciplinado e misterioso. ║
╚══════════════════════════════════════╝
""")

    pausa(0.5)

    print("""
╔══════════════════════════════════════╗
║ URSO TIBERS                          ║
╠══════════════════════════════════════╣
║ Vida: 180                            ║
║ Ataque: 24                           ║
║ Defesa: 10                           ║
║ Nível: 6                             ║
║                                      ║
║ A fúria encarnada das montanhas.     ║
╚══════════════════════════════════════╝
""")

    pausa(0.5)

    print("""
╔══════════════════════════════════════╗
║ DRAGÃO DE ELDORIA                    ║
╠══════════════════════════════════════╣
║ Vida: 300                            ║
║ Ataque: 40                           ║
║ Defesa: 15                           ║
║ Nível: 10                            ║
║                                      ║
║ Uma antiga lenda do reino.           ║
╚══════════════════════════════════════╝
""")

    aviso("\nMais criaturas serão registradas...")

    input("\nPressione ENTER para retornar.")
