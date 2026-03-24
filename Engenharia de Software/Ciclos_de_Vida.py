# 1. Cascata (Waterfall) – Software Bancário
# Exemplo: Sistemas bancários legados, onde cada fase é rigidamente separada (requisitos → desenvolvimento → testes → implantação).
# Simulação de um sistema bancário básico seguindo o modelo Cascata
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        """Fase 1: Definição de requisitos - Criar uma conta bancária com saldo inicial"""
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Fase 2: Implementação - Método para adicionar dinheiro à conta"""
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        """Fase 3: Testes - Simulação de saque verificando saldo disponível"""
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")

    def exibir_saldo(self):
        """Fase 4: Manutenção - Método para visualizar o saldo da conta"""
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()



#2. Espiral – Software Aeroespacial
#Exemplo: Sistemas de controle de aeronaves e satélites. O software passa por várias iterações, ajustando requisitos e eliminando riscos.

import random

# Simulação de controle de altitude de um satélite com análise de risco
class Satelite:
    def __init__(self):
        """Configuração inicial do satélite"""
        self.altitude = 500  # km

    def ajustar_altitude(self):
        """Cada iteração verifica possíveis falhas antes de ajustar a altitude"""
        for i in range(3):  # 3 ciclos de análise de risco
            risco = random.choice([True, False])  # Simula risco de falha
            if risco:
                print(f"Risco identificado na iteração {i + 1}, corrigindo...")
            else:
                self.altitude += 10
                print(f"Altura ajustada: {self.altitude} km")

# Exemplo de uso
satelite = Satelite()
satelite.ajustar_altitude()


#3. Prototipação – Aplicativos Mobile
#Exemplo: Figma e Notion começam com protótipos para testar interfaces antes da implementação final.
# Simulação de um protótipo de app de notas
class AppNotas:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        """Protótipo inicial: Adiciona notas ao aplicativo"""
        self.notas.append(nota)
        print("Nota adicionada:", nota)

    def visualizar_notas(self):
        """Protótipo refinado: Permite visualizar as notas"""
        print("Minhas Notas:", self.notas)

# Exemplo de uso
app = AppNotas()
app.adicionar_nota("Estudar Python")
app.visualizar_notas()

