#LIFO (Last In, First Out)
class Pilha:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
         
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True
        
        # uma abordagem mais sintética aqui seria:
        # return not len(self.data) > 0
        # retorna o valor negado de (essa pilha é > 0 ?)

def conversor_binário(x):
    #'Converte para binário usando uma pilha'
    p = Pilha()
    while x > 0 :
        resto = x%2
        x = x//2
        p.push(resto)
    while not p.empty():
        print(p.pop(), end='')

conversor_binário(13)