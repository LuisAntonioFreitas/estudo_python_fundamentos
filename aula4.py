# for x in range(10):
#   print(x)

# for x in range(1, 10):
#   print(x)

# a = int(input('Entre com um número: '))
# div = 0
# for x in range(1, (a + 1)):
#   resto = a % x
#   print(x, resto)
#   if resto == 0:
#     div += 1
# if div == 2:
#   print('Número {} é primo'.format(a))
# else:
#   print('Número {} não é primo'.format(a))

# for num in range(101):
#   div = 0
#   for x in range(1, (num + 1)):
#     resto = num % x
#     if resto == 0:
#       div += 1
#   if div == 2:
#     print(num)

# a = 0
# while a <= 10:
#   print(a)
#   a += 1

nota = int(input('Entre com a nota: '))
while nota > 10:
  nota = int(input('Nota inválida. Entre com uma nova nota: '))
print('Nota = {}'.format(nota))
