from random import shuffle

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f'{self.valor}{self.naipe}'
    
    def __repr__(self):
        return self.__str__()
    
class Baralho:
    def __init__ (self):
        self.baralho = []
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        naipes = ['\u2660', '\u2661', '\u2662', '\u2663']
        for valor in valores:
            for naipe in naipes:
                self.baralho.append(Carta(valor, naipe))
    
    def __str__(self):
        return f'{self.baralho}'
    
    def embaralhar(self):
        shuffle(self.baralho)
        
    def distribuir(self):
        return self.baralho.pop()