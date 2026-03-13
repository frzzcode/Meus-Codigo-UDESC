class Aluno:
    __Nome = None
    __Nota1 = None
    __Nota2 = None
    __Nota3 = None
    __Media = None

    def __init__(self):
        self.__Nome = "Digite seu Nome"
        self.__Nota1 = 0
        self.__Nota2 = 0
        self.__Nota3 = 0
        self.Calculo()

    def Leitura(self):
        self.__Nome = input("Digite o nome: ")
        self.__Nota1 = float(input("Digite a primeira Nota: "))
        self.__Nota2 = float(input("Digite a segunda Nota: "))
        self.__Nota3 = float(input("Digite a terceira Nota: "))

    def Calculo(self):
        self.__Media = (self.__Nota1 + self.__Nota2 + self.__Nota3) / 3
        return self.__Media
    
    def toString(self):
        Str = f"O aluno {self.__Nome}, tem as notas {self.__Nota1, self.__Nota2, self.__Nota3}, e sua media é {self.Calculo()}"
        return Str
    

N=int(input("Qual a quantidade de Alunos: "))


vet_alu=[]
for i in range(0,N,1):
    a=Aluno()
    a.Leitura()
    a.Calculo()
    vet_alu.append(a)

str=""
for i in range(0,N,1):
    str= str +"%s\n" % vet_alu[i].toString()

print("\nImpressão final:")
print(str)
