class Batalha:

    def __init__(self, jogador, monstro):

        self.jogador = jogador
        self.monstro = monstro

    def iniciar(self):

        print("======================")
        print(" ⚔ INÍCIO DA BATALHA ⚔")
        print("======================")

        while self.jogador.esta_vivo() and self.monstro.esta_vivo():

            self.turno_jogador()

            if not self.monstro.esta_vivo():
                break

            self.turno_monstro()

        self.finalizar()

    def turno_jogador(self):

        print(f"""
Seu turno:

{self.jogador.nome}
 {self.jogador.vida}

Inimigo:
{self.monstro.nome}
 {self.monstro.vida}


1 - Atacar
2 - Mostrar status
""")

        escolha = input("Escolha: ")

        if escolha == "1":

            self.jogador.atacar(self.monstro)

        elif escolha == "2":

            self.usar_habilidade()
        else:

            print("Ação inválida")

    def turno_monstro(self):

        print(f"\nTurno do {self.monstro.nome}")

        self.monstro.atacar(self.jogador)

    def finalizar(self):

        if self.jogador.esta_vivo():

            print(f"""
 Vitória!

Você derrotou:
{self.monstro.nome}

XP recebido:
{self.monstro.xp}

Ouro:
{self.monstro.ouro}
""")

        else:

            print("""
 Derrota...

Seu herói caiu.
""")

    def usar_habilidade(self):

        print("\nHabilidades:")

        for habilidade in self.jogador.habilidades:

            print(habilidade)

        escolha = input("Escolha: ")

        if escolha == "Golpe Pesado":

            dano = self.jogador.forca * 3

            print("Golpe Pesado!")

            self.monstro.receber_dano(dano)

        elif escolha == "Bola de Fogo":

            if self.jogador.mana < 20:

                print("Mana insuficiente")

                return

            dano = self.jogador.inteligencia * 4

            self.jogador.mana -= 20

            print("Bola de Fogo!")

            self.monstro.receber_dano(dano)
