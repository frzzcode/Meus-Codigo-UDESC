import random

class Node:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
        self.__prox = None  

    def get_prox(self):
        return self.__prox      
    def set_prox(self, prox):
        self.__prox = prox

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, nome):
        self.__nome = nome

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor


class Fila:
    def __init__(self):
        self.__fim = None

    def push(self, nome, valor):
        novo = Node(nome, valor)
        if not self.__fim:
            novo.set_prox(novo)
        else:
            novo.set_prox(self.__fim.get_prox())
            self.__fim.set_prox(novo)
        self.__fim = novo

    def pop(self):
        if not self.__fim:
            return "Fila Vazia"
        
        elif self.__fim == self.__fim.get_prox():
            self.__fim = None
        else:
            self.__fim.set_prox(self.__fim.get_prox().get_prox())
        return "Item Removido"

    def pop_push(self):
        if self.__fim.get_prox() != self.__fim:
            temp = self.__fim.get_prox()
            self.__fim.set_prox(self.__fim.get_prox().get_prox())
            temp.set_prox(self.__fim.get_prox())
            self.__fim.set_prox(temp)
            self.__fim = temp

    def jogada(self, jogada_premiada):
        if not self.__fim:
            return "Sem Jogadores"
        
        jogador_atual = self.__fim.get_prox()
        
        saldo_atual = jogador_atual.get_valor()
        jogador_atual.set_valor(saldo_atual - 5)
        
        print(f"\nJogador {jogador_atual.get_nome()} pagou $5. Saldo restante: ${jogador_atual.get_valor()}")
        
        
        num_sorteado = random.randint(1, 10) 
        if num_sorteado == jogada_premiada:
            return jogador_atual.get_nome() 
            
        
        if jogador_atual.get_valor() < 5:
            print(f"Jogador {jogador_atual.get_nome()} ficou sem saldo suficiente e foi removido.")
            self.pop()
        else:
            self.pop_push()
            
            
    def print_all(self):
        if not self.__fim:
            return "Fila vazia"
        
        atual = self.__fim.get_prox()
        saida = "\nFila atual: \n" 
        while True:
            saida += f"{atual.get_nome()} / R${atual.get_valor()}"
            atual = atual.get_prox()
            if atual == self.__fim.get_prox():
                break
        return "Fila: " + saida 
        

def main():
    f = Fila()
    jogada_premiada = random.randint(1, 10)
    
    menu = "\n1 - Adicionar Jogador\n2 - Imprimir Fila\n3 - Jogar\n4 - Sair\nOpção: "
    
    while True:
        op = int(input(menu))
        if op == 1:
            nome = input("Nome do jogador: ")
            saldo = float(input("Saldo inicial: "))
            f.push(nome, saldo)
        elif op == 2:
            print(f.print_all())
        elif op == 3:
            ganhador = f.jogada(jogada_premiada)
            if ganhador:
                if "Sem Jogadores" == ganhador:
                    print("\nNão há jogadores na fila para jogar!")
                else:
                    print(f"\nPARABÉNS \nO jogador {ganhador} ganhou o prêmio de 1 MILHÃO DE DÓLARES!")
                    
                    break
            else:               
                if f.print_all() == "Fila vazia":
                    print("\nTodos os jogadores ficaram sem saldo. Fim de jogo sem vencedores!")
                    break
        elif op == 4:
            break

if __name__ == "__main__":
    main()