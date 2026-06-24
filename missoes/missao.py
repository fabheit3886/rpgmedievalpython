class Missao:

    def __init__(self, nome, descricao, recompensa_xp, recompensa_ouro):

        self.nome = nome
        self.descricao = descricao

        self.recompensa_xp = recompensa_xp
        self.recompensa_ouro = recompensa_ouro

        self.concluida = False

    def completar(self, jogador):

        if self.concluida:

            return

        self.concluida = True

        jogador.ganhar_xp(self.recompensa_xp)

        jogador.ouro += self.recompensa_ouro

        print(f"""

Missão concluída!

+{self.recompensa_xp} XP
+{self.recompensa_ouro} Ouro

""")
