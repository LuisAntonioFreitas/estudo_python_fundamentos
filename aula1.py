print("Meu primeiro Python")
a = 1
b = 2
soma = a + b
print(soma) 

str1 = "this i/s stri/ng example....wow!!!"
str2 = "e/xam"

print(str1.find('s'))
print(str1.find('s', 1))
print(str1.find(str2, 40, 45))

# mostra o último caracter
x = 'Luis Antonio'
n = x[-1:]
print(n)

# mostra o primeiro caracter
x = 'Luis Antonio'
n = x[:1]
print(n)

# mostra do primeiro ao penúltimo caracter
x = 'Luis Antonio'
n = x[:-1]
print(n)

# mostra do segundo ao último caracter
x = 'Luis Antonio'
n = x[1:]
print(n)

# mostra do segundo ao penúltimo caracter
x = 'Luis Antonio'
n = x[1:-1]
print(n)