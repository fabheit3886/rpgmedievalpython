class Equipamento:

    def __init__(self, nome, ataque=0, defesa=0):

        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa


espada_ferro = Equipamento("Espada de Ferro", ataque=5)

arco_reforcado = Equipamento("Arco Reforçado", ataque=5)

cajado_antigo = Equipamento("Cajado Antigo", ataque=5)

armadura_couro = Equipamento("Armadura de Couro", defesa=3)
