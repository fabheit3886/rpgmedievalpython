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
        self.xp_proximo_nivel = 100

        self.inventario = []

        self.habilidades = {}
        self.escolhas = {}

    def atacar(self, inimigo):

        dano = self.forca

        if self.calcular_critico():

            dano *= 2

            print("CRÍTICO!")

        inimigo.receber_dano(dano)

    def receber_dano(self, dano):

        if self.esquivar():

            print(f"{self.nome} desviou do ataque!")

            return

        dano_final = dano - self.defesa

        if dano_final < 0:
            dano_final = 0

        self.vida -= dano_final

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu {dano_final} de dano!")

    def esta_vivo(self):

        return self.vida > 0

    def calcular_critico(self):

        chance = random.randint(1, 100)

        return chance <= 20

    def esquivar(self):

        chance = random.randint(1, 100)

        return chance <= self.agilidade * 2

    def ganhar_xp(self, quantidade):

        self.xp += quantidade

        print(f"{self.nome} ganhou {quantidade} XP!")

        self.verificar_level_up()

    def verificar_level_up(self):

        while self.xp >= self.xp_proximo_nivel:

            self.xp -= self.xp_proximo_nivel

            self.nivel += 1

            self.xp_proximo_nivel += 50

            self.vida += 20
            self.mana += 10

            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def adicionar_item(self, item):

        self.inventario.append(item)

        print(f"{item} adicionado ao inventário.")

    def mostrar_inventario(self):

        print("\n=== INVENTÁRIO ===")

        if not self.inventario:

            print("Inventário vazio.")
            return

        for item in self.inventario:

            print(f"- {item}")

    def mostrar_habilidades(self):

        print("\n=== HABILIDADES ===")

        if not self.habilidades:

            print("Nenhuma habilidade.")
            return

        for nome, dados in self.habilidades.items():

            custo = dados.get("mana", 0)

            print(f"{nome} | Mana: {custo}")

    def mostrar_status(self):

        print(f"""
================================

Nome: {self.nome}

Nível: {self.nivel}
XP: {self.xp}/{self.xp_proximo_nivel}

Vida: {self.vida}
Mana: {self.mana}

Força: {self.forca}
Agilidade: {self.agilidade}
Inteligência: {self.inteligencia}

Defesa: {self.defesa}

================================
""")
