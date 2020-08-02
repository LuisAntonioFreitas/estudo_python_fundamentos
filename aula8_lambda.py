contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['gato', 'cobra', 'papagaio']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

# dicionário
calculadora = {
  'soma': lambda a, b: a + b, 
  'subtracao': lambda a, b: a - b
}

print(type(calculadora))
somaX = calculadora['soma']
subtracaoX = calculadora['subtracao']
print('A soma é: {}'.format(somaX(10, 5)))
print('A subtração é: {}'.format(subtracaoX(10, 5)))