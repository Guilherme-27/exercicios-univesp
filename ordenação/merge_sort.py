# Merge Sort
# Usa o princípio de dividir para conquistar, quebra o vetor de forma similar à uma busca binária e depois volta reordenando.

def merge_sort(v, ini, fim):  
    if ini < fim:  # Condição de parada: só divide se houver mais de 1 elemento
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio, fim)

def intercala(v, ini, meio, fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    i = j = 0
    k = ini

    # Junta enquanto houver elementos em ambas as listas
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        k += 1

    # Copia o que sobrou (em L ou R)
    while i < len(L):
        v[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        v[k] = R[j]
        j += 1
        k += 1