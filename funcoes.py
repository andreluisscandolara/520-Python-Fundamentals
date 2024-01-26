def definirCategoria(pessoas):
    menor = {}
    adulto = {}
    idoso = {}
    
    n_menor = 0
    n_adulto = 0
    n_idoso = 0

    for nome, idade in pessoas.items():
        if idade <= 17:
            menor[nome] = idade
            n_menor += 1
        elif idade <= 59:
            adulto[nome] = idade
            n_adulto += 1
        else:
            idoso[nome] = idade
            n_idoso += 1

    while True:
        escolha = int(input(f"""Voce digitou {len(pessoas)} nomes, e eles foram divididos em:
Menores: {n_menor}
Adultos: {n_adulto}
Idosos: {n_idoso}

Voce gostaria de verificar os nomes das pessoas de alguma categoria?
Digite 1 - Para ver os nomes dos menores.
Digite 2 - Para ver os nomes dos adultos.
Digite 3 - Para ver os nomes dos idosos.
Digite 4 - Para fechar o programa.
"""))
        
        if escolha == 1:
            print(f"Os menores adicionados foram:")
            for nome, idade in menor.items():
                print(f"{nome}, {idade} anos.")

        elif escolha == 2:
            print(f"Os adultos adicionados foram:")
            for nome, idade in adulto.items():
                print(f"{nome}, {idade} anos.")
        
        elif escolha == 3:
            print(f"Os idosos adicionados foram:")
            for nome, idade in idoso.items():
                print(f"{nome}, {idade} anos.")

        elif escolha == 4:
            break
