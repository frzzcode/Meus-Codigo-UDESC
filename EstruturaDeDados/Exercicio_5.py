# Nome: Guilherme Ferraz
# Disciplina: Estrutura de Dados 1

# Exercício 05 - Pilha e Filas

class Pilha:
    def __init__(self):
        self.__pilha = []
    def push(self, num: int):
        self.__pilha.append(num)
    def getPilha(self):
        return self.__pilha
    def print(self):
        print("Pilha:", self.__pilha)


class Fila:
    def __init__(self):
        self.__fila = []
    def push(self, num: int):
        self.__fila.append(num)
    def printall(self):
        #Vê se a fila nao ta vazia.
        if len(self.__fila) == 0:
            print("Fila vazia")
        else:
            print(self.__fila)

#Inicializa os objetos e começa o programa.

pilha = Pilha()
fila_par = Fila()
fila_impar = Fila()

# Entrada dos numeros. 
while True:
    num = int(input("Digite um número (<=0 para parar): "))
    if num <= 0:
        break
    pilha.push(num)

# Separação em fila par ou fila impar.
for num in pilha.getPilha():
    if num % 2 == 0:
        fila_par.push(num)
    else:
        fila_impar.push(num)

# Saída
print("\n--- RESULTADO ---")
pilha.print()

print("Fila de pares:")
fila_par.printall()

print("Fila de ímpares:")
fila_impar.printall()