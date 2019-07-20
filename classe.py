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
        self.data_nasc = data_nasc
    
    def get_dono(self):
        return super().get_nome()
    


obede = Pessoa('Obede', '15')
costela = Pet('Obede', '15', 'costela', '2018')


print(costela.get_dono())