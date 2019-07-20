from datetime import date, datetime
from math import floor


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



class Pet(Pessoa):
    def __init__(self, dono,idade_dono, nome, data_nasc):
        super().__init__(dono,idade_dono)
        self.nome = nome
        data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y').date()
        self.data_nasc = data_nasc
    
    def get_dono(self):
        return super().get_nome()
    
    def get_idade_pet(self):
        data_atual = datetime.now().date()
        idade =  int((data_atual-self.data_nasc).days)
        return floor((idade/365))
    


obede = Pessoa('Obede', '15')
costela = Pet('Obede', '15', 'costela', '25/09/2017')

print(costela.get_idade_pet())