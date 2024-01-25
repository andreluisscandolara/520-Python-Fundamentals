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


# ====================================================
# Exercicio 2:
# Escreva uma calculadora utilizando funções
# Ela pergunta dois numeros, e da as opções de calculo.
# (soma, diferença, multiplicação, divisão)

#Exemplo 2
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


# ====================================================
# Exercicio 3:
# Reescreva o exercício da quitanda do capítulo 2 separando as operações 
# em funções.


# ====================================================
# Exercicio 4:
# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.


# ====================================================
# Exercicio 5:
# Assumindo que uma lata de tinta pinta 3m², escreva um programa
# que possua uma função que receba as dimenções de uma parede,
# passadas pelo usuario, calcule sua área, e mostre uma mensagem
# dizendo quantas latas de tinta seriam necessárias para pintar
# essa parede.

def qtdlatas(base, altura):
    area == base * altura
    qtd == area / 3
    


