# Soit une fonction qui prend en entrée deux paramètre et qui renvoi une chaine de caractère
# avec des lettres intercalées par rapport aux paramètres d'entrés


def mot_intercaler(x, y):
    result = ""             # Initialisons la chaine de caractère pour stocker les caractere intercales
    k = min(len(x), len(y))   # Trouver la longueur du mot le plus court

    for i in range(k):          # Intercaler les caractères des deux mots
        result = result + x[i] + y[i]
        # result += y[i]

    if len(x) > len(y):                # Ajouter les caractères restants du mot le plus long
        for i in range(k, len(x)):
            result += x[i]
    else:
        for i in range(k, len(y)):
            result += y[i]
    return result


p = "yvell"
z = "brondel"

# print(min(len(z), len(p)))
t = mot_intercaler(p, z)
print(t)
