from combate.monstros import Monstro


class GuardiaoArkan(Monstro):

    def __init__(self):

        super().__init__(
            nome="Guardião de Arkan",
            vida=250,
            ataque=30,
            defesa=12,
            nivel=8,
            xp=300,
            ouro=150,
        )
