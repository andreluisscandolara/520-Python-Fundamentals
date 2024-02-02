# Arquivo usado pra armazenar as funções relacionadas ao banco de dados.

from lib import classes
import sqlite3

def criar_banco():
    conexao = sqlite3.connect(r"data\banco.db")
    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome PRIMARY KEY, idade, saldo)")
    cursor.execute("CREATE TABLE IF NOT EXISTS auth (nome PRIMARY KEY, usuario, senha)")
    conexao.commit()

def registrar():
    nome = input("Qual o nome completo da pessoa a ser cadastrada? ")
    idade = input("Qual a idade da pessoa? ")
    saldo = 0.00
    usuario = input("Qual o nome de usuario? ")
    senha = input("Escolha uma senha: ")

    pessoa = classes.Cliente(nome, idade, saldo, usuario, senha)
    pessoa.cadastrar()

def login():
    global login_usuario
    login_usuario = input("Digite seu usuario: ")
    login_senha = input("Digite sua senha: ")

    conexao = sqlite3.connect(r"data\banco.db")
    cursor = conexao.cursor()

    cursor.execute(f"SELECT senha from auth WHERE usuario = '{login_usuario}'")
    conteudo = cursor.fetchone()
    
    if login_senha == conteudo[0]:
        return True
    return False

def saldo():
    conexao = sqlite3.connect(r"data\banco.db")
    cursor = conexao.cursor()

    cursor.execute(f"SELECT nome from auth WHERE usuario = '{login_usuario}'")
    nome_usuario = cursor.fetchone()
    cursor.execute(f"SELECT saldo from clientes WHERE nome = '{nome_usuario[0]}'")
    conteudo = cursor.fetchone()

    print(conteudo[0])

def transferencia():
    acao = input("Que tipo de transferencia está fazendo? [deposito/saque]: ")
    valor = float(input("Qual o valor da transferencia? "))

    conexao = sqlite3.connect(r"data\banco.db")
    cursor = conexao.cursor()

    cursor.execute(f"SELECT nome from auth WHERE usuario = '{login_usuario}'")
    nome_usuario = cursor.fetchone()

    cursor.execute(f"SELECT saldo from clientes WHERE nome = '{nome_usuario[0]}'")
    saldo_usuario = cursor.fetchone()
    saldo_usuario = float(saldo_usuario[0])
    if acao == "deposito":
        novo_saldo = saldo_usuario + valor
    elif acao == "saque":
        novo_saldo = saldo_usuario - valor

    cursor.execute(f"UPDATE clientes SET SALDO = '{novo_saldo}' WHERE nome = '{nome_usuario[0]}'")
    print("Tranferencia feita")
