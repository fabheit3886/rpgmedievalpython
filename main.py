from menus.criador_personagens import CriadorPersonagem
from menus.menu_principal import menu
from menus.bestiario import bestiario
from menus.creditos import creditos

from mundo.historia import Historia
from mundo.capitulo1 import Capitulo1
from mundo.capitulo2 import Capitulo2

from utils.save import salvar, carregar, apagar_save

from utils.interface import sucesso, erro, aviso

from utils.efeitos import pausa

while True:

    opcao = menu()

    if opcao == "1":

        # Novo jogo
        apagar_save()

        criador = CriadorPersonagem()

        jogador = criador.criar()

        salvar(jogador)

        historia = Historia(jogador)

        historia.iniciar()

        break

    elif opcao == "2":

        # Continuar
        jogador = carregar()

        if jogador is None:

            erro("\nNenhum save encontrado.")

            pausa(2)

            continue

        sucesso(f"\nBem-vindo de volta, {jogador.nome}!")

        pausa(2)

        # Continua do capítulo salvo
        if jogador.capitulo_atual == 1:

            Capitulo1(jogador).iniciar()

        elif jogador.capitulo_atual == 2:

            Capitulo2(jogador).iniciar()

        else:

            Historia(jogador).iniciar()

        break

    elif opcao == "3":

        bestiario()

    elif opcao == "4":

        creditos()

    elif opcao == "5":

        aviso("\nAté a próxima aventura.")

        pausa(2)

        break

    else:

        erro("\nOpção inválida.")

        pausa(1)
