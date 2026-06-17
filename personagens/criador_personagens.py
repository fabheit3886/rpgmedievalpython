from personagens.guerreiro import Guerreiro
from personagens.mago import Mago
from personagens.arqueiro import Arqueiro



class CriadorPersonagem:


    def criar(self):

        print("===================")
        print(" CRIAÇÃO DE HERÓI ")
        print("===================")


        nome = input(
            "Nome do personagem: "
        )


        pontos = 15


        atributos = {
            "forca": 0,
            "agilidade": 0,
            "inteligencia": 0
        }



        while pontos > 0:


            print(
                f"""
Pontos restantes: {pontos}

1 - Força: {atributos["forca"]}
2 - Agilidade: {atributos["agilidade"]}
3 - Inteligência: {atributos["inteligencia"]}
"""
            )


            escolha = input(
                "Escolha onde colocar ponto: "
            )



            if escolha == "1":

                atributos["forca"] += 1


            elif escolha == "2":

                atributos["agilidade"] += 1


            elif escolha == "3":

                atributos["inteligencia"] += 1


            else:

                print(
                    "Opção inválida"
                )

                continue


            pontos -= 1



        return self.criar_classe(
            nome,
            atributos
        )



    def criar_classe(
        self,
        nome,
        atributos
    ):


        forca = atributos["forca"]
        agilidade = atributos["agilidade"]
        inteligencia = atributos["inteligencia"]



        if forca >= inteligencia + 3:


            print(
                "Classe escolhida: Guerreiro ⚔"
            )


            return Guerreiro(
                nome,
                forca,
                agilidade,
                inteligencia
            )



        elif inteligencia >= forca + 3:


            print(
                "Classe escolhida: Mago 🧙"
            )


            return Mago(
                nome,
                forca,
                agilidade,
                inteligencia
            )



        elif agilidade >= forca + 2:


            print(
                "Classe escolhida: Arqueiro 🏹"
            )


            return Arqueiro(
                nome,
                forca,
                agilidade,
                inteligencia
            )



        else:


            print(
                "Classe escolhida: Aventureiro"
            )


            return Guerreiro(
                nome,
                forca,
                agilidade,
                inteligencia
            )