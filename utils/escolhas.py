def escolher(jogador, opcoes):

    while True:

        escolha = input("\nEscolha: ")

        if escolha == "0":

            jogador.menu_personagem()

            continue

        if escolha in opcoes:

            return escolha

        print("Opção inválida.")
