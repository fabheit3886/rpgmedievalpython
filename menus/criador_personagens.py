from personagens.guerreiro import Guerreiro
from personagens.mago import Mago
from personagens.arqueiro import Arqueiro

from utils.interface import titulo, narracao, opcao, sucesso, aviso, info, limpar, ficha
from utils.efeitos import escrever, pausa


class CriadorPersonagem:

    def criar(self):

        while True:

            limpar()

            escrever("...")
            pausa(0.5)

            escrever("......")
            pausa(0.5)

            escrever("..........")
            pausa(1)

            print()

            narracao("Você abre o livro.")
            pausa(1)

            narracao("As páginas estão vazias.")
            pausa(1)

            narracao("Uma voz ecoa entre as folhas.")
            pausa(1)

            narracao('"Viajante..."')
            pausa(1)

            narracao('"Diga-me seu nome."')

            print()

            nome = input("Nome: ")

            limpar()

            narracao(f'"{nome}..."')
            pausa(1)

            narracao("Um nome digno de ser lembrado.")
            pausa(1)

            narracao("O destino lhe oferece três caminhos.")
            pausa(1)

            titulo("ESCOLHA SEU CAMINHO")

            print()

            opcao("1 - O Caminho da Espada")
            print()

            opcao("2 - O Caminho da Magia")
            print()

            opcao("3 - O Caminho da Precisão")

            print()

            escolha = input("Escolha: ")

            if escolha == "1":

                limpar()

                narracao("Você sente o peso de uma espada.")
                pausa(1)

                narracao("Seu corpo se fortalece.")
                pausa(1)

                sucesso("Você será um Guerreiro.")

                jogador = Guerreiro(nome, 10, 5, 3)

                classe = "Guerreiro"

            elif escolha == "2":

                limpar()

                narracao("Runas antigas brilham ao seu redor.")

                pausa(1)

                narracao("O conhecimento invade sua mente.")

                pausa(1)

                sucesso("Você será um Mago.")

                jogador = Mago(nome, 3, 5, 10)

                classe = "Mago"

            elif escolha == "3":

                limpar()

                narracao("O vento guia seus movimentos.")

                pausa(1)

                narracao("Seus sentidos se tornam aguçados.")

                pausa(1)

                sucesso("Você será um Arqueiro.")

                jogador = Arqueiro(nome, 5, 10, 5)

                classe = "Arqueiro"

            else:

                aviso("Opção inválida.")

                pausa(1)

                continue

            pausa(1)

            limpar()

            ficha(jogador, classe)
            
            print()

            opcao("1 - Confirmar")
            opcao("2 - Refazer")

            confirmar = input("\nEscolha: ")

            if confirmar == "1":

                sucesso("\nPersonagem criado com sucesso!")

                pausa(2)

                return jogador
