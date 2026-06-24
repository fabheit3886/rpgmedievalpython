from utils.interface import capitulo, sucesso, aviso
from utils.escolhas import escolher
from utils.efeitos import escrever, pausa
from cidade.ferreiro import Ferreiro
from combate.batalha import Batalha
from combate.chefe import GuardiaoArkan
from utils.save import salvar

class Capitulo4:

    def __init__(self, jogador):

        self.jogador = jogador

    def iniciar(self):
        self.jogador.capitulo_atual = 4
        salvar(self.jogador)
        capitulo(4, "As Ruínas de Arkan")

        escrever("Dias após deixar Eldoria...")

        pausa(1)

        escrever("Você alcança as lendárias Ruínas de Arkan.")

        pausa(1)

        escrever("Uma figura trabalha em uma forja improvisada.")

        pausa(1)

        escrever("Seu nome é Bjorn.")

        pausa(1)

        Ferreiro().abrir(self.jogador)

        escrever("Mais adiante, algo desperta...")

        pausa(1)

        aviso("O Guardião de Arkan surge!")

        pausa(1)

        batalha = Batalha(self.jogador, GuardiaoArkan())

        batalha.iniciar()

        if not self.jogador.esta_vivo():

            return

        sucesso("O Guardião foi derrotado!")

        escrever("Entre os escombros você encontra um fragmento brilhante.")

        pausa(2)

        escrever('"Apenas quatro fragmentos restantes..."')

        pausa(2)

        escrever("Continua...")
