from personagens.personagem import Personagem


class Mago(Personagem):

    def __init__(self, nome, forca, agilidade, inteligencia):

        super().__init__(nome, forca, agilidade, inteligencia)

        self.mana += 100

        self.habilidades["Bola de Fogo"] = {"dano": 4, "mana": 20}

        self.habilidades["Cura"] = {"cura": 30, "mana": 15}

    def atacar(self, inimigo):

        dano = self.inteligencia

        if self.calcular_critico():

            dano *= 2

            print("CRÍTICO!")

        print(f"{self.nome} realizou um ataque mágico!")

        inimigo.receber_dano(dano)
