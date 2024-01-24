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

#DICIONARIO - Hash table

dicionario = {}
for x in dicionario():
    print(x)

for x in dicionario.items():
    print(x)

for x in dicionario.keys():
    print(x)

for x in dicionario.values():
    print(x)

for x, y in dicionario.items():
    print(f"Cahve: {x}, Valor: {y}")

#SETS
variavel_sets = {}
variavel_sets = {10, 15, 30, "teste", 15}
variavel_sets = set(variavel_sets)
variavel_sets.add(20)

print (variavel_sets)

































