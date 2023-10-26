
# Soit une fonction qui inverse lettre qui prend en entrée une chaine de caracctère
# et renvoit une chaine de caractère des lettres inversées


"""
def inverse_letter(input):
    if isinstance(input, str):
        return input[::-1]
    elif isinstance(input, list):
        result = []
        for i in input:
            if isinstance(i, str):
                result.append(i[::-1])
            else:
                result.append(None)
        return result
    else:
        return None"""

"""
def inverse_letter(incitius):

# initialisation de la variable qui va stocker les lettres inversées
    resultat = ""
# Mettre le dernier élément i à la position    
    i = len(incitius) - 1
# Tant que l'élément i est sup = 0, on ajoute au resultat la lettre correspondant à la position
    while i >= 0:
        resultat = resultat + incitius[i]
    # Itération jusqu'à ce i devient inf 0
        i = i - 1

    return resultat
"""


def inverse_mot(x):
    p = len(x) - 1
    result = ""
    for i in range(p, -1, -1):
        result += x[i]

    return result


t = 'trf'
societe = "INCITIUS"
list_info = ["Incitius", "se", "situe", "Montpellier"]

print(inverse_mot(t))
print(inverse_mot(societe))
print(inverse_mot(list_info))
