from personagens.personagem import Personagem



class Guerreiro(Personagem):


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


        self.vida += 50
        self.defesa += 10

        self.habilidades.add(
            "Golpe Pesado"
        )


        self.habilidades.add(
            "Bloqueio"
        )


    def atacar(self, inimigo):

        dano = self.forca * 2

        print(
            f"{self.nome} usou Golpe Pesado!"
        )

        inimigo.receber_dano(dano)