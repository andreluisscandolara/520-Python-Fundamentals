# Arquivo utilizado pra armazenar as classes utilizadas na aplicação.
import sqlite3

class Cliente:
    def __init__(self, nome, idade, saldo, usuario, senha):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self):
        conexao = sqlite3.connect(r"data\banco.db")
        cursor = conexao.cursor()

        cursor.execute(f"INSERT INTO clientes (nome, idade, saldo) VALUES ('{self.nome}', '{self.idade}', '{self.saldo}')")
        cursor.execute(f"INSERT INTO auth (nome, usuario, senha) VALUES ('{self.nome}', '{self.usuario}', '{self.senha}')")

        conexao.commit()
        conexao.close()
