#Exercicio 4
from collections import deque

class Lista:
    def __init__(self):
        self.__lista = deque()

    def push(self, num):
        if not self.__lista:
            self.__lista.append(num)
        else:
            posicao = 0
            inserido = False
            for item in self.__lista:
                if num < item:
                    self.__lista.insert(posicao, num)
                    inserido = True
                    break
                posicao += 1
            if not inserido:
                self.__lista.append(num)

    def get_Lista(self):
        
        return self.__lista

    def pop_repetidos(self):
        aux = deque()
        while self.__lista:
            item = self.__lista.popleft()
           
            if item not in aux:
                aux.append(item)
        self.__lista = aux

    def pop_all(self):
        self.__lista.clear()

    def print_all(self, nome_lista="Lista"):
        
        aux = deque()
        print(nome_lista)
        while self.__lista:
            valor = self.__lista.popleft()
            print(f"{valor}", end="\t")
            aux.append(valor)
        print("\n") 
        self.__lista = aux

def main():
    l1 = Lista() 
    l2 = Lista() 
    l = Lista()  

    numeros = [10, 3, 10, 5, 2, 8, 7, 3]

    for n in numeros:
        if n % 2 == 0:
            l1.push(n)
        else:
            l2.push(n)
    
  
    l1.print_all("L1 (Par)")
    l2.print_all("L2 (Ímpar)")

  
    for item in l1.get_Lista():
        l.push(item)
    for item in l2.get_Lista():
        l.push(item)

    print("\nLista L Combinada (antes de limpar duplicatas)")
    l.print_all("L")

    l.pop_repetidos()
    
    print("\nResultado Final ")
    l.print_all("L Final")

if __name__ == "__main__":
    main()