# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

import csv

with open("faroeste.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        print(linha, end="")
    arquivo.close()






# ====================================================================================
# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
# seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Endereço

# Os registros deverão ser armazenados em um arquivo CSV. Caso desejar manter o padrão
# brasileiro, o CSV será separado pelo caractere ;


# ====================================================================================
# 3) Implemente uma função de consulta no programa do exercício 2.


# ====================================================================================
# 4) Implemente uma função de exclusão no programa do exercício 2.
