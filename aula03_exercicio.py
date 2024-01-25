import os
import math

# Exercicio 1:
# Escreva uma função que receba um nome e que tenha como saída uma saudação.

# O argumento da função deverá ser o nome, e saída deverá ser como a seguir:

# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'

#Exemplo 1
def saudacao(nome):
    print(f"Olá {nome}! Tudo bem com você?")

nome = input("Qualo seu nome?: ")

saudacao(nome)

#Exemplo 2
def saudacao(nome):
    return(f"""
    Chamada da função: saudação('{nome}')
    Saída: 'Olá {nome}! Tudo bem co você?'
    """)
resp = input("Qual é o seu nome?: ")
print(saudacao(resp))

# ====================================================
# Exercicio 2:
# Escreva uma calculadora utilizando funções
# Ela pergunta dois numeros, e da as opções de calculo.
# (soma, diferença, multiplicação, divisão)

#Exemplo 1
def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
        return resultado
    elif operacao == 2:
        resultado = num1 - num2
        return resultado
    elif operacao == 3:
        resultado = num1 * num2
        return resultado
    elif operacao == 4:
        resultado = num1 / num2
        return resultado

num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))

while True:
        print("""
        Operações:
        1 - Soma
        2 - Subtracção
        3 - Multiplicação
        4 - Divisão
                
        """)

        operacao = int(input("Selecione a operação desejada. "))
      
        print(calculadora(num1, num2, operacao))

        break

#Exemplo 2
def calculadora(valor1, valor2, operacao):
    if operacao == "1":
        return(f"O resultado da soma entre {valor1} e {valor2} é {valor1 + valor2}")
    elif operacao == "2":
        return(f"O resultado da diferença entre {valor1} e {valor2} é {valor1 - valor2}")
    elif operacao == "3":
        return(f"O resultado da multiplicação entre {valor1} e {valor2} é {valor1 * valor2}")
    elif operacao == "4":
        if valor2 == 0.0:
            return("Não é possivel dividir um numero por zero.")
        else:
            return(f"O resultado da divisão de {valor1} por {valor1} é {valor1 / valor2:.2f}")
    else:
        return("O valor indicado para a operação é inválido")
    
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

escolha = input(f"""
Escolha o que fazer com os numeros {n1} e {n2}:
1 - Somá-los
2 - Subtraí-los
3 - Multiplicá-los
4 - Dividí-los
""")

print(calculadora(n1, n2, escolha))


# ====================================================
# Exercicio 3:
# Reescreva o exercício da quitanda do capítulo 2 separando as operações 
# em funções.

cesta = []
valor_gasto = 0

def verCesta():
    if len(cesta) < 1:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("A cesta está vazia")
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(cesta)

def menuFrutas():
    global valor_gasto
    while True:
        print("""
        Menu de frutas:
        Escolha fruta desejada:
        1 - Banana   R$2.50
        2 - Melancia R$8.00
        3 - Morango  R$6.00
            
        """)

        opcao_fruta = input("Selecione a fruta para adicionar na cesta. ")

        if opcao_fruta == "1":
            cesta.append("Banana")
            valor_gasto = valor_gasto + 2.50
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("'Banana' foi adicionada a cesta.")
            break
        elif opcao_fruta == "2":
            cesta.append("Melancia")
            valor_gasto = valor_gasto + 8.00
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("'Melancia' foi adicionada a cesta.")
            break
        elif opcao_fruta == "3":
            cesta.append("Morango")
            valor_gasto = valor_gasto + 6.00
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("'Morango' foi adicionada a cesta.")
            break
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("Valor inválido, digite novamente.")

def checkout():
    print(f"""Conteúdo da cesta: {cesta}
Valor gasto: R${valor_gasto:.2f}
""")

while True:
    print("""
        Quitanda:
        1: Ver cesta
        2: Adicionar frutas
        3: Sair

        """)

    opcao = input("Selecione uma das opções acima. ")

    if opcao == "1":
        verCesta()

    elif opcao == "2":
        menuFrutas()

    elif opcao == "3":
        checkout()
        break

    else:
        print("Valor inválido, digite novamente.")


# ====================================================
# Exercicio 4:
# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.

def pares(lista):
    if len(lista) < 1:
        return("A lista está vazia")

    numeros_pares = 0

    for x in lista:
        if x % 2 == 0:
            numeros_pares += 1

    return(f"{numeros_pares} numeros pares foram encontrados na lista")

numeros = []

while True:
    valor = int(input("Escolha um numero para adicionar a lista, ou digite 999 para fechar: "))
    if valor == 999:
        break
    numeros.append(valor)

print(pares(numeros))



# ====================================================
# Exercicio 5:
# Assumindo que uma lata de tinta pinta 3m², escreva um programa
# que possua uma função que receba as dimenções de uma parede,
# passadas pelo usuario, calcule sua área, e mostre uma mensagem
# dizendo quantas latas de tinta seriam necessárias para pintar
# essa parede.

def tinta(x, y):
    area = x * y
    latas = area / 3

    return(f"Seriam necessárias {math.ceil(latas)} latas de tinta para pintar essa parede.")

altura = float(input("Qual a altura da parede em metros? "))
largura = float(input("Qual a largura da parede em metros? "))

print(tinta(altura, largura))


