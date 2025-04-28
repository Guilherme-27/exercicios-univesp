l = [1,2,3,4,5,6,7,8,9]

def soma_lista(lista, n=0):
    if n == len(lista) - 1:
        return lista[n] # -> o útimo elemento da lista vai vir aqui, é o caso base

    soma = lista[n] + soma_lista(lista, n+1) # -> induz um empilhamento de processos que vai até o caso base

    return soma # -> retorna a soma de cada processo

print(soma_lista(l))