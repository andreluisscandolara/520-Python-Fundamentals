import os

# 1) Escreva um script em Python que substitua o caractere “x” por espaço considerando a
# seguinte frase:
# “Umxpratoxdextrigoxparaxtrêsxtigresxtristes”

frase = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
frase=frase.replace("x", " ")
print(frase)


# ======================================================================================================
# 2) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
# a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
# seguinte tabela:

# Geração        Intervalo

# Baby Boomer -> Até 1964
# Geração X   -> 1965 - 1979
# Geração Y   -> 1980 - 1994
# Geração Z   -> 1995 - Atual

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:

# • ano nascimento = 1988: Geração: Y
# • ano nascimento = 1958: Geração: Baby Boomer
# • ano nascimento = 1996: Geração: Z

# ano = int(input("Qual o ano de seu nascimento?: "))

if ano <= 1964:
    print(f"ano de nascimento = {ano}: Geração Baby Boomer")
elif ano <= 1979:
    print(f"ano de nascimento = {ano}: Geração X")
elif ano <= 1994:
    print(f"ano de nascimento = {ano}: Geração Y")
else:
    print(f"ano de nascimento = {ano}: Geração Z")


# ======================================================================================================
# 3) Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# Menu principal:

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair

# Menu de frutas:
# Digite a opção desejada:
# Escolha fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Digite à opção desejada: 2
# Melancia adicionada com sucesso!


# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem:
# Digitado uma opção inválida

# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.

cesta = []

while True:
    print("""
        Quitanda:
        1: Ver cesta
        2: Adicionar frutas
        3: Sair

        """)

    opcao = input("Selecione uma das opções acima. ")

    if opcao == "1":
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

    elif opcao == "2":
        while True:
            print("""
            Menu de frutas:
            Escolha fruta desejada:
            1 - Banana
            2 - Melancia
            3 - Morango
                
            """)

            opcao_fruta = input("Selecione a fruta para adicionar na cesta. ")

            if opcao_fruta == "1":
                cesta.append("Banana")
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print("'Banana' foi adicionada a cesta.")
                break
            elif opcao_fruta == "2":
                cesta.append("Melancia")
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print("'Melancia' foi adicionada a cesta.")
                break
            elif opcao_fruta == "3":
                cesta.append("Morango")
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

    elif opcao == "3":
        print("Finalizando programa")
        break

    else:
        print("Valor inválido, digite novamente.")



# ======================================================================================================
# 4) Altere o exercicio numero 3 para adicionar o preço dos itens comprados, mantendo uma conta do valor
# total gasto nas compras, e no fim, imprima o valor total e os itens na cesta de compras.

cesta = []
valor_gasto = 0

while True:
    print("""
        Quitanda:
        1: Ver cesta
        2: Adicionar frutas
        3: Sair

        """)

    opcao = input("Selecione uma das opções acima. ")

    if opcao == "1":
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

    elif opcao == "2":
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

    elif opcao == "3":
        print(f"""Conteúdo da cesta: {cesta}
Valor gasto: R${valor_gasto:.2f}
""")
        break

    else:
        print("Valor inválido, digite novamente.")



