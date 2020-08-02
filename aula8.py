# importa apenas a classe nomeada do modulo
from aula7_televisao import Televisao

televisao1 = Televisao()
print(televisao1.ligada)

# importa todas as classes do modulo
import aula7_televisao

televisao2 = Televisao()
print(televisao2.ligada)
televisao2.power()
print(televisao2.ligada)

# importa apenas os metodos nomeados do modulo
from aula8_contador_letras import contador_letras, teste

lista = ['elefante', 'tartaruga', 'macaco']
total_letras = contador_letras(lista)
print('Total de Letras por Palavras da Lista: {}'.format(total_letras))
print(teste())