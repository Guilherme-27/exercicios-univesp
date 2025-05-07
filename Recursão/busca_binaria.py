l = [1, 3, 5, 7, 11, 12, 23, 27, 33, 44, 57, 68, 100, 102]

def busca_binaria(lista, x, ini, fim):
    # Lista, número procurado, posição de início e fim
    if ini > fim:
        return -1  # Valor não encontrado

    meio = (ini + fim) // 2

    if lista[meio] == x:
        return meio
    elif lista[meio] > x:
        return busca_binaria(lista, x, ini, meio - 1)
    else:
        return busca_binaria(lista, x, meio + 1, fim)

print(busca_binaria(l, 100, 0, len(l)-1))