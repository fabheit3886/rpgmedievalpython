from personagens.criador_personagens import CriadorPersonagem
from combate.monstros import Goblin
from combate.batalha import Batalha



criador = CriadorPersonagem()


jogador = criador.criar()


goblin = Goblin()



batalha = Batalha(
    jogador,
    goblin
)


batalha.iniciar()