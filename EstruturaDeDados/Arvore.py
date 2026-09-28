class Node():
    def __init__(self, info):
        self.info = info
        self.dir = None
        self.esq = None


class Arvore():
    def __init__(self):
        self.raiz = None

    def inserir(self, aux, valor):
        if aux == None:
            return Node(valor)
        elif valor <= aux.info:
            aux.esq = self.inserir(aux.esq, valor)
        else:
            aux.dir = self.inserir(aux.dir, valor)
        return aux

    def imprimir(self, aux):
        if aux != None:
            self.imprimir(aux.esq)
            print(aux.info, end=" ")
            self.imprimir(aux.dir)

    def contar(self, aux):
        if aux == None:
            return 0
        else:
            return 1 + self.contar(aux.esq) + self.contar(aux.dir)

    def soma(self, aux):
        if aux == None:
            return 0
        else:
            return aux.info + self.soma(aux.esq) + self.soma(aux.dir)

    def consultar(self, aux, valor):
        if aux == None:
            return False

        if aux.info == valor:
            return True
        elif valor < aux.info:
            return self.consultar(aux.esq, valor)
        else:
            return self.consultar(aux.dir, valor)

    def menor_valor(self, aux):
        while aux.esq != None:
            aux = aux.esq
        return aux

    def remover(self, aux, valor):
        if aux == None:
            return aux

        if valor < aux.info:
            aux.esq = self.remover(aux.esq, valor)

        elif valor > aux.info:
            aux.dir = self.remover(aux.dir, valor)

        else:
            
            if aux.esq == None and aux.dir == None:
                return None

            
            elif aux.esq == None:
                return aux.dir

            
            elif aux.dir == None:
                return aux.esq

            temp = self.menor_valor(aux.dir)
            aux.info = temp.info
            aux.dir = self.remover(aux.dir, temp.info)

        return aux

    def prof(self, aux):
        if aux == None:
            return -1

        esq = self.prof(aux.esq)
        dir = self.prof(aux.dir)

        if esq > dir:
            return esq + 1
        else:
            return dir + 1

    def nivel(self, aux, valor, nivelAtual=0):
        if aux == None:
            return -1

        if aux.info == valor:
            return nivelAtual

        elif valor < aux.info:
            return self.nivel(aux.esq, valor, nivelAtual + 1)

        else:
            return self.nivel(aux.dir, valor, nivelAtual + 1)
        
arv = Arvore()

while True:
    print("\n1 - Inserir")
    print("2 - Imprimir")
    print("3 - Contar")
    print("4 - Somar")
    print("5 - Média")
    print("6 - Consultar")
    print("7 - Remover")
    print("8 - Profundidade")
    print("9 - Nível do nó")
    print("0 - Sair")

    op = int(input("Escolha: "))

    if op == 1:
        valor = int(input("Valor: "))
        arv.raiz = arv.inserir(arv.raiz, valor)

    elif op == 2:
        arv.imprimir(arv.raiz)

    elif op == 3:
        print("Quantidade:", arv.contar(arv.raiz))

    elif op == 4:
        print("Soma:", arv.soma(arv.raiz))

    elif op == 5:
        qtd = arv.contar(arv.raiz)

        if qtd != 0:
            print("Média:", arv.soma(arv.raiz) / qtd)
        else:
            print("Árvore vazia")

    elif op == 6:
        valor = int(input("Valor: "))
        if arv.consultar(arv.raiz, valor):
            print("Valor encontrado")
        else:
            print("Valor não encontrado")

    elif op == 7:
        valor = int(input("Valor: "))
        arv.raiz = arv.remover(arv.raiz, valor)

    elif op == 8:
        print("Profundidade:", arv.prof(arv.raiz))

    elif op == 9:
        valor = int(input("Valor: "))
        nivel = arv.nivel(arv.raiz, valor)

        if nivel == -1:
            print("Valor não encontrado")
        else:
            print("Nível:", nivel)

    elif op == 0:
        break
        
