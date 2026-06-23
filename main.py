from personagens.criador_personagens import CriadorPersonagem
from mundo.historia import Historia

criador = CriadorPersonagem()

jogador = criador.criar()

historia = Historia(jogador)

historia.iniciar()
