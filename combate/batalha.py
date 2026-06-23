class Batalha:

    def __init__(self, jogador, monstro):

        self.jogador = jogador
        self.monstro = monstro

    def iniciar(self):

        print("======================")
        print(" INÍCIO DA BATALHA ")
        print("======================")

        while self.jogador.esta_vivo() and self.monstro.esta_vivo():

            self.turno_jogador()

            if not self.monstro.esta_vivo():
                break

            self.turno_monstro()

        self.finalizar()

    def turno_jogador(self):

        print(f"""

================================

{self.jogador.nome}
Vida: {self.jogador.vida}
Mana: {self.jogador.mana}

------------------------------

{self.monstro.nome}
Vida: {self.monstro.vida}

================================

1 - Atacar
2 - Habilidades
3 - Status

""")

        escolha = input("Escolha: ")

        if escolha == "1":

            self.jogador.atacar(self.monstro)

        elif escolha == "2":

            self.usar_habilidade()

        elif escolha == "3":

            self.jogador.mostrar_status()

        else:

            print("Ação inválida.")

    def turno_monstro(self):

        print(f"\nTurno do {self.monstro.nome}")

        self.monstro.atacar(self.jogador)

    def finalizar(self):

        if self.jogador.esta_vivo():

            print(f"""

====================

Vitória!

Você derrotou:
{self.monstro.nome}

XP recebido:
{self.monstro.xp}

Ouro recebido:
{self.monstro.ouro}

====================

""")

            self.jogador.ganhar_xp(self.monstro.xp)

        else:

            print("""

====================

Derrota...

Seu herói caiu.

====================

""")

    def usar_habilidade(self):

        habilidades = list(self.jogador.habilidades.keys())

        if not habilidades:

            print("Nenhuma habilidade disponível.")

            return

        print("\n=== HABILIDADES ===\n")

        for i, habilidade in enumerate(habilidades):

            dados = self.jogador.habilidades[habilidade]

            print(f"{i+1} - {habilidade} " f"(Mana: {dados.get('mana', 0)})")

        try:

            escolha = int(input("\nEscolha: ")) - 1

            habilidade = habilidades[escolha]

        except:

            print("Opção inválida.")
            return

        dados = self.jogador.habilidades[habilidade]

        custo_mana = dados.get("mana", 0)

        if self.jogador.mana < custo_mana:

            print("Mana insuficiente.")

            return

        self.jogador.mana -= custo_mana

        if "dano" in dados:

            atributo_principal = max(
                self.jogador.forca, self.jogador.agilidade, self.jogador.inteligencia
            )

            dano = atributo_principal * dados["dano"]

            print(f"\n{self.jogador.nome} usou {habilidade}!")

            self.monstro.receber_dano(dano)

        elif "cura" in dados:

            cura = dados["cura"]

            self.jogador.vida += cura

            print(f"\n{self.jogador.nome} recuperou {cura} pontos de vida!")

        elif "defesa" in dados:

            bonus = dados["defesa"]

            self.jogador.defesa += bonus

            print(f"\n{self.jogador.nome} aumentou sua defesa em {bonus}!")
