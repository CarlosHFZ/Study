# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private ou protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no SETTER')
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
        


caneta = Caneta('Azul')
caneta.cor = 'Roxo'
caneta.cor_tampa = 'Azul'
#  getter -> obeter valor
print(caneta.cor)
print(caneta.cor_tampa)
