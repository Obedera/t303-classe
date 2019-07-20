class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
    
    def set_nome(self, valor):
        self._nome = valor
    
    def get_nome(self):
        return self._nome
    
    def set_idade(self, valor):
        self._idade = valor
    
    def get_idade(self):
        return self._idade




    


obede = Pessoa('Obede', '15')
