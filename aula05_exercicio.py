# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

def isVowel(letra):
    if letra.lower() in "aeiouáéíóúãẽĩõũâêîôûàèìòùäëïöü":
        return True
    else:
        return False

vogais = 0
consoantes = set()

# conteudo = ["asdasdas", "asdasd", "asdasd"]
# #                0          1         2

# linha    = "asdasdasda"
# #           0123456789

with open("faroeste.txt", "r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        for letra in linha:
            if isVowel(letra) == True:
                vogais += 1
            else:
                consoantes.add(letra)

print(f"Vogais: {vogais}")
print(f"Consoantes:\n {consoantes}")


# ====================================================================================
# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
# seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Endereço

# Os registros deverão ser armazenados em um arquivo CSV. Caso desejar manter o padrão
# brasileiro, o CSV será separado pelo caractere ;

import csv


while True:
    opcao = input("Gostaria de cadastrar uma nova entrada no banco? [S/N]")

    if opcao.lower() == "n":
        print("Parando a execução")
        break
    
    elif opcao.lower() == "s":
        cpf = input("Qual o CPF da pessoa? ")
        nome = input("Qual o nome da pessoa? ")
        idade = input("Qual o idade da pessoa? ")
        sexo = input("Qual o sexo da pessoa? ")
        endereco = input("Qual o endereço da pessoa? ")

        pessoa = (cpf, nome, idade, sexo, endereco)

        with open("banco.csv", "a+", newline="") as arquivo:
            conteudo = csv.writer(arquivo, delimiter=";")
            conteudo.writerow(pessoa)

        print(f"'{nome}' cadastrada no banco com sucesso.")

    else:
        print("Por favor, digite apenas 'S' ou 'N'.")

# ====================================================================================
# 3) Implemente uma função de consulta no programa do exercício 2.
# import csv

def consulta():
    resposta = int(input("""Qual valor deseja consultar?
0 - CPF
1 - Nome 
"""))

    valor = input("Digite o CPF/Nome a consultar: ")

    with open("banco.csv", "r") as arquivo:
        conteudo = csv.reader(arquivo, delimiter=";")
        for linha in conteudo:
            if linha[resposta] == valor:
                print(f"""Cadastro encontrado:
CPF: {linha[0]}
NOME: {linha[1]}
IDADE: {linha[2]}
SEXO: {linha[3]}
ENDEREÇO: {linha[4]}""")
                
while True:
    opcao = input("""Digite uma opção:
1 - Consultar um valor no banco.
2 - Cadastrar um valor no banco.
3 - Parar o programa.""")

    if opcao == "3":
        print("Parando a execução")
        break
    
    elif opcao == "2":
        cpf = input("Qual o CPF da pessoa? ")
        nome = input("Qual o nome da pessoa? ")
        idade = input("Qual o idade da pessoa? ")
        sexo = input("Qual o sexo da pessoa? ")
        endereco = input("Qual o endereço da pessoa? ")

        pessoa = (cpf, nome, idade, sexo, endereco)

        with open("banco.csv", "a+", newline="") as arquivo:
            conteudo = csv.writer(arquivo, delimiter=";")
            conteudo.writerow(pessoa)

        print(f"'{nome}' cadastrada no banco com sucesso.")

    elif opcao == "1":
        consulta()

    else:
        print("O valor digitado não é válido.")

# ====================================================================================
# 4) Implemente uma função de exclusão no programa do exercício 2.

import os
import csv

def consulta():
    resposta = int(input("""Qual valor deseja consultar?
0 - CPF
1 - Nome 
"""))

    valor = input("Digite o CPF/Nome a consultar: ")

    with open("banco.csv", "r") as arquivo:
        conteudo = csv.reader(arquivo, delimiter=";")
        for linha in conteudo:
            if linha[resposta] == valor:
                print(f"""Cadastro encontrado:
CPF: {linha[0]}
NOME: {linha[1]}
IDADE: {linha[2]}
SEXO: {linha[3]}
ENDEREÇO: {linha[4]}""")

def exculsao(dado_a_excluir):
    with open("banco.csv", "r") as arquivo_inicial, open("banco_editado.csv", "a") as arquivo_final:
        writer = csv.writer(arquivo_final, delimiter=";")

        for linha in csv.reader(arquivo_inicial, delimiter=";"):
            if linha[0] != dado_a_excluir and linha[1] != dado_a_excluir:
                writer.writerow(linha)
        
    os.remove("banco.csv")
    os.rename("banco_editado.csv", "banco.csv")

while True:
    opcao = input("""Digite uma opção:
1 - Consultar um valor no banco.
2 - Cadastrar um valor no banco.
3 - Remover um valor do banco.
4 - Parar o programa.""")

    if opcao == "4":
        print("Parando a execução")
        break
    
    elif opcao == "3":
        entrada = input("Digite o nome ou CPF da pessoa que deseja demover do banco: ")
        exculsao(entrada)
        print(f"Entrada {entrada} removida do banco de dados.")

    elif opcao == "2":
        cpf = input("Qual o CPF da pessoa? ")
        nome = input("Qual o nome da pessoa? ")
        idade = input("Qual o idade da pessoa? ")
        sexo = input("Qual o sexo da pessoa? ")
        endereco = input("Qual o endereço da pessoa? ")

        pessoa = (cpf, nome, idade, sexo, endereco)

        with open("banco.csv", "a+", newline="") as arquivo:
            conteudo = csv.writer(arquivo, delimiter=";")
            conteudo.writerow(pessoa)

        print(f"'{nome}' cadastrada no banco com sucesso.")

    elif opcao == "1":
        consulta()

    else:
        print("O valor digitado não é válido.")
