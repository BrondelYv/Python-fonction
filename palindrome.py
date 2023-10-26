
# Soit une fonction booléenne qui envoi True si le mot ou la chaine de caractère est un mot palindrome, sinon False

"""
def palindrome(x):
# la boucle for permet la facilité d'écriture, pour tout i, rangeons au départ len(x) - 1, l'arrivé à -1 et avec un pas de -1
    for i in range(len(x) - 1, -1, -1):   # inverse de notre mot
        if x[i] != x[len(x) - i - 1]:  # si le premier élément est différent du dernier, renvoie Faux
            return False
    return True
"""
"""
def palindrome(x):
    result = ""
    for c in x:
        result += c
        if result == x:
            return True
        else:
            return False
    return result
"""
"""
def palindrome(x):
    for i in range(len(x) - 1, len(x) // 2, -1):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True

"""
"""
def palindrome(x):
    i = len(x) - 1
    while i > len(x) // 2:
        if x[i] != x[len(x) - i - 1]:
            return False
        i = i - 1
    return True
"""

# print(palindrome('eelavalee'))
