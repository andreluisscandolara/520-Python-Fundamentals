# # Isso e um comentário
# # No python frases entre aspas duplas ou simpleas são STRINGS
# # Ctrl + / comenta ou descomenta linhas selecionas

# # PRINT é usado para imprimir/enviar mensagems ao usuário
# print("Meu nome é André")

# # INPUT é usado para coletar informações do usuário
# input("Qual é seu nome do meio?:")

# # Váriaves
# nome = "André Luís"
# idade = '27'

# print(nome)
# print('nome')

# nome = input("Qual o seu nome?: ")
# print("Bem vindo, "+ nome +"!")
# print("Bem vindo, {}!".format(nome))
# print(f"Bem vindo, {nome}!")

# # Tipos primitivos
# # String  = str   = frases, cadeias de caracteres.
# # Float   = float = números reais com ponto
# # Integer = int   = números inteiros
# # Boolean = bool  = True ou False

# variavel_str = "Avião azul"
# variavel_str2 = " está caindo"
# variavel_float = 25.7
# variavel_int = 40
# variavel_bool = False

# print(variavel_str + variavel_str2)
# print(variavel_float + variavel_int)

# # IF - Condição
# idade = int(input("Qual é a sua idade? "))

# if idade ==+ 18:
#     print("Voce é maior de idade.")

# elif idade > 15:
#     print("Voce tem pelo menos 15 anos.")

# elif idade > 10:
#     print("Voce tem pelo menos 10 anos.")

# else:
#     print("Voce tem menos de 10 anos.")

# #FOR / WHILE - repetição
# #FOR
# for numero in range (1, 10):
#     print(numero)

# #WHILE
# resposta = "nao"
# while resposta != "sim":
#     print("Imprimindo mensagem do loop")
#     resposta = input("Quer para o loop? [sim/nao] ")

# while True:
#     resposta = input("Quer para o loop? [sim/nao] ")
#     if resposta == "sim":
#         break

# #TUPLA / LISTA / DICIONARIO /SET - Coleções
# #TUPLA
# #Tuplas não podem ser editadas
# tupla = ("Beterraba", "Mandioca", "Batata", 50, True)
# #Index       0            1           2      3    4 
# print(tupla)
# print(tupla[3])

# for item in tupla:
#     print(item)
#     print(f"O objeto {item} é um {type(item)}")

# #LISTA
# #Listas podem ser editadas
# lista = ["Beterraba", "Mandioca", "Batata", 50, True]
# #Index       0            1           2      3    4 
# lista.append("Pão de batata")
# lista.remove(50)
# lista.pop(0)
# lista.insert(2, "Avião")
# print(lista)

# frase = "Um cachorro me mordeu"
# print(frase.replace("c", "---"))
# print(frase)
# frase=frase.replace("c", "---")
# print(frase)

# #DICIONARIO - Hash table
# #chave -> valor

# dicionario = {"Altura": 1.80}

# dicionario["Nome"] = "Tiago"
# dicionario["Cor"] = "Verde"

# #              |------ITEM----|  |----ITEM-----|
# # DICIONARIO = {'Nome': 'Tiago', 'Cor': 'Verde'}
# #               CHAVE  :  VALOR,  CHAVE: VALOR

# dicionario = {}
# for x in dicionario():
#     print(x)

# for x in dicionario.items():
#     print(x)

# for x in dicionario.keys():
#     print(x)

# for x in dicionario.values():
#     print(x)

# for x, y in dicionario.items():
#     print(f"Cahve: {x}, Valor: {y}")

# #SETS
# variavel_sets = {}
# variavel_sets = {10, 15, 30, "teste", 15}
# variavel_sets = set(variavel_sets)
# variavel_sets.add(20)

# print (variavel_sets)

# #FUNÇÕES
# def soma():
#     print("Você está usando uma função")

# soma()

# def soma(x, y):
#     resultado = x + y
#     print(resultado)

# soma(5, 8)
# soma(4, 2)
# soma(3, 3)

# def soma(x, y):
#     resultado = x + y
#     return resultado

# print(soma(5, 8))
# print(soma(4, 2))
# print(soma(3, 3))

# #FUNÇÕES LAMBDA / FUNÇÕES ANÔNIMAS
# diferenca = lambda x, y: x - y

# print(diferenca(7, 5))


# # DUNDER __name__
# def final():
#     print("Finalizando o teste.")

# def main():
#     print("Inicializando o teste.")
#     final()

# if __name__ == "__main__":
#     main()

# #MÓDULOS
# #MÓDULOS NATIVOS
# import os
# os.system()          

# from os import system
# system()

# #MÓDULOS BAIXADOS COM PIP
# pip3 install flask

# #==================
# #MÓDULO RANDOM
# import random

# random.choice()
# random.random(1, 100)
# random.randint(1, 100)

# #break -> pára o loop completamente
# #continue -> continua pula para o proximo lopp
# #pass -> continua a execução do código

# #HELP DE COMANDOS
# help(open) #help comando open

# #MANIPULAÇÃO DE ARQUIVOS
# #r -> read
# #w -> escrita (sobescreve)
# #a -> append
# #+ -> leitura e escrita

# arquivo = open("texto.txt", "w")
# conteudo = "Primeira linha do arquivo"
# arquivo.write(conteudo)
# arquivo.close()

# arquivo = open("texto.txt", "a")
# conteudo = "\nSegunda linha do arquivo"
# arquivo.write(conteudo)
# arquivo.close()

# arquivo = open("texto.txt", "r")
# conteudo = arquivo.readlines()
# for linha in conteudo:
#     print(linha, end="")
# arquivo.close()

# #ARQUIVOS .CSV
# import csv

# with open("registro.csv", "r") as arquivo:
#     conteudo = csv.reader(arquivo, delimiter=";")
#     # cabecalho = next(conteudo)
#     # primeira_linha = next(conteudo)
#     # segunda_linha = next(conteudo)
#     # terceira_linha = next(conteudo)

#     lista_conteudo = []

#     for linha in conteudo:
#         lista_conteudo.append(linha)

#     for linha in lista_conteudo:
#         print(linha)

# #--------------------------------------------
# with open("registro.csv", "a", newline="") as arquivo:
#     escrita=csv.writer(arquivo, delimiter=";")

#     escrita.writerow(["444444444", "André", "49", "M", "Brasileiro"])


# #CASE / MATCH -> python 3.10 e superiores
# def verificanome(nome):
#     match nome:
#         case "André":
#             print("Nome bonito")
#         case "Bob":
#             print("O apelido é Bobito")
#         case "MacGyver":
#             print("O apelido é Bebezão")
#         case _:
#             print("Nomes inválidos")

# nome = input("Qual o nome?: ")

# verificanome(nome)

# #ESCOPO / SCOPE
# x = 300 #variável Global. Escopo Global

# def funcao():
#     #global x
#     x =  250 #variável Local. Escopo Local
 
# funcao()
# print(x)

# #CLASS / CLASSES
# #Crie uma classe pra simular uma pilha, onde itens só podem ser removidos do topo.

# class Pilha:

#     def __init__(self):
#         self.__pilha = []
#         self.__topo = 0 #Ecapsulamento -> variáveis começando com __

#     def empilhar(self, item):
#         self.__pilha.append(item)
#         self.__topo += 1

#     def desempilhar(self):
#         if self.__topo > 0:
#             ultimo_item = self.__pilha[-1]
#             self.__pilha.remove(ultimo_item)
#             self.__topo -= 1
#             return "Item removido"
#         else:
#             return "Nenhum item empilhado"
        
#     def checar(self):
#         return self.__pilha
        
# balcao = Pilha()

# balcao.empilhar("Prato de vidro verde")
# balcao.empilhar("Prato de porcelana azul")
# balcao.empilhar("Prato de metal")
# balcao.empilhar("Prato de madeira")

# print(balcao.checar())

# balcao.desempilhar()
# balcao.desempilhar()

# #Encapsulamento
# print(balcao.checar())

# #Herança
# class Funcionario:

#     def __init__(self):
#         self.__nome = ""
#         self.__idade = 0
#         self.__salario = 0


# class Gerentes(Funcionario):

#     def __init__(self):
#         super().__init__()
#         self.__bonus = "25%"


# #Polimorfismo -> herda caracteristicas de outras classas e também as alteras
# class Cliente:

#     def __init__(self):
#         self.carrinho = []
#         self.cpf = ''
#         self.total = 0

#     def adicionar_item(self, item):
#         self.carrinho.append(item)

#     def caixa(self):
#         for item in self.carrinho:
#             self.total += 1.99
#         return self.total
    
# class ClienteVIP(Cliente):

#     def __init__(self):
#         super().__init__()
#         self.desconto = 0.95

#     def caixa(self):
#         for item in self.carrinho:
#             self.total += 1.99
#         return self.total * self.desconto






