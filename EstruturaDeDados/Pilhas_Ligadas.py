class Node:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None

    def get_valor(self):
        return self.__valor

    def get_proximo(self):
        return self.__proximo
    def set_proximo(self, proximo):
        self.__proximo = proximo


class Pilha:
    def __init__(self):
        self.__topo = None
    def push(self, valor):
        novo = Node(valor)
        novo.set_proximo(self.__topo)
        self.__topo = novo

    def pop(self):
        if self.__topo is None:
            return None

        valor = self.__topo.get_valor()
        self.__topo = self.__topo.get_proximo()
        return valor
    def vazia(self):
        return self.__topo is None


def decimal_para_binario(numero):
    pilha = Pilha()
    if numero == 0:
        return "0"
    
    while numero > 0:
        resto = numero % 2
        pilha.push(resto)
        numero = numero // 2
    saida = ""
    while not pilha.vazia():
        saida += str(pilha.pop())

    return saida

def binario_para_decimal(binario):
    decimal = 0
    potencia = 0

    i = len(binario) - 1

    while i >= 0:
        digito = int(binario[i])
        decimal += digito * (2 ** potencia)
        potencia += 1
        i = i - 1
    return decimal


def validar_decimal(entrada):
    try:
        numero = int(entrada)
        if numero < 0:
            return None
        return numero
    except:
        return None


def validar_binario(entrada):
    for c in entrada:
        if c not in "01":
            return False
    return True


def menu():
    while True:
        menu = "\n1 - Decimal para binário\n2 - Binário para decimal\n0 - Sair\n\nopcao: "
        opcao = input(menu)

        if opcao == "1":
            while True:
                entrada = input("Digite um número: ")
                numero = validar_decimal(entrada)

                if numero is None:
                    print("Entrada inválida")
                else:
                    print("Binario:", decimal_para_binario(numero))
                    break

        elif opcao == "2":
            while True:
                entrada = input("Digite um número binário: ")

                if not validar_binario(entrada):
                    print("Entrada inválida")
                else:
                    print("Decimal:", binario_para_decimal(entrada))
                    break

        elif opcao == "0":
            break

        else:
            print("Opção inválida")

menu()