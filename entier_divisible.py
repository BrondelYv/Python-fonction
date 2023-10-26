# Soit une fonction qui prend des valeurs allant de 1 à n et qui vérifie si n est divisible par 3 et 5
# et qui imprime une chaine de caractère si cela est vraie

def integer(n):
    for i in range(1, n+1):           # n+1 est exclut dans cette fonction donc i prend que les valeurs allant de 1 à n
        if i % 3 == 0 and i % 5 == 0:       # vérification du reste entier de la division avec l'expression % modulo
            print('payo')
        elif i % 5 == 0:
            print('yo')
        elif i % 3 == 0:
            print('pa')


x = 20
print(integer(x))
