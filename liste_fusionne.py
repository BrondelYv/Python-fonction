# Soit une fonction qui prend en entrée 2 listes triées par ordre croissant et qui renvoit une liste triée et ordonnée


def fusion_lists(x, y):                     # x et y sont des listes d'ordre croissant
    result = []                              # Initialisation de la liste de stockage
    i, j = 0, 0                             # Initialisons les positions des indices des listes

    while i < len(x) and j < len(y):       # Tant que nous n'avons pas atteint la fin des deux listes, i et j continuent de les parcourir
        if x[i] < y[j]:                    # Si l'élément de la liste x à la position i est plus petit que l'élément de la liste y à la position j
            result.append(x[i])            # Ajoute l'élément de x à la liste result
            i += 1                         # Avance l'index i de x et l'index j de y d'une position + 1
        else:                              # Sinon,
            result.append(y[j])            # Ajoute l'élément de y à la liste result
            j += 1

    result.extend(y[j:])                   # Ajoute les éléments restants de la liste x et y à la liste result
    result.extend(x[i:])

    # while i < len(x):
    # result.append(x[i])
    # i += 1
    # while j < len(y):
    # result.append(y[j])
    # j += 1
    return result


# Soit les listes suivantes :
liste1 = [1, 3, 5, 7]
liste2 = [2, 4, 6, 8]
liste3 = fusion_lists(liste2, liste1)

print(liste3)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
