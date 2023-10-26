# Soit une fonction qui prend en entrée une matrice et un entier,
# et qui initialise la matrice en sortie par ce nombre entier.:

# DANS CE CAS NOUS ALLONS VOIR PLUSIEURS CAS DIFFERENTS QUI TRAITE
# LES MATRICES INITIALISEES DE DIMENSIONS 2 ou 3 ET MULTIDIMENSIONNELLES

"""
def matrice_constante(M,n):   # Ce cas traite les matrices rectangulaire de dimension 2
    rows = len(M)
    column = len(M[0])
    # Comprehension de list
    initmat = [[n for _ in range(column)] for _ in range(rows)]
    return initmat
"""
"""
def matrice_constante1(M, n):   # Ce cas traite les matrices rectangulaire de dimension 2
    rows = len(M)
    column = len(M[0])
    for i in range(rows):
        # Comprehension de list
        result = [[n] * column for _ in range(rows)]
        return result
"""
"""
def matrice_constante2(M, n):
    rows = len(M)
    column = len(M[0])
    matrix = []
    for rows in M:                            # Pour toutes les lignes, parcours la matrice M
       lign = []                             # Initialise la liste lign
    for i in rows:                        # Pour tous éléments k de la matrice parcours toutes les lignes
        lign.insert(0, n)          # ajoute le nombre n sur toutes les lignes
        lign.append(n)
        matrix.insert(0, lign)         # Ajoute chaque ligne contenant la valeur n à la matrice
        matrix.append(lign)
"""
"""
def matrice_constante2(M,n):  # Ce cas traite les matrices rectangulaire de dimension 2
    rows = len(M)
    column = len(M[0])
    matrix = []
    for i in range(rows):
          ligne = [n] * column
          matrix += [ligne]

    return matrix
"""
"""
import copy

def initmat(M, n):                          # Ce cas traite les matrices rectangulaire de dimension 2
    result = copy.deepcopy(M)
    for i in range(0,len(M), 1):
        for j in range(0, len(M[i]), 1):
            result[i][j] = n

    return result
"""
"""
def initmat2(mat, v):       # Ce cas traite les matrices à plusieurs dimensions
    if isinstance(mat, list):
        result = []
        for i in range(0, len(mat), 1):
# À chaque itération de la boucle, cette expression appelle récursivement la fonction initmat2 avec l'élément mat[i] 
# et la valeur v

            result.append(initmat2(mat[i], v))
    else:
        result = v
    return result
"""
"""
def initmat3(mat, v):           # Ce cas traite les matrices rectangulaire de dimension 2
    result = []
    for i in range(0, len(mat), 1):
        row = []
        for j in range(0, len(mat[i]), 1):
            row.append(v)
        result.append(row)
    return result
"""


def initmat4(mat, v):   # Ce cas traite les matrices rectangulaire de dimension 2
    result = []
    for r in mat:
        row = []
        for _ in r:
            row.append(v)
        result.append(row)
    return result


w = [
    [[1, 2, 4], [0, 2]],
    [[1, 2]],
    [[1, 2], [0, 2, 8]]
]

# print(matrice_constante(w,1))
# print(matrice_constante1(w,1))
# print(matrice_constante2(w,1))
print(initmat4(w, 1))
# print(initmat2(w,1))
# print(initmat3(w,1))
# print(initmat4(w,1))
