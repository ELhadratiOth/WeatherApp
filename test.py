from collections import Counter


def unique_list_of_size_six_with_indices(lst):
    count = Counter(lst)  # Compter le nombre d'occurrences de chaque élément
    unique_values = list(count.keys())  # Obtenir les valeurs uniques

    result = []  # Liste résultante
    indices = []  # Indices des éléments utilisés

    # Créer une nouvelle liste avec les éléments uniques jusqu'à ce qu'elle atteigne la taille de 6
    for index, value in enumerate(lst):
        if len(result) < 6:
            if value in unique_values:
                result.append(value)
                indices.append(index)
                unique_values.remove(value)  # Retirer la valeur de la liste des valeurs uniques
        else:
            break

    # Si la liste résultante a moins de 6 éléments, compléter avec les valeurs restantes de la liste d'origine
    while len(result) < 6:
        for index, value in enumerate(lst):
            if len(result) < 6:
                result.append(value)
                indices.append(index)

    return result, indices


# Liste principale
main_list = [3, 80, 61, 80, 3, 3, 3, 3, 3, 3, 99, 80, 80, 3, 61, 61, 80, 80, 3, 61, 3, 3, 3, 3, 3]

# Obtenir la liste unique de 6 éléments et les indices correspondants
unique_six_list, used_indices = unique_list_of_size_six_with_indices(main_list)

print("Liste unique de taille 6:", unique_six_list)
print("Indices des éléments utilisés:", used_indices)
