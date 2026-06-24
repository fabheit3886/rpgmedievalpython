from utils.interface import titulo, barra, sucesso, erro, aviso, info
from utils.interface import limpar
from utils.efeitos import escrever, pausa


class Batalha:

    def __init__(self, jogador, monstro):

        self.jogador = jogador
        self.monstro = monstro

        self.log = []

    def adicionar_log(self, mensagem):

        self.log.append(mensagem)

        if len(self.log) > 5:

            self.log.pop(0)

    def mostrar_log(self):

        print("\nÚLTIMAS AÇÕES\n")

        for mensagem in self.log:

            print(f"• {mensagem}")

        print()

    def iniciar(self):

        titulo("BATALHA")

        escrever(f"Um {self.monstro.nome} apareceu!")

        pausa(1)

        while self.jogador.esta_vivo() and self.monstro.esta_vivo():

            self.turno_jogador()

            if not self.monstro.esta_vivo():

                break

            pausa(1)

            self.turno_monstro()

            pausa(1)

        self.finalizar()

    def turno_jogador(self):

        limpar()

        titulo("SEU TURNO")

        self.mostrar_log()

        print(f"""
JOGADOR

Nome: {self.jogador.nome}

Vida:
[{barra(
    self.jogador.vida,
    self.jogador.vida_maxima
)}]
{self.jogador.vida}/{self.jogador.vida_maxima}

Mana:
[{barra(
    self.jogador.mana,
    self.jogador.mana_maxima
)}]
{self.jogador.mana}/{self.jogador.mana_maxima}

--------------------------------------------------

INIMIGO

Nome: {self.monstro.nome}

Vida:
[{barra(
    self.monstro.vida,
    self.monstro.vida_maxima
)}]
{self.monstro.vida}/{self.monstro.vida_maxima}

--------------------------------------------------

1 - Atacar
2 - Habilidades
3 - Status
4 - Inventário
""")

        escolha = input("\nEscolha: ")

        if escolha == "1":

            vida_antes = self.monstro.vida

            escrever(f"\n{self.jogador.nome} ataca!")

            pausa(0.5)

            self.jogador.atacar(self.monstro)

            dano = vida_antes - self.monstro.vida

            self.adicionar_log(f"{self.jogador.nome} causou {dano} de dano.")

        elif escolha == "2":

            self.usar_habilidade()

        elif escolha == "3":

            self.jogador.mostrar_status()

        elif escolha == "4":

            self.jogador.usar_item()

        else:

            erro("Ação inválida.")

    def turno_monstro(self):

        limpar()

        titulo(f"TURNO DO {self.monstro.nome.upper()}")

        pausa(0.5)

        vida_antes = self.jogador.vida

        self.monstro.atacar(self.jogador)

        dano = vida_antes - self.jogador.vida

        if dano > 0:

            self.adicionar_log(f"{self.monstro.nome} causou {dano} de dano.")

        else:

            self.adicionar_log(f"{self.monstro.nome} não causou dano.")

    def finalizar(self):
        if self.monstro.nome not in self.jogador.descobertas:

            self.jogador.descobertas.append(self.monstro.nome)
        if self.jogador.esta_vivo():

            self.jogador.ganhar_xp(self.monstro.xp)

            self.jogador.ouro += self.monstro.ouro

            titulo("VITÓRIA")

            sucesso(f"Você derrotou {self.monstro.nome}")

            print()

            info(f"+{self.monstro.xp} XP")

            info(f"+{self.monstro.ouro} Ouro")

        else:

            titulo("DERROTA")

            erro("Seu herói caiu em batalha.")

    def usar_habilidade(self):

        habilidades = list(self.jogador.habilidades.keys())

        if not habilidades:

            aviso("Nenhuma habilidade disponível.")

            return

        titulo("HABILIDADES")

        for i, habilidade in enumerate(habilidades, start=1):

            dados = self.jogador.habilidades[habilidade]

            print(f"{i} - {habilidade}" f" | Mana: {dados.get('mana', 0)}")

        try:

            escolha = int(input("\nEscolha: ")) - 1

            habilidade = habilidades[escolha]

        except:

            erro("Opção inválida.")

            return

        dados = self.jogador.habilidades[habilidade]

        custo_mana = dados.get("mana", 0)

        if self.jogador.mana < custo_mana:

            erro("Mana insuficiente.")

            return

        self.jogador.mana -= custo_mana

        if "dano" in dados:

            atributo_principal = max(
                self.jogador.forca, self.jogador.agilidade, self.jogador.inteligencia
            )

            dano = atributo_principal * dados["dano"]

            vida_antes = self.monstro.vida

            escrever(f"\n{self.jogador.nome} usou {habilidade}!")

            pausa(0.5)

            self.monstro.receber_dano(dano)

            dano_real = vida_antes - self.monstro.vida

            self.adicionar_log(f"{habilidade} causou {dano_real} de dano.")

        elif "cura" in dados:

            cura = dados["cura"]

            self.jogador.vida += cura

            if self.jogador.vida > self.jogador.vida_maxima:
                self.jogador.vida = self.jogador.vida_maxima

            sucesso(f"\n{self.jogador.nome} recuperou {cura} de vida!")

            self.adicionar_log(f"{self.jogador.nome} recuperou {cura} de vida.")

        elif "defesa" in dados:

            bonus = dados["defesa"]

            self.jogador.defesa += bonus

            sucesso(f"\nDefesa aumentada em {bonus}!")

            self.adicionar_log(f"Defesa aumentada em {bonus}.")
