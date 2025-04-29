# Exercício:
# Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal.
#
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila,
# dependendo da idade de cada uma (acima de 60 anos entra na fila prioritária).
#
# A saída de pessoas da fila deve ocorrer da seguinte forma:
# a cada duas pessoas que saem da fila prioritária, uma sai da fila normal.

#First In First Out - FIFO
class Fila:
    def __init__(self):
        self.data = []
        
    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)
    
    def empty(self):
        return not len(self.data) > 0
    
    def __str__(self):
        return f'{self.data}'

def gerenciamento_filas():
    normal = Fila()
    prioritaria = Fila()
    quantidade = int(input('Digite o total de pessoas que entrarão na fila: '))

    while quantidade > 0:
        nome = input('Digite o nome da pessoa: ')
        idade = int(input(f'Digite a idade de {nome}: '))
        if idade >= 60:
            prioritaria.insert(nome)
        else:
            normal.insert(nome)
        quantidade -= 1
        
    while not prioritaria.empty() or not normal.empty():
        print(prioritaria.remove())
        print(prioritaria.remove())
        print(normal.remove())

gerenciamento_filas()