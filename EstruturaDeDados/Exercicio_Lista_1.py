from collections import deque
class Lista:
    def __init__(self):
        self.__lista = deque()
    def push_first(self, nome):
        self.__lista.appendleft(nome)
    def push_end(self, nome):
        self.__lista.append(nome)
    def printall(self):
        if not self.__lista:
            print("Lista Vazia")
        else:
            aux = deque()
            saida  = "Lista: \n"
            while self.__lista:
                valor = self.__lista.popleft()
                saida += valor + "\t"
                aux.append(valor)
            self.__lista = aux
            return saida
    def find(self,nome):
        return nome in self.__lista
        
    def pop_first(self):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            return "Item Excluido" + self.__lista.popleft()
    def pop_end(self):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            return "Item Excluido" + self.__lista.pop()
    def pop(self, nome):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            if nome in self.__lista:
                self.__lista.remove(nome)
                return "Item Excluido"
            else:
                return "Nome não encontrado"
    def pop_all(self):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            self.__lista.clear()
            return "Agora a Lista está Vazia"

def main():

    l = Lista()
    while True:
        op = int(input("\n1 - Inserir no início\n2 - Inserir no final\n3 - Consulta\n4 - Remover primeiro/ultimo\n5 - Sair\n\nOpção: "))
        if op == 1:
            l.push_first(input("Digite um nome para inserir: "))
            print(l.printall())
        elif op == 2:
            l.push_end(input("Digite um nome para inserir: "))
            print(l.printall())
        elif op == 3:
            if l.find(input("Digite o nome a Consultar: ")):
                print("Nome na lista")
            else:
                print("Nome não está na lista")
        elif op == 4:
            op2 = int(input("Menu Excluir\n1 - Remover o primeiro\n2 - Remover último\n3 - Remover nome de escolha\n4 - Limpar a Lista\n"))
            if op2 == 1:
                l.pop_first()
                print(l.printall())
            elif op2 == 2:
                l.pop_end()
                print(l.printall())
            elif op2 == 3:
                l.pop(input("Digite o nome a ser excluido: "))
                print(l.printall())
            elif op2 == 4:
                l.pop_all()
                print(l.printall())
        elif op == 5:
            break

if __name__ == "__main__":
    main()
