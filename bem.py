class Bem:
    def __init__(self, codigo, descricao, localizacao, situacao):
        self.__codigo = codigo
        self.descricao = descricao
        self.localizacao = localizacao
        self.situacao = situacao
    
    def __str__(self):
        return (
            f"Codigo: {self.__codigo}\n"
            f"Descricao: {self.descricao}\n"
            f"Localizacao: {self.localizacao}\n"
            f"Situação: {self.situacao}"
        )
 
    @property
    def codigo(self):
        return self.__codigo

    def set_descricao(self, nova_descricao:str):
        self.descricao = nova_descricao

    def set_localizacao(self, nova_localizacao:str):
        self.localizacao = nova_localizacao

    def set_situacao(self, nova_situacao:str):
        self.situacao = nova_situacao
           
