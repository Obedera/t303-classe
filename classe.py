from datetime import date, datetime
from math import floor

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def set_nome(self, valor):
        self._nome = valor
    
    def get_nome(self):
        return self._nome
    
    def set_idade(self, valor):
        self._idade = valor
    
    def get_idade(self):
        return self._idade
    
    def falar(self):
        return print('Talkey')


class Pet(Pessoa):
    def __init__(self, dono,idade_dono, nome, data_nasc):
        super().__init__(dono,idade_dono)
        self.nome = nome
        data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y').date()
        self.data_nasc = data_nasc
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, valor):
        self.nome = valor

    def get_dono(self):
        return super().get_nome()

    def set_dono(self, valor):
        super().set_nome(valor)

    def set_data_nasc(self, valor):
        data_nasc = datetime.strptime(valor, '%d/%m/%Y').date()
        self.data_nasc = data_nasc
    
    def get_idade(self):
        data_atual = datetime.now().date()
        idade =  int((data_atual-self.data_nasc).days)
        return floor((idade/365))

    def get_dados(self):
        print(f'O nome do dono é {self.get_dono()} e sua idade é {super().get_idade()} anos')
        print(f'O nome do pet é {self.get_nome()} e sua idade é {self.get_idade()}')


obede = Pessoa('Obede', '15')
costela = Pet('Obede', '15', 'Costela', '25/09/2017')

costela.set_nome('Costelinha')
costela.set_dono('Obedera')

costela.get_dados()
obede.falar()

costela.set_data_nasc('25/09/2016')

costela.get_dados()