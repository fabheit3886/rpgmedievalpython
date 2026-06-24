import json
import os
from personagens.guerreiro import Guerreiro
from personagens.mago import Mago
from personagens.arqueiro import Arqueiro

CAMINHO_SAVE = "saves/save.json"


def salvar(jogador):

    dados = {
        "classe": jogador.__class__.__name__,
        "nome": jogador.nome,
        "vida": jogador.vida,
        "mana": jogador.mana,
        "vida_maxima": jogador.vida_maxima,
        "mana_maxima": jogador.mana_maxima,
        "forca": jogador.forca,
        "agilidade": jogador.agilidade,
        "inteligencia": jogador.inteligencia,
        "nivel": jogador.nivel,
        "xp": jogador.xp,
        "xp_proximo_nivel": jogador.xp_proximo_nivel,
        "ouro": jogador.ouro,
        "capitulo_atual": jogador.capitulo_atual,
        "inventario": jogador.inventario,
        "habilidades": jogador.habilidades,
        "escolhas": jogador.escolhas,
    }

    os.makedirs("saves", exist_ok=True)

    with open(CAMINHO_SAVE, "w", encoding="utf-8") as arquivo:

        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar():

    if not os.path.exists(CAMINHO_SAVE):

        return None

    with open(CAMINHO_SAVE, "r", encoding="utf-8") as arquivo:

        dados = json.load(arquivo)

    classe = dados["classe"]

    if classe == "Guerreiro":

        jogador = Guerreiro(
            dados["nome"], dados["forca"], dados["agilidade"], dados["inteligencia"]
        )

    elif classe == "Mago":

        jogador = Mago(
            dados["nome"], dados["forca"], dados["agilidade"], dados["inteligencia"]
        )

    else:

        jogador = Arqueiro(
            dados["nome"], dados["forca"], dados["agilidade"], dados["inteligencia"]
        )

    jogador.vida = dados["vida"]
    jogador.mana = dados["mana"]

    jogador.vida_maxima = dados["vida_maxima"]
    jogador.mana_maxima = dados["mana_maxima"]

    jogador.nivel = dados["nivel"]

    jogador.xp = dados["xp"]
    jogador.xp_proximo_nivel = dados["xp_proximo_nivel"]

    jogador.ouro = dados["ouro"]
    jogador.capitulo_atual = dados.get("capitulo_atual", 1)
    jogador.inventario = dados["inventario"]

    jogador.habilidades = dados["habilidades"]

    jogador.escolhas = dados["escolhas"]

    return jogador


def apagar_save():

    if os.path.exists(CAMINHO_SAVE):

        os.remove(CAMINHO_SAVE)
