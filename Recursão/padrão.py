# Implemente o método recursivo pattern2(), que aceita um inteiro não negativo como entrada e exibe o padrão mostrado a seguir. Os padrões para as entradas 0 e 1 são nada e um asterisco, respectivamente:

# >>> pattern2(0)
# >>> pattern2(1)
# *

# Os padrões para as entradas 2 e 3 aparecem em seguida.

# >>> pattern2(2)
# *
# **
# *
# >>> pattern2(3)
# *
# **
# *
# ***
# *
# **
# *

def pattern(n):
    if n == 0:
        return ''
    else:
        pattern(n-1)
        print(n*'*')
        pattern(n-1)

pattern(3)