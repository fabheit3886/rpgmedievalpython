from personagens.personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome, forca, agilidade, inteligencia):

        super().__init__(nome, forca, agilidade, inteligencia)

        self.habilidades.add("Tiro Preciso")

    def atacar(self, inimigo):

        dano = self.agilidade * 2

        print(f"{self.nome} disparou uma flecha!")

        inimigo.receber_dano(dano)
