# 1) Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:

# capacidade total
# capacidade atual
# placa
# modelo
# movimento

# Os comportamentos esperados para um Ônibus são:

# Embarcar
# Desembarcar
# Acelerar
# Frear

# Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir super-
# lotação. Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque
# de pessoas. Além disso, pessoas não podem embarcar ou desembarcar com o onibus em movimento.


class Onibus:

    def __init__(self):
        self.__capacidade_total = 45
        self.__passageiros = 0
        self.__movimento = False
        self.__placa = "HKT-5239"
        self.__modelo = "Escolar"

    def embarcar(self, novos_passageiros):
        if self.__movimento == True:
            return("O onibus está em movimento!")
        elif self.__passageiros == self.__capacidade_total:
            return("O onibus está lotado!")
        else:
            if self.__passageiros + novos_passageiros > self.__capacidade_total:
                total_passageiros = self.__passageiros + novos_passageiros
                passageiros_de_fora = total_passageiros - self.__capacidade_total
                conseguiram_entrar = novos_passageiros - passageiros_de_fora

                self.__passageiros = 45
                return(f"Apenas {conseguiram_entrar} pessoas conseguiram entrar, {passageiros_de_fora} ficaram de fora porque o onibus lotou.")

            else:
                self.__passageiros += novos_passageiros
                return(f"Todos os {novos_passageiros} passageiros entraram no onibus.")

    def desembarcar(self, passageiros_saindo):
        if self.__movimento == True:
            return("O onibus está em movimento!")
        elif self.__passageiros == 0:
            return("Não há ninguém para desembarcar")
        elif self.__passageiros < passageiros_saindo:
            return(f"Não há {passageiros_saindo} pessoas pra desembarcar, há apenas {self.__passageiros} pessoas no onibus neste momento.")
        else:
            self.__passageiros -= passageiros_saindo
            return(f"{passageiros_saindo} passageiros desembacaram do onibus.")

    def acelerar(self):
        if self.__movimento == True:
            return("O onibus já está em movimento.")
        else:
            self.__movimento = True
            return("O onibus começou a se mover.")
        
    def frear(self):
        if self.__movimento == False:
            return("O onibus já está parado.")
        else:
            self.__movimento = False
            return("O onibus parou de se mover.")


onibus_escolar = Onibus()

print(onibus_escolar.acelerar())
print(onibus_escolar.frear())
print(onibus_escolar.embarcar(10))
print(onibus_escolar.acelerar())
print(onibus_escolar.frear())
print(onibus_escolar.desembarcar(5))
print(onibus_escolar.embarcar(50))
print(onibus_escolar.acelerar())


# ==========================================================================
# 2) Implemente um programa que represente uma fila. O contexto do programa é uma
# agência de banco. Cada cliente ao chegar deverá respeitar a seguinte regra: o primeiro
# a chegar deverá ser o primeiro a sair. Você poderá representar pessoas na fila a par-
# tir de números os quais representam a idade. A sua fila deverá conter os seguintes
# comportamentos:

# • Adicionar pessoa na fila: adicionar uma pessoa na fila.
# • Atender Fila: atender a pessoa respeitando a ordem de chegada
# • Dar prioridade: colocar uma pessoa maior de 65 anos como o primeiro da fila

class Fila:

    def __init__(self):
        self.__fila = []
        self.__prioridade = []

    def adicionar(self, nome, idade):
        if idade >= 65:
            self.__prioridade.append(nome)
            self.__fila.append(nome)
            return(f"{nome} entrou na fila")
        else:
            self.__fila.append(nome)
            return(f"{nome} entrou na fila")
        
    def atender(self):
        if len(self.__fila) < 1:
            return("Não há ninguém na fila.")
        else:
            atendido = self.__fila[0]
            if self.__fila[0] in self.__prioridade:
                self.__prioridade.remove(self.__fila[0])
            self.__fila.remove(self.__fila[0])
            return(f"Atendendo a primeira pessoa da fila, {atendido}")

    def dar_prioridade(self):
        if len(self.__prioridade) < 1:
            return("Não há ninguém pra dar prioridade.")
        else:
            prioritario = self.__prioridade[0]
            self.__prioridade.remove(prioritario)
            self.__fila.remove(prioritario)
            self.__fila.insert(0, prioritario)
            return(f"{prioritario} recebeu prioridade e está na frente da fila.")
        
banco = Fila()

print(banco.adicionar("Tiago", 27))
print(banco.adicionar("Caio", 28))
print(banco.adicionar("Kaique", 30))
print(banco.adicionar("Leonardo", 20))
print(banco.adicionar("Amanda", 78))
print(banco.adicionar("Maria", 66))
print(banco.adicionar("José", 12))

print(banco.atender())
print(banco.atender())
print(banco.dar_prioridade())
print(banco.atender())
