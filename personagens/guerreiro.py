from personagens.personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome, forca, agilidade, inteligencia):

        super().__init__(nome, forca, agilidade, inteligencia)

        self.vida += 50
        self.defesa += 10

        self.habilidades["Golpe Pesado"] = {"dano": 3, "mana": 0}

        self.habilidades["Bloqueio"] = {"defesa": 10, "mana": 0}

    def atacar(self, inimigo):

        dano = self.forca * 2

        if self.calcular_critico():

            dano *= 2

            print("CRÍTICO!")

        print(f"{self.nome} usou Golpe Pesado!")

        inimigo.receber_dano(dano)
