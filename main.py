from controlePatrimonio import ControlePatrimonio
c = ControlePatrimonio()
c.carregar_dados()
print("ALUNA: MARIA EDUARDA SOARES FERREIRA\n")

while True:

    print("--------------MENU----------------")
    print("1- Cadastrar bem patrimonial")
    print("2- Listar bens")
    print("3- Editar bem")
    print("4- Excluir bem")
    print("5- Gerar relatorio")
    print("0- Sair")
    
    try:
        opcao= int(input("O que deseja? "))

    except ValueError:
        print("ERRO: A OPCAO DEVE SER UM NUMERO")
        continue

    except Exception as e:
        print(f"ERRO INESPERADO, DESCULPA :/ ->  {e}")
        continue

    match opcao:
        case 1:
            c.cadastrar_bem()
        case 2:
            c.listar_bens()
        case 3:
            c.editar_bens()
        case 4:
            c.excluir_bens()
        case 5:
            c.gerar_relatorio()
        case 0:
           break 
        case _:
            print("Opção inválida! Tente novamente.")