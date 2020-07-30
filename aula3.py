a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# if a > b:
#   print('O primeiro número é {} e é o maior'.format(a))
# else:
#   print('O segundo número é {} e é o maior'.format(b))

if (a > b and a > c):
  resto = a % 2
  parimpar = 'par' if (resto == 0) else 'impar'
  print('O primeiro número é {} que é {} e é o maior que {} e {}'.format(a, parimpar, b, c))
elif (b > a and b > c):
  resto = b % 2
  parimpar = 'par' if (resto == 0) else 'impar'
  print('O segundo número é {} que é {} e é o maior que {} e {}'.format(b, parimpar, a, c))
else:
  resto = c % 2
  parimpar = 'impar' if (not resto == 0) else 'par'
  print('O terceiro número é {n1} que é {parimpar} e é o maior que {n2} e {n3}'.format(n1=c, parimpar=parimpar, n2=a, n3=b))

print('Final do Programa')