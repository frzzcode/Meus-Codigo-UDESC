from datetime import datetime

class No:
    def __init__(self, nome, quantidade, unidade, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.validade = validade
        self.prox = None
        self.ant = None

class Lista:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def empty(self):
        return self.__ini is None

    def push(self, nome, qtd, unidade, validade):

        try:
            data = datetime.strptime(validade, "%d/%m/%Y")
        except ValueError:
            print("Data inválida!")
            return

        novo = No(nome, qtd, unidade, validade)

        if self.empty():
            self.__ini = novo
            self.__fim = novo
            return

        atual = self.__ini

        while atual:

            data_atual = datetime.strptime(
                atual.validade,
                "%d/%m/%Y"
            )

            if nome.lower() < atual.nome.lower():
                break

            if nome.lower() == atual.nome.lower():
                if data < data_atual:
                    break

            atual = atual.prox

        if atual is None:
            novo.ant = self.__fim
            self.__fim.prox = novo
            self.__fim = novo
            return

        if atual == self.__ini:
            novo.prox = self.__ini
            self.__ini.ant = novo
            self.__ini = novo
            return

        anterior = atual.ant

        anterior.prox = novo
        novo.ant = anterior

        novo.prox = atual
        atual.ant = novo
        
    def consumir(self, nome, qtd):

        total = 0
        atual = self.__ini

        while atual:
            if atual.nome.lower() == nome.lower():
                total += atual.quantidade
            atual = atual.prox

        if total == 0:
            print("Alimento inexistente!")
            return

        if qtd > total:
            print("Quantidade maior que o estoque disponível!")
            return

        atual = self.__ini

        while atual and qtd > 0:

            prox = atual.prox

            if atual.nome.lower() == nome.lower():

                if atual.quantidade <= qtd:

                    qtd -= atual.quantidade
                    self.__remover_no(atual)

                else:

                    atual.quantidade -= qtd
                    qtd = 0

            atual = prox

        print("Consumo realizado com sucesso!")

    def consultar_agrupado(self):

        if self.empty():
            print("Lista vazia!")
            return

        estoque = {}
        atual = self.__ini

        while atual:

            if atual.nome not in estoque:
                estoque[atual.nome] = [0, atual.unidade]

            estoque[atual.nome][0] += atual.quantidade

            atual = atual.prox

        print("\nESTOQUE AGRUPADO")
        

        for nome, dados in estoque.items():
            print(f"{nome}: {dados[0]} {dados[1]}")

    def consultar_lotes(self):

        if self.empty():
            print("Lista vazia!")
            return

        atual = self.__ini

        print("\nESTOQUE POR LOTES")
        

        while atual:

            print(
                f"{atual.nome:10} | "
                f"{atual.quantidade:5} | "
                f"{atual.unidade:10} | "
                f"{atual.validade}"
            )

            atual = atual.prox

    def listar_vencidos(self):

        if self.empty():
            print("Lista vazia!")
            return

        hoje = datetime.today()

        atual = self.__ini
        encontrou = False

        print("\nALIMENTOS VENCIDOS")
        

        while atual:

            data = datetime.strptime(
                atual.validade,
                "%d/%m/%Y"
            )

            if data < hoje:

                print(
                    f"{atual.nome:10} | "
                    f"{atual.quantidade:5} | "
                    f"{atual.unidade:10} | "
                    f"{atual.validade}"
                )

                encontrou = True

            atual = atual.prox

        if not encontrou:
            print("Nenhum alimento vencido.")

    def remover_vencidos(self):

        if self.empty():
            print("Lista vazia!")
            return

        hoje = datetime.today()

        atual = self.__ini
        removidos = 0

        while atual:

            prox = atual.prox

            data = datetime.strptime(
                atual.validade,
                "%d/%m/%Y"
            )

            if data < hoje:
                self.__remover_no(atual)
                removidos += 1

            atual = prox

        print(f"{removidos} lote vencido removido.")

lista = Lista()

while True:

    print("1 - Inserir alimento")
    print("2 - Consumir alimento")
    print("3 - Consultar estoque agrupado")
    print("4 - Consultar estoque por lote")
    print("5 - Listar vencidos")
    print("6 - Remover vencidos")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        qtd = int(input("Quantidade: "))
        unidade = input("Unidade: ")
        validade = input("Validade: ")

        lista.push(nome, qtd, unidade, validade)

    elif op == "2":
        nome = input("Nome do alimento: ")
        qtd = int(input("Quantidade a consumir: "))

        lista.consumir(nome, qtd)

    elif op == "3":
        lista.consultar_agrupado()

    elif op == "4":
        lista.consultar_lotes()

    elif op == "5":
        lista.listar_vencidos()

    elif op == "6":
        lista.remover_vencidos()

    elif op == "0":
        break

    else:
        print("Opção inválida!")