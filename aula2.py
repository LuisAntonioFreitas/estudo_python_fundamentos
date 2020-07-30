a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
#a = 10
#b = 6
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print('soma : ' + soma)
print(subtracao)
print(multiplicacao)
print(type(divisao))
divisao = int(divisao)
print(divisao)
print(resto)
x = '1'
soma2 = int(x) + 1
print('soma2: ' + str(soma2))
print('Multiplicacao: {}. Resto: {}'.format(multiplicacao, resto))
print('Multiplicacao: {sm}. \nResto: {rs}'.format(sm=multiplicacao, rs=resto))