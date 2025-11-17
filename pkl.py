
import pickle
class Bem:
    def __init__(self,codigo, descricao,localizacao,situacao):
        self.codigo = codigo
        self.descricao = descricao
        self.situacao = situacao
        self.localizacao = localizacao
    
    def __str__(self):
        return f"Codigo: {self.codigo} \nDescricao: {self.descricao}, \nLocalizacao: {self.localizacao}, \nSituação: {self.situacao}"
    
    def set_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def set_localizacao(self, nova_localizacao):
        self.localizacao = nova_localizacao

    def set_situacao(self, nova_situacao):
        if nova_situacao in ["Disponível", "Em uso", "Em manutenção"]:
            self.situacao = nova_situacao
            return True
        return False

class Controle:

    def __init__(self):
        self.bens = []
    
    def carregar(self,item):
            with open("patrimonio.pkl", "wb") as arquivo:
                    pickle.dump(item, arquivo)
                    print("Dados gravados com sucesso!")
    def cadastrar(self):
            cod = input("cod:")
            leg = input("leg:")
            loc = input("loc:")
            sit = input("sit:")
            bem = Bem(cod,leg,loc,sit)
            self.bens.append(bem)
            self.carregar(self.bens)

    def imprimir(self):
         for bem in self.bens:
              print(bem)
c = Controle()
c.cadastrar()
c.imprimir()
c.cadastrar()
c.imprimir()
c.cadastrar()
c.imprimir()
#formatando(cod,leg,loc,sit)

"""      
dados2 = [{"1","dasl0","dkf","jcaji"},{"2","asd","dsjnf","dnsj"}]
dados = [{"Codigo": " 105", 
          "descricao": " Computador I7 com 16GB de RAM",
          "localizacao": "C1 - Sala 30",
          "Situacao":"Em uso"
          },
         {"Codigo": " 104", 
          "descricao": " Computador I7 com 16GB de RAM",
          "localizacao": "C1 - Sala 30",
          "Situacao":"Em uso"
          },
         {"Codigo": " 106",  
          "descricao": " Computador I7 com 16GB de RAM",
          "localizacao": "C1 - Sala 30",
          "Situacao":"Em uso"
          }]
while True:
    cod = input("cod:")
    leg = input("leg:")
    loc = input("loc:")
    sit = input("sit:")
    def formatando(cod,leg,loc,sit):
        novo = {"Codigo": cod,  
          "descricao": leg,
          "localizacao": loc,
          "Situacao":sit
          }
        return novo 

    adicionar = formatando(cod,leg,loc,sit)
    dados.append(adicionar)
    try:
        with open("patrimonio.pkl", "wb") as arquivo:
            pickle.dump(dados, arquivo)
            print("Dados gravados com sucesso!")
    except FileNotFoundError:
        print("Erro: caminho do arquivo inválido.")
    except PermissionError:
        print("Erro: sem permissão para gravar o arquivo.")
    except pickle.PickleError as e:
        print(f"Erro ao serializar os dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    try:
            with open("patrimonio.pkl","rb") as arquivo:
                dados_carregados = pickle.load(arquivo)
            for item in dados_carregados:
                    print(f"Código: {item['Codigo']}")
                    print(f"Descrição: {item['descricao']}")
                    print(f"Localização: {item['localizacao']}")
                    print(f"Situação: {item['Situacao']}")
                    print("-" * 40)
    except PermissionError as e:
                print("sem permissao")
    except Exception as e:
                print("que issooooooooooo")"""