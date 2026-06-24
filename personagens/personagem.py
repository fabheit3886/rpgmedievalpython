import random
from utils.interface import limpar

class Personagem:

    def __init__(self, nome, forca, agilidade, inteligencia):

        self.nome = nome

        self.forca = forca
        self.agilidade = agilidade
        self.inteligencia = inteligencia

        self.vida_maxima = 100
        self.vida = self.vida_maxima

        self.mana_maxima = 50
        self.mana = self.mana_maxima

        self.defesa = 5

        self.nivel = 1
        self.xp = 0
        self.xp_proximo_nivel = 100

        self.ouro = 0

        self.inventario = []

        self.habilidades = {}
        self.escolhas = {}

        self.descobertas = []
        self.capitulo_atual = 1

        def menu_personagem(self):

            while True:

                limpar()

                self.mostrar_status()

                print("""
        1 - Inventário
        2 - Habilidades
        3 - Equipamentos

        0 - Voltar
        """)

                escolha = input("\nEscolha: ")

                if escolha == "1":

                    self.mostrar_inventario()

                elif escolha == "2":

                    self.mostrar_habilidades()

                elif escolha == "3":

                    self.mostrar_equipamentos()

                elif escolha == "0":

                    break

                input("\nENTER para continuar...")
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

    def ganhar_xp(self, quantidade):

        self.xp += quantidade

        print(f"\n{self.nome} recebeu {quantidade} XP!")

        while self.xp >= self.xp_proximo_nivel:

            self.subir_nivel()

    def subir_nivel(self):

        self.xp -= self.xp_proximo_nivel

        self.nivel += 1

        self.xp_proximo_nivel = int(self.xp_proximo_nivel * 1.5)

        self.vida_maxima += 20
        self.vida = self.vida_maxima

        self.mana_maxima += 10
        self.mana = self.mana_maxima

        self.forca += 2
        self.agilidade += 2
        self.inteligencia += 2

        print(f"""

================================

PARABÉNS!

{self.nome} alcançou o nível {self.nivel}!

Vida Máxima +20
Mana Máxima +10

Força +2
Agilidade +2
Inteligência +2

================================

""")

    def calcular_critico(self):

        chance = random.randint(1, 100)

        return chance <= 20

    def esquivar(self):

        chance = random.randint(1, 100)

        return chance <= self.agilidade * 2

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

Nome: {self.nome}

Nível: {self.nivel}
XP: {self.xp}/{self.xp_proximo_nivel}

Vida: {self.vida}/{self.vida_maxima}
Mana: {self.mana}/{self.mana_maxima}

Ouro: {self.ouro}

Força: {self.forca}
Agilidade: {self.agilidade}
Inteligência: {self.inteligencia}
Defesa: {self.defesa}

""")

    def usar_item(self):

        if not self.inventario:

            print("\nInventário vazio.")

            return

        print("\n=== INVENTÁRIO ===\n")

        itens_unicos = {}

        for item in self.inventario:

            if item not in itens_unicos:

                itens_unicos[item] = 0

            itens_unicos[item] += 1

        nomes_itens = list(itens_unicos.keys())

        for i, item in enumerate(nomes_itens, start=1):

            print(f"{i} - {item} " f"x{itens_unicos[item]}")

        try:

            escolha = int(input("\nEscolha: ")) - 1

            item = nomes_itens[escolha]

        except:

            print("Item inválido.")

            return

        if item == "Poção de Vida":

            cura = 50

            self.vida += cura

            if self.vida > self.vida_maxima:

                self.vida = self.vida_maxima

            print(f"\nVocê recuperou {cura} de vida.")

        elif item == "Poção de Mana":

            mana = 30

            self.mana += mana

            if self.mana > self.mana_maxima:

                self.mana = self.mana_maxima

            print(f"\nVocê recuperou {mana} de mana.")

        self.inventario.remove(item)
