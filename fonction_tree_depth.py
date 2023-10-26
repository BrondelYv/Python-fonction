def tree_depth(tree):

    if isinstance(tree, list):
        node, left, right = tree        # Si tree est une liste, on la décompose en trois éléments
    # for i in range(0, len(tree), 1):
        if isinstance(left, list):
            left_depth = tree_depth(left)    # si vrai on calcule la profondeur du sous arbre gauche de façon récursive
        else:
            left_depth = 0
        if isinstance(right, list):
            right_depth = tree_depth(right)    # si vrai on calcule la profondeur du sous arbre droit de façon récursive
        else:
            right_depth = 0

        maxi = max(left_depth, right_depth) + 1
        return maxi
    else:
        return 0


# print(tree_depth([1, [2, 4, [5, 7, 8]], [3, None, [6, 9, None]]]))


y = [1, [2, 4, [5, 7, 8]], [3, None, [6, 9, None]]]

print(tree_depth(y))
