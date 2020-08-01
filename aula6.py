conjunto = {1, 2, 3, 4, 4, 2}
print(type(conjunto))
print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto.discard(2)
print(conjunto)

conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

conjunto_diferenca1 = conjunto.difference(conjunto2)
print(conjunto_diferenca1)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca2)

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print(conjunto_superset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)