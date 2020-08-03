lista = [1, 10]

try:
  divisao = 10 / 1 #0
  numero = lista[1] #3
  #x = a

except ZeroDivisionError: 
  print('\nNão é possível realizar divisão por zero\n')
except ArithmeticError: 
  print('\nHouve um erro ao realizar uma operação aritmética\n')
except IndexError:
  print('\nErro ao acessar um índice inválido ba lista\n')
except BaseException as ex:
 print('\nErro desconhecido. Erro: {}\n'.format(ex))

else:
  #executa quando não ocorrer nenhum erro
  print('\nExecutado por não ocorrer erros\n')

finally:
  #sempre executa mesmo ocorrendo erros
  print('\nExecutado sempre mesmo ocorrendo erros\n')

