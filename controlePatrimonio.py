import pickle
from bem import Bem

class ControlePatrimonio:
    def __init__(self):
        self.__bens = []
    
    def salvar_dados(self,item):
            try:
                with open("patrimonio.pkl", "wb") as arquivo:
                    pickle.dump(item, arquivo)
            except FileNotFoundError:
                 print("ERRO: NAO FOI ENCONTRADO O ARQUIVO")
            except PermissionError:
                    print("ERRO: EM PERMISSAO PARA GRAVAR OS DADOS.")
            except pickle.PickleError as e:
                    print(f"Erro ao serializar os dados: {e}")
            except Exception as e:
                    print(f"ERRO INESPERADO :/ {e}")
    def carregar_dados(self):
            try:
                with open("patrimonio.pkl", "rb") as arquivo:
                    dados_carregados= pickle.load(arquivo)
                    print("Dados carregados com sucesso!")
                self.__bens = dados_carregados
            except FileNotFoundError:
                print("Erro: o arquivo 'dados.pkl' não foi encontrado.")
            except PermissionError:
                print("Erro: sem permissão para ler o arquivo.")
            except pickle.UnpicklingError:
                print("Erro: o arquivo não contém dados válidos do pickle (pode estar corrompido).")
            except EOFError:
                print("Erro: o arquivo está vazio.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
    def procurar_bem(self, codigo):
        for bem in self.__bens:
            if bem.codigo == codigo:
                return bem
        return False

    def cadastrar_bem(self):
            print("----------Cadastrar Novo Bem----------")
            try:     
               cod = input("Qual o codigo do bem?")
               if cod != "":         
                existe = self.procurar_bem(cod)
                if existe:
                        print("Este bem ja esta cadastrado no sistema")
                else:
                            leg = input("Qual a legenda do bem?")
                            loc = input("Qual a localizacao do bem?")
                            sit = "disponivel"
                            bem = Bem(cod,leg,loc,sit)
                            self.__bens.append(bem)
                            print("BEM CADASTRADO")
                            self.salvar_dados(self.__bens)
               else:
                    ("O codigo deve existir!")
            except Exception as e: 
                print("ERRO INESPERADO :( ")
       
    def listar_bens(self):
         print("----------Bens----------")
         if not self.__bens:
               print("Ainda nao ha bens cadastrados")
         else:
            for bem in self.__bens:
                print(bem)
                print("-" * 40)


    def editar_bens(self):
        print("----------Editar Bem----------")
        qual = input("Qual o codigo do Bem que deseja editar? ")
        editado = False
        editbem = self.procurar_bem(qual)
        
        if not editbem:
             print("este bem nao existe para ser editado")
             return 
        
        print("Deixe vazio caso nao queira alterar opcao!")

        nova_descricao = input("Qual a nova legenda?")
        nova_localizacao = input("Qual a nova localização?")
        nova_situacao = input("Qual a nova situaçao? (disponivel, em uso, Em manutencao) ").lower()

         
        for i in range(len(self.__bens)):
                if self.__bens[i] == editbem:
                    if nova_descricao != "":
                         editbem.set_descricao(nova_descricao)
                    if nova_localizacao != "":
                         editbem.set_localizacao(nova_localizacao)
                    
                    if nova_situacao != "":
                        if nova_situacao != "disponivel" and nova_situacao != "em uso" and nova_situacao != "em manutencao":
                            print("Bem nao atualizado: Situacao invalida, verifique a situacao")
                            return 
                        else:   
                            editbem.set_situacao(nova_situacao)
        editado = True
        print("BEM EDITADO")
        self.salvar_dados(self.__bens)
        return editado
       
    def excluir_bens(self) -> bool:
        print("----------Excluir Bem----------")
        qual = input("Qual o codigo do Bem que deseja apagar? ")
        removido = False
        delbem = self.procurar_bem(qual)
       
        if delbem:
            decisao =  input(f"Deseja apagar o Bem:\n{delbem} \nsim ou nao?")
            if decisao == "sim":
                for i in range(len(self.__bens)):
                    if self.__bens[i] == delbem:
                        del self.__bens[i]
                        removido = True
                        print("BEM REMOVIDO")
                        self.salvar_dados(self.__bens)
        else:
             print("impossivel apagar um bem que nao existe")
        return removido


    def gerar_relatorio(self):
                em_uso = 0
                disponivel = 0
                em_manutençao = 0
                tambens = len(self.__bens)
                for i in range(tambens):
                    if self.__bens[i].situacao == "em uso":
                        em_uso = em_uso+1
                    elif self.__bens[i].situacao == "disponivel":
                        disponivel = disponivel+1
                    elif self.__bens[i].situacao == "em manutencao":
                        em_manutençao = em_manutençao+1
                print("----------Relatorio----------")
                print(f"Quantidade de bens: {tambens}")
                print(f"EM USO: {em_uso}")
                print(f"EM MANUTENCAO: {em_manutençao}")
                print(f"DISPONIVEIS: {disponivel}")
                       
               
                    
