from collections import deque

class Lista:
    def __init__(self):
        self.__lista = deque()
    def push(self, valor):
        if not self.__lista:
            self.__lista.append(valor)
        else:
            posicao = 0
            for item in self.__lista:
                if valor < item:
                    break
                posicao += 1
    
            self.__lista.insert(posicao, valor)
        
        print(f"'{valor}' inserido.")
        
    def pop(self, nome):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            if nome in self.__lista:
                self.__lista.remove(nome)
                return "Item Excluido"
            else:
                return "Nome não encontrado"
    def print_all(self):
        if not self.__lista:
            print("Lista Vazia")
        else:
            aux = deque()
            saida = "Lista: \n"
            while self.__lista:
                valor = self.__lista.popleft()
                saida += valor + "\t"
                aux.append(valor)
            self.__lista = aux
            return saida
    def find(self,nome):
        return nome in self.__lista
    def pop_all(self):
        if not self.__lista:
            return "Nenhum nome na Lista"
        else:
            self.__lista.clear()
            return "Agora a Lista está Vazia"
        
def main():

    l = Lista()
    while True:
        op = int(input("\n1 - Inserir \n2 - Consulta\n3 - Remover Escolha\n4 - Remover Todos\n5 - Sair\n\nOpção: "))
        if op == 1:
            l.push(input("Digite um nome para inserir: "))
            print(l.print_all())

        elif op == 2:
            if l.find(input("Digite o nome a Consultar: ")):
                print("Nome na lista")
            else:
                print("Nome não está na lista")
        elif op == 3:
            l.pop(input("Digite o nome a ser excluido: "))
            print(l.print_all())
        elif op == 4:
            l.pop_all()
            print(l.print_all())
        elif op == 5:
            break

if __name__ == "__main__":
    main()