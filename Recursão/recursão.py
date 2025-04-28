# Desafio: somar todos os números pares de uma lista, usando recursão
l = [3, 4, 7, 10, 5]

def soma_pares(lista, n=0):
    if n == len(lista) - 1: # Esse if trata o caso base, se for par retona o número, se for impar retorna 0
        if lista[n]%2== 0:
            return lista[n]
        else: 
            return 0
    if lista[n]%2== 0: # Se o numero for par, ele retorna a soma do número com o return dos outros processos
        soma = lista[n] + soma_pares(lista, n+1) 
    else: # Se o número for ímpar, retorna 0 + o return dos outros processos
        soma = soma_pares(lista, n+1)

    return soma # -> Retorna a soma de cada processo

print(soma_pares(l))