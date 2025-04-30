# Insertion Sort
# O Insertion Sort percorre a lista, inserindo cada valor na posição correta entre os elementos à esquerda.
def insertion_sortio(v):
    for i in range(1, len(v)):
        x= v[i] # Armazena o valor atual que será inserido na posição correta
        j = i-1 # Elemento anterior ao índice atual
        while j >= 0 and x < v[j]: # Enquanto j estiver dentro da lista (j >= 0) e x for menor que v[j], continue deslocando
            v[j+1] = v[j] # Desloca o elemento maior para a direita
            j-=1 # Diminui J para continuar comparando com os elementos anteriores
        v[j+1] = x # Insere x na posição correta encontrada