from personagens.personagem import Personagem


class Mago(Personagem):


    def __init__(
        self,
        nome,
        forca,
        agilidade,
        inteligencia
    ):

        super().__init__(
            nome,
            forca,
            agilidade,
            inteligencia
        )


        self.mana += 100


        self.habilidades.add(
            "Bola de Fogo"
        )


    def atacar(self, inimigo):

        if self.mana < 20:

            raise Exception(
                "Mana insuficiente"
            )


        dano = self.inteligencia * 3


        self.mana -= 20


        print(
            f"{self.nome} lançou Bola de Fogo!"
        )


        inimigo.receber_dano(dano)