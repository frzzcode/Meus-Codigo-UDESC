class Principal:
    def __init__(self):
        # Atributo privado conforme o diagrama
        self.__A = []

    def getA(self):
        return self.__A

    def setA(self, valor):
        self.__A.append(valor)

    def Leitura(self):
        self.__A = [] # Reinicia a lista para nova leitura
        n = int(input("Quantidade de valores de n: "))
        for i in range(n):
            v = float(input(f"Digite o {i+1}º valor: "))
            self.setA(v)

    def ordena(self):
        self.__A.sort()

    def toString(self):
        if not self.__A:
            return "Lista vazia."
        saida = "Valores na lista: "
        for item in self.__A:
            saida += str(item) + "  "
        return saida

    def repetições(self):
        if not self.__A:
            print("Lista vazia.")
            return
        
        # Ordenamos para facilitar a contagem por vizinhos
        self.ordena()
        print("\nVerificando repetições:")
        
        i = 0
        teve_repetido = False
        while i < len(self.__A):
            cont = 0
            j = i + 1
            # Enquanto o próximo for igual ao atual, contamos
            while j < len(self.__A) and self.__A[j] == self.__A[i]:
                cont += 1
                j += 1
            
            if cont > 0:
                # O número de vezes que APARECE REPETIDO é a contagem extra
                print(f"O número {self.__A[i]} aparece repetido {cont} vez(es).")
                teve_repetido = True
            
            i = j # Pula para o próximo número diferente
            
        if not teve_repetido:
            print("Nenhum número se repete.")

    def gerarB(self):
        if not self.__A:
            print("Lista A está vazia.")
            return
        
        self.ordena()
        B = []
        # Lógica manual para copiar apenas os únicos
        if len(self.__A) > 0:
            B.append(self.__A[0])
            for i in range(1, len(self.__A)):
                if self.__A[i] != self.__A[i-1]:
                    B.append(self.__A[i])
        
        print(f"Nova lista B (sem repetidos): {B}")

    def média(self):
        if not self.__A:
            print("Lista vazia, média zero.")
            return
        
        # Usando a função sum() conforme permitido
        m = sum(self.__A) / len(self.__A)
        print(f"Média aritmética da lista A: {m:.2f}")

    def del_A(self):
        self.__A = []
        print("Lista A foi limpa.")

def main():
    ex = Principal()
    menu = """
    ======== MENU ========
    1 - Ler valores (Lista A)
    2 - Imprimir Ordenado
    3 - Determinar Repetições
    4 - Gerar Lista B (Sem repetidos)
    5 - Calcular Média
    6 - Sair
    Opção: """

    while True:
        op = int(input(menu))
        if op == 1:
            ex.Leitura()
        elif op == 2:
            ex.ordena()
            print(ex.toString())
        elif op == 3:
            ex.repetições()
        elif op == 4:
            ex.gerarB()
        elif op == 5:
            ex.média()
        elif op == 6:
            print("Encerrando programa...")
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()