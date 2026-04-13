#Exercício 3

#Guilherme Ferraz
#Est. Dados 1

from collections import deque
class Lista:
    def __init__(self):
        self.__listaL = deque()
        self.__listaK = deque()
    def push_first(self, nome):
        self.__listaL.appendleft(nome)
    def push_end(self, nome):
        self.__listaL.append(nome)
    def printall(self):
        if not self.__listaK:
            print("Lista K Vazia")
        else:
            aux = deque()
            saida = "Lista: \n"
            while self.__listaK:
                valor = self.__listaK.popleft()
                saida += valor + "\t"
                aux.append(valor)

            self.__listaK = aux

            return saida
    def push_K(self):
        if not self.__listaL:
            print("Lista L Vazia")
        else:
            while self.__listaL:

                iteml = self.__listaL.popleft()

                if not self.__listaK:
                    self.__listaK.append(iteml)
                else:
                    posicao = 0
                    inserido = False

                    for i in self.__listaK:
                            if iteml < i:
                                self.__listaK.insert(posicao, iteml)
                                inserido =True
                                break                            
                            posicao += 1

                    if not inserido:
                        self.__listaK.append(iteml)
def main():

    l = Lista()
    while True:
        op = int(input("\n1 - Inserir no início\n2 - Inserir no final\n3 - Sair\n\nOpção: "))
        if op == 1:
            l.push_first(input("Digite um nome para inserir: "))
            l.push_K()
            print(l.printall())
        elif op == 2:
            l.push_end(input("Digite um nome para inserir: "))
            l.push_K()
            print(l.printall())
        elif op == 3:
            break

if __name__ == "__main__":
    main()