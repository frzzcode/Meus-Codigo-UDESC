# Simulação de um Modelo de Desenvolvimento de Software Incremental
# O sistema será desenvolvido em incrementos, adicionando funcionalidades passo a passo.

def apresentar_menu():
    """ Exibe o menu de opções para o usuário """
    print("\nEscolha uma funcionalidade para adicionar ao sistema:")
    print("1. Cadastro de Usuários")
    print("2. Registro de Pedidos")
    print("3. Relatórios de Vendas")
    print("4. Encerrar o Desenvolvimento")

def desenvolvimento_incremental():
    """ Simula a construção incremental de um sistema """
    funcionalidades = []
    print("Bem-vindo ao desenvolvimento incremental do software!\n")
    
    while True:
        apresentar_menu()
        escolha = input("Digite o número da funcionalidade a ser adicionada: ")
        
        if escolha == "1" and "Cadastro de Usuários" not in funcionalidades:
            funcionalidades.append("Cadastro de Usuários")
            print("Incremento 1: Módulo de Cadastro de Usuários adicionado ao sistema.")
        
        elif escolha == "2" and "Registro de Pedidos" not in funcionalidades:
            if "Cadastro de Usuários" not in funcionalidades:
                print("Erro: O módulo 'Cadastro de Usuários' precisa ser implementado primeiro.")
            else:
                funcionalidades.append("Registro de Pedidos")
                print("Incremento 2: Módulo de Registro de Pedidos adicionado ao sistema.")

        elif escolha == "3" and "Relatórios de Vendas" not in funcionalidades:
            if "Registro de Pedidos" not in funcionalidades:
                print("Erro: O módulo 'Registro de Pedidos' precisa ser implementado primeiro.")
            else:
                funcionalidades.append("Relatórios de Vendas")
                print("Incremento 3: Módulo de Relatórios de Vendas adicionado ao sistema.")

        elif escolha == "4":
            print("\nDesenvolvimento concluído! Funcionalidades implementadas:")
            for func in funcionalidades:
                print(f"- {func}")
            print("O sistema foi entregue com sucesso!")
            break
        else:
            print("Opção inválida ou funcionalidade já implementada. Tente novamente.")

# Execução da simulação do modelo incremental
desenvolvimento_incremental()

-----------------------------------------------------------------------------------------------
# Exemplo Modelo RAD
# Simulação do Modelo de Desenvolvimento de Software RAD (Rapid Application Development)
# O sistema será desenvolvido rapidamente em módulos, com feedback constante do usuário.

def apresentar_menu():
    """ Exibe o menu de opções para o usuário interagir com o desenvolvimento do sistema """
    print("\nSelecione um módulo para desenvolver rapidamente:")
    print("1. Modelagem do Negócio")
    print("2. Modelagem dos Dados")
    print("3. Modelagem do Processo")
    print("4. Geração da Aplicação")
    print("5. Teste e Modificação")
    print("6. Finalizar Desenvolvimento")

def desenvolvimento_rad():
    """ Simula um desenvolvimento rápido baseado no modelo RAD """
    modulos_desenvolvidos = []
    print("Bem-vindo ao Desenvolvimento Rápido de Aplicações (RAD)!\n")
    
    while True:
        apresentar_menu()
        escolha = input("Digite o número do módulo a ser desenvolvido: ")
        
        if escolha == "1" and "Modelagem do Negócio" not in modulos_desenvolvidos:
            modulos_desenvolvidos.append("Modelagem do Negócio")
            print("Módulo 'Modelagem do Negócio' desenvolvido com sucesso!")

        elif escolha == "2" and "Modelagem dos Dados" not in modulos_desenvolvidos:
            modulos_desenvolvidos.append("Modelagem dos Dados")
            print("Módulo 'Modelagem dos Dados' desenvolvido com sucesso!")

        elif escolha == "3" and "Modelagem do Processo" not in modulos_desenvolvidos:
            modulos_desenvolvidos.append("Modelagem do Processo")
            print("Módulo 'Modelagem do Processo' desenvolvido com sucesso!")

        elif escolha == "4" and "Geração da Aplicação" not in modulos_desenvolvidos:
            if "Modelagem dos Dados" not in modulos_desenvolvidos or "Modelagem do Processo" not in modulos_desenvolvidos:
                print("Erro: Para gerar a aplicação, finalize as modelagens de dados e processo primeiro.")
            else:
                modulos_desenvolvidos.append("Geração da Aplicação")
                print("Módulo 'Geração da Aplicação' desenvolvido com sucesso!")

        elif escolha == "5" and "Teste e Modificação" not in modulos_desenvolvidos:
            if "Geração da Aplicação" not in modulos_desenvolvidos:
                print("Erro: Para testar e modificar, a aplicação precisa estar gerada.")
            else:
                modulos_desenvolvidos.append("Teste e Modificação")
                print("Módulo 'Teste e Modificação' desenvolvido com sucesso! Feedback aplicado.")

        elif escolha == "6":
            print("\nDesenvolvimento finalizado! Módulos desenvolvidos:")
            for modulo in modulos_desenvolvidos:
                print(f"- {modulo}")
            print("O sistema foi desenvolvido com sucesso usando o modelo RAD!")
            break

        else:
            print("Opção inválida ou módulo já desenvolvido. Tente novamente.")

# Execução da simulação do modelo RAD
desenvolvimento_rad()
