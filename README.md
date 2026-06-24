# rpgmedievalpython
# 🏰 RPG Medieval em Python

Um RPG de texto desenvolvido em Python utilizando Programação Orientada a Objetos.

O jogo possui criação de personagens, combate por turnos, sistema de níveis, história ramificada, cidade com NPCs, guilda de missões e sistema de salvamento.

---

# 📖 Índice

- Sobre o projeto
- Funcionalidades
- Estrutura do projeto
- Tecnologias utilizadas
- Instalação
- Como jogar
- Tutorial
- Sistema de Personagens
- Sistema de Combate
- Sistema de História
- Cidade de Eldoria
- Sistema de Save
- UML
- Programação Orientada a Objetos
- Melhorias Futuras

---

# 📜 Sobre o Projeto

RPG Medieval é um jogo de terminal desenvolvido em Python com foco em:

- Programação Orientada a Objetos
- Modularização
- Reutilização de código
- Narrativa interativa
- Expansão futura

O jogador cria um herói e embarca em uma jornada por Eldoria enfrentando monstros, fazendo escolhas e evoluindo durante a aventura.

---

# ⚔ Funcionalidades

### ✔ Criação de Personagem

- Guerreiro
- Mago
- Arqueiro

### ✔ Sistema de Combate

- Turnos
- Habilidades
- Mana
- Ataques
- Defesa

### ✔ Sistema de Níveis

- XP
- Evolução
- Aumento de atributos

### ✔ História Ramificada

- Capítulos
- Escolhas com consequências

### ✔ Cidade de Eldoria

- Loja
- Estalagem
- Guilda
- NPCs
- Ferreiro

### ✔ Save Automático

- Salvar progresso
- Continuar partida

### ✔ Interface Estilizada

- Barras de vida
- Cores
- Efeitos de escrita

---

# 📁 Estrutura do Projeto

```
RPGMEDIEVALPYTHON

cidade/
combate/
itens/
menus/
missoes/
mundo/
personagens/
saves/
utils/

main.py
README.md
```

---

# 🛠 Tecnologias Utilizadas

- Python 3
- Colorama
- Pickle
- Random
- Time
- OS

---

# 🚀 Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd RPGMEDIEVALPYTHON
```

Instale o Colorama:

```bash
pip install colorama
```

Execute:

```bash
python main.py
```

---

# 🎮 Como Jogar

Ao iniciar o jogo aparecerá o menu principal:

```
1 - Novo Jogo
2 - Continuar
3 - Bestiário
4 - Créditos
5 - Sair
```

---

# 📚 Tutorial

## Criando o Personagem

Escolha:

- Nome
- Classe

Classes disponíveis:

### Guerreiro

Especialista em força e resistência.

### Mago

Especialista em magia e inteligência.

### Arqueiro

Especialista em agilidade e precisão.

---

# ⚔ Sistema de Combate

Durante uma batalha existem quatro opções:

```
1 - Atacar
2 - Habilidades
3 - Status
4 - Inventário
```

### Atacar

Realiza dano baseado nos atributos do personagem.

### Habilidades

Consomem mana e possuem efeitos especiais.

### Status

Exibe informações do personagem.

### Inventário

Permite utilizar itens.

---

# ⭐ Sistema de Evolução

Ao derrotar monstros o jogador recebe:

- XP
- Ouro

Ao subir de nível os atributos aumentam automaticamente.

---

# 📖 História

## Capítulo 1

Escolha entre:

- Floresta
- Caverna

---

## Capítulo 2

As escolhas do primeiro capítulo influenciam o segundo.

Eventos:

- Acampamento abandonado
- Mercador perdido
- Santuário antigo
- Túnel profundo

---

## Capítulo 3

Chegada à cidade de Eldoria.

---

## Capítulo 4

Continuação da jornada nas Ruínas de Arkan.

---

# 🏰 Cidade de Eldoria

## Loja

Compra de itens.

## Estalagem

Recupera vida e mana.

## Guilda

Recebe missões.

## Ferreiro

Melhoria de equipamentos.

## NPCs

Diálogos e informações.

---

# 👹 Bestiário

Monstros disponíveis:

### Goblin

- Vida: 50

### Lobo Selvagem

- Vida: 80

### Urso Tibers

- Vida: 180

### Monge Cego

- Vida: 120

### Dragão de Eldoria

- Vida: 300

### Troglodita Esquecido

- Vida: 400

---

# 💾 Sistema de Save

O jogo salva:

- Nome
- Classe
- Vida
- Mana
- Nível
- XP
- Ouro
- Inventário
- Escolhas
- Capítulo atual

Funções:

```python
salvar()
carregar()
apagar_save()
```

---

# 🧩 Programação Orientada a Objetos

Conceitos aplicados:

### Encapsulamento

Organização dos atributos e métodos.

### Herança

Classes derivadas:

```
Personagem
│
├── Guerreiro
├── Mago
└── Arqueiro
```

```
Monstro
│
├── Goblin
├── Lobo
├── Dragão
└── ...
```

### Polimorfismo

Métodos reutilizados por diversas classes.

### Modularização

Separação por responsabilidade.

---

# 📊 UML

Principais classes:

- Personagem
- Guerreiro
- Mago
- Arqueiro
- Batalha
- Monstro
- Goblin
- Lobo
- História
- Capítulo1
- Capítulo2
- Capítulo3
- Capítulo4
- Loja
- Guilda
- Estalagem
- NPC
- Save

---

# 🔮 Melhorias Futuras

- Sistema de equipamentos
- Mais cidades
- Chefes especiais
- Árvores de habilidades
- Classes avançadas
- Mais capítulos
- Mapa em ASCII
- Sistema de quests complexo
- Eventos aleatórios
- Magias elementais

---

# 👨‍💻 Autores

Fabio Heitor Bezerra Pires
Isaías Marques da Silva
Állef Braz da Silva Santos

Projeto desenvolvido para estudo de:

- Python
- Programação Orientada a Objetos
- Estruturas de Dados
- Desenvolvimento de Jogos

---

# 🧑‍🏫 Professora responsável

Priscilla Suene de Santana Nogueira Silverio

---

# ⚜ "Toda grande aventura começa com uma escolha."