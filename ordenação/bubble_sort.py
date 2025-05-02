#Bubble Sort
# O Bubble Sort percorre a lista e troca os elementos adjacentes sempre que o atual for maior que o próximo.

lista = [29, 10, 14, 37, 13, 5, 78, 3, 18, 25]

def bubble_sort(v):
    for i in range(len(v)-1): # Loop externo: controla o número de passagens (no máximo n-1 passagens são necessárias)
        for j in range(len(v)-i-1): # Loop interno: percorre os pares vizinhos até o último ainda não ordenado
            if v[j] > v[j+1]: # Se o elemento atual for maior que o próximo
                v[j], v[j+1] = v[j+1], v[j] # Troca os dois de posição

bubble_sort(lista)
print(lista)