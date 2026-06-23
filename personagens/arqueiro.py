from personagens.personagem import Personagem


class Arqueiro(Personagem):

    def __init__(self, nome, forca, agilidade, inteligencia):

        super().__init__(nome, forca, agilidade, inteligencia)

        self.defesa += 3

        self.habilidades["Tiro Preciso"] = {"dano": 3, "mana": 5}

        self.habilidades["Rajada de Flechas"] = {"dano": 5, "mana": 20}

    def atacar(self, inimigo):

        dano = self.agilidade

        if self.calcular_critico():

            dano *= 2

            print("CRÍTICO!")

        print(f"{self.nome} disparou uma flecha!")

        inimigo.receber_dano(dano)
