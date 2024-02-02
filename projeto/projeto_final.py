# Utilizando todo o conteudo que aprendeu no treinamento, crie uma aplicação capaz de simular o 
# funcionamento de um caixa eletrônico. O caixa deverá possuir as seguintes funções:
# - Registrar novos clientes.
# - Fazer login dos clientes.
# - Checar o saldo dos clientes.
# - Realizar depósitos.
# - Realizar saques.

# Faça o uso de Classes, funções e tratamentos de erro para otimizar seu código.

# - Clientes podem ser criados a partir de uma classe.
# - Informações dos clientes, como nome, senha e saldo, podem ser armazenadas em um banco de dados.
# - Podemos criar funções para tomar as ações do caixa eletrônico.
# - Podemos fazer uso de diversos arquivos pra segmentar o nosso código.

# =================================================================================================

# 1° - Criar um arquivo pra lidar com o banco de dados.
# 2° - Criar as tabelas no DB, uma pra armazenar as informações do cliente (nome, idade, saldo)
# e outra pra armazenar os usuarios/senha dos clientes.
# 3° - Criar um arquivo pra armazenar a classes utilizada no programa.
# 4° - Criar um arquivo que conterá as funções executadas pelo programa (registrar, deposito, saque).
# 5° - No meu arquivo principal, eu criariaria um menu para executar o programa.

# 6° - Corrigir valores repetidos sendo adicionados na primeira execução.
# 7° - Fazer um tratamento de erros em todo o programa.
# 8° - Melhorar a qualidade de uso do programa para o cliente. (Melhorar a comunicação)

from lib import teste
from lib import funcao_banco

funcao_banco.criar_banco()

while True:
    escolha = input("""
Bem vindo ao caixa eletrônico:
                    
1 - Se registrar no banco.
2 - Se logar no sistema.
""")
    
    if escolha == "1":
        funcao_banco.registrar()
    elif escolha == "2":
        if funcao_banco.login() == True:
            while True:
                acao = input("""Que ação gostaria de tomar? 

1 - Checar o saldo
2 - Realizar uma transferencia (depositos ou saques)
3 - Sair
""")
                
                if acao == "1":
                    funcao_banco.saldo()
                elif acao == "2":
                    funcao_banco.transferencia()
                elif acao == "3":
                    break
                else:
                    print("Opção inválida")
    else:
        print("Valor inválido")

