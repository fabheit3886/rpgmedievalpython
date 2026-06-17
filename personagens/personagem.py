import random


class Personagem:

    def __init__(self, nome, forca, agilidade, inteligencia):

        self.nome = nome

        self.forca = forca
        self.agilidade = agilidade
        self.inteligencia = inteligencia

        self.vida = 100
        self.mana = 50

        self.defesa = 5

        self.nivel = 1
        self.xp = 0

        self.inventario = []
        self.habilidades = set()

    def atacar(self, inimigo):

        dano = self.forca

        if self.calcular_critico():

            dano *= 2

            print("⚡ CRÍTICO!")

        inimigo.receber_dano(dano)

    def receber_dano(self, dano):

        self.vida -= dano

    def esta_vivo(self):

        return self.vida > 0

    def mostrar_status(self):

        print(f"""
        Nome: {self.nome}

        Vida: {self.vida}
        Mana: {self.mana}

        Força: {self.forca}
        Agilidade: {self.agilidade}
        Inteligência: {self.inteligencia}

        Habilidades:
        {self.habilidades}
        """)

    def calcular_critico(self):

        chance = random.randint(1, 100)

        return chance <= 20

    def esquivar(self):

        chance = random.randint(1, 100)

        return chance <= self.agilidade * 2

    def receber_dano(self, dano):

        if self.esquivar():

            print(f"{self.nome} desviou do ataque!")

            return

        self.vida -= dano

        if self.vida < 0:
            self.vida = 0
