class Monstro:

    def __init__(self, nome, vida, ataque, defesa, nivel, xp, ouro):

        self.nome = nome

        self.vida = vida
        self.vida_max = vida

        self.ataque = ataque
        self.defesa = defesa

        self.nivel = nivel

        self.xp = xp
        self.ouro = ouro

    def atacar(self, alvo):

        dano = self.ataque - alvo.defesa

        if dano < 0:
            dano = 0

        print(f"{self.nome} atacou!")

        alvo.receber_dano(dano)

    def receber_dano(self, dano):

        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu {dano} de dano!")

    def esta_vivo(self):

        return self.vida > 0

    def mostrar_status(self):

        print(f"""
 {self.nome}

 Vida:
{self.vida}/{self.vida_max}

 Ataque:
{self.ataque}

 Defesa:
{self.defesa}

Nível:
{self.nivel}
""")
class Goblin(Monstro):


    def __init__(self):

        super().__init__(
            nome="Goblin",
            vida=50,
            ataque=10,
            defesa=3,
            nivel=1,
            xp=20,
            ouro=10
        )
class Lobo(Monstro):


    def __init__(self):

        super().__init__(
            nome="Lobo Selvagem",
            vida=80,
            ataque=15,
            defesa=5,
            nivel=2,
            xp=40,
            ouro=20
        )
class Dragao(Monstro):


    def __init__(self):

        super().__init__(
            nome="Dragão de Eldoria",
            vida=300,
            ataque=40,
            defesa=15,
            nivel=10,
            xp=500,
            ouro=200
        )
class Urso(Monstro):

     def __init__(self):

        super().__init__(
            nome="Urso Tibers",
            vida=180,
            ataque=24,
            defesa=10,
            nivel=6,
            xp=200,
            ouro=60
        )
class Monge(Monstro):

     def __init__(self):

        super().__init__(
            nome="Monge cego",
            vida=120,
            ataque=18,
            defesa=8,
            nivel=4,
            xp=80,
            ouro=35
        )
class Troglodita(Monstro):

    def __init__(self):

        super().__init__(
            nome="Troglodita esquecido",
            vida=400,
            ataque=45,
            defesa=20,
            nivel=12,
            xp=600,
            ouro=260
        )