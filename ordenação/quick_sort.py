#Quick Sort
# O algoritmo quick_sort aplica a estratégia de dividir para conquistar, escolhendo um pivô e reorganizando os elementos menores à esquerda e os maiores à direita, de forma recursiva.

def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2  # Calcula o índice do elemento central
    pivo = v[meio]           # Define o pivô como o valor do elemento central
    i = ini
    j = fim

    while i <= j:  # Enquanto os ponteiros não se cruzarem
        # Avança da esquerda até encontrar um valor maior ou igual ao pivô
        while v[i] < pivo:
            i += 1
        # Recua da direita até encontrar um valor menor ou igual ao pivô
        while v[j] > pivo:
            j -= 1
        # Se os ponteiros ainda não se cruzaram, troca os elementos
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1

    # Chamada recursiva para as duas metades do vetor
    if ini < j:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)
