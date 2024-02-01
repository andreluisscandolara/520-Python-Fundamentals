# Reescreva o exercicio 4 da aula 05 adicionando tratamentos de erro, 
# com a finalidade de que o programa nunca dê uma exceção e também que ele
# não aceite dados incorretos em nenhum momento.

import os
import csv

def validacao(teste, valor):
    match teste:

        case "resposta":
            try:
                valor = int(valor)
                if valor in [0, 1]:
                    return valor
                print("Valor inválido")
                return None                
            
            except ValueError:
                print("Valor inválido")
                return None
            
        case "cpf_nome":
                if len(valor) == 11 and valor.isnumeric() == True: 
                    return True
                
                elif valor.isalpha():
                    return True

                print("Valor inválido")
                return False
        
        case "nome":
            if valor.isalpha():
                return True
            print("Valor inválido")
            return False

        case "cpf":
                if len(valor) == 11 and valor.isnumeric() == True: 
                    return True

                print("Valor inválido")
                return False
        
        case "sexo":
            if valor.isalpha():
                if valor.upper() in ["M", "F", "OUTROS"]:
                    return True
            return False
        
        case "idade":
            try:
                valor = int(valor)
                return valor
            
            except ValueError:
                print("Valor inválido")
                return False

def consulta():
    while True:
        resposta = input("""Qual valor deseja consultar?
        0 - CPF
        1 - Nome\n\n""")
        resultado_int = validacao("resposta", resposta)
        if resultado_int != None:
            break

    while True:
        cpf_nome = input("Digite o CPF/Nome a consultar: ").strip().replace(".", "").replace("-", "")
        resultado = validacao("cpf_nome", cpf_nome)
        if resultado == True:
            break

    with open("banco.csv", "r") as arquivo:
        conteudo = csv.reader(arquivo, delimiter=";")
        valor_encontrado = False
        for linha in conteudo:
            try:
                if linha[resultado_int] == cpf_nome:
                    print(f"""Cadastro encontrado:
    CPF: {linha[0]}
    NOME: {linha[1]}
    IDADE: {linha[2]}
    SEXO: {linha[3]}
    ENDEREÇO: {linha[4]}\n""")
                    valor_encontrado = True
                    break    
            except IndexError:
                pass
        if valor_encontrado == False:
            print("Valor não encontrado.")

def exculsao(dado_a_excluir):
    with open("banco.csv", "r") as arquivo_inicial, open("banco_editado.csv", "a", newline="") as arquivo_final:
        writer = csv.writer(arquivo_final, delimiter=";")

        for linha in csv.reader(arquivo_inicial, delimiter=";"):
            try:
                if linha[0] != dado_a_excluir and linha[1] != dado_a_excluir:
                    writer.writerow(linha)
            except IndexError:
                pass

    os.remove("banco.csv")
    os.rename("banco_editado.csv", "banco.csv")

while True:
    opcao = input("""Digite uma opção:
1 - Consultar um valor no banco.
2 - Cadastrar um valor no banco.
3 - Remover um valor do banco.
4 - Parar o programa.\n\n""").strip()

    os.system("cls" if os.name == "nt" else "clear")

    if opcao == "4":
        print("Parando a execução")
        break
    
    elif opcao == "3":
        while True:
            entrada = input("Digite o nome ou CPF da pessoa que deseja remover do banco: ")
            if validacao("cpf_nome", entrada) == False:
                continue

            exculsao(entrada)
            print(f"Entrada {entrada} removida do banco de dados.")
            break

    elif opcao == "2":
        while True:
            cpf = input("Qual o CPF da pessoa? ").replace(".", "").replace("-", "")
            if validacao("cpf", cpf) == False:
                continue
            break
        
        while True:
            nome = input("Qual o nome da pessoa? ")
            if validacao("nome", nome) == False:
                continue
            break

        while True:
            idade = input("Qual o idade da pessoa? ")
            if validacao("idade", idade) == False:
                continue
            break

        while True:
            sexo = input("Qual o sexo da pessoa? [M/F/Outro]").strip()
            if validacao("sexo", sexo) == False:
                continue
            break

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
