# 1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
# nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
# informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# -----------------------------
# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65
# -----------------------------

nome = input ("Entre com o nome: ")
cpf = input ("Entre com o CPF: ")
idade = input ("Entre com a idade: ")

print(f"""
-----------------------------
Confirmação de cadastro:
Nome: {nome}
CPF: {cpf}
Idade: {idade}
-----------------------------
""")

# 2) Escreva um script em Python que receba dois números e que seja realizado as seguintes
# operações:
# • soma dos dois números
# • diferença dos dois números
# O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
# 4 e 2:

# ------------------------------
# Soma: 4 + 2 = 6
# Diferença: 4 - 2 = 2

primeiro_numero = int(input ("Entre com o 1 número: "))
segundo_numero = int(input ("Entre com o 2 número: "))
soma = primeiro_numero + segundo_numero
diferenca = primeiro_numero - segundo_numero

print(f"""
-----------------------------
Soma {primeiro_numero} + {segundo_numero} = {soma}
Diferença {primeiro_numero} - {segundo_numero} = {diferenca}
-----------------------------
""")



