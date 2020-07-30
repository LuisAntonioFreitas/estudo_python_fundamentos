lista = [12, 10, 7, 5]
lista_animal = ['elefante', 'gato', 'cachorro']

print(type(lista))
print(lista)

print(lista_animal[1])

for x in lista_animal:
  print(x)

for x in range(3):
  print(lista_animal[x])

print(sum(lista))
print(max(lista))
print(min(lista))

#alfabeto
print(max(lista_animal))
print(min(lista_animal))

nova_lista = lista * 3
print(nova_lista)

if 'gato' in lista_animal:
  print('existe um gato na lista')
  #lista_animal.pop(1)
  lista_animal.remove('gato')
  print(lista_animal)
else: 
  print('não existe um gato na lista')

if 'lobo' in lista_animal:
  print('existe um lobo na lista')
else: 
  print('não existe um lobo na lista')
  lista_animal.append('lobo')
  print(lista_animal)

lista_animal.pop()
print(lista_animal)

lista_animal.append('gato')

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

lista_animal.reverse()
print(lista_animal)

lista_animal[0] = 'macaco'
print(lista_animal)

#se cria a tupla usando (parenteses) ela é imutável
tupla = (1, 10, 12, 14)
print(tupla)

print(len(tupla))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

print(tupla_animal[0])

nova_lista_animal = list(tupla_animal)
print(type(nova_lista_animal))
print(nova_lista_animal)

nova_lista_animal.insert(1, "gato")
print(nova_lista_animal)