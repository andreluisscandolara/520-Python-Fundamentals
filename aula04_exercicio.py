import random
import time

# 1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
# deverá ser apresentado vencedor.

# Dica: [OPCIONAL] Você poderá utilizar o modulo "time" para simular um tempo de a cada rodada para criar
# um efeito mais interessante.

# Dica: [OPCIONAL] Tentem fazer a remoção de uma pessoa aleatória por rodada sem utilizar a função "choice".

#Exemplo 1
def jogo(lista):
    if len(lista) !=10:
        print("O jogo precisa ter 10 participantes")
    while len(lista) > 1:
        tempo = random.uniform(2, 5)
        time.sleep(tempo)
        removido = random.choice(lista)
        lista.remove(removido)

    print(f"Vencedor foi {lista[0]}.")

participantes = ["André", "Luiz", "Maria", "Rodrigo", "Adriana", "Beatriz", "Thaís", "Bob", "MacGyver", "Lua"]

jogo(participantes)

# =============================================================
# 2) Crie um programa utilizando dois arquivos, onde um deles possui todas as funcçoes utilizadas na aplicação.
# Onde o programa deverá perguntar ao usuario nome/idade de uma pessoa, e armazenar esses valores em um dicionario,
# e repetir essa ação até que a pessoa não queira mais adicionar nomes, em seguida, o programa deverá mostrar o numero
# de pessoas em categorias de acordo com a idade:
# 0-17 anos: Menor de idade
# 18-59 anos: Adulto
# 60+ anos: Idoso
# E deverá perguntar para o usuario se ele gostaria de exibir na tela uma lista com os nomes das pessoas de cada grupo,
# ou se o usuario deseja finalizar o programa.

dicionario = {}

while True:
    print("""
        Escolha a opção:
        1: Entre com os dados
        2: Sair

        """)

    opcao = input("Selecione uma das opções acima. ")

    if opcao == "1":
        nome = input("Qual seu nome?: ")
        dicionario.update({nome},{idade})
      
    elif opcao == "2":
        print("Saindo do programa...")

        break


print(dicionario)




# =============================================================
# 3) Crie um programa que pergunte para o usuario um numero de pessoas a participarem de um sorteio (2-20),
#  e o numero de pessoas a serem sorteadas, e depois sorteie esse numero de pessoas da lista.

# O programa deverá pegar o numero de pessoas a participar aleatoriamente desta lista:

# lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
# "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
# "Benedito", "Tereza", "Valmir", "Joaquim"]

# Nota: A mesma pessoa não pode ganhar duas vezes.




