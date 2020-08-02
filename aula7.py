def soma(a, b): 
  return a + b

def subtracao(a, b):
  return a - b

print(soma(1, 2))
print(subtracao(4, 2))

# calculadora 1
class Calculadora1:
  def __init__ (self, num1, num2):
    self.valor_a = num1
    self.valor_b = num2

  def soma(self): 
    return self.valor_a + self.valor_b

  def subtracao(self):
    return self.valor_a - self.valor_b

calculadora1 = Calculadora1(10, 2)
print(calculadora1.soma())
print(calculadora1.subtracao())

# calculadora 2
class Calculadora2:
  def soma(self, valor_a, valor_b): 
    return valor_a + valor_b

  def subtracao(self, valor_a, valor_b):
    return valor_a - valor_b

calculadora2 = Calculadora2()
print(calculadora2.soma(10, 2))
print(calculadora2.subtracao(10, 2))

# televisão
class Televisao:
  def __init__(self):
    self.ligada = False
    self.canal = 5

  def power(self):
    if self.ligada:
      self.ligada = False
    else:
      self.ligada = True

  def aumenta_canal(self):
    if self.ligada:
      self.canal += 1

  def diminui_canal(self):
    if self.ligada:
      if self.canal > 1:
        self.canal -= 1

televisao = Televisao()
print('Televisão esta ligada: {}'.format('SIM' if (televisao.ligada) else 'NÃO'))
televisao.power()
print('Televisão esta ligada: {}'.format('SIM' if (televisao.ligada) else 'NÃO'))

televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal)) #7

televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal)) #8

televisao.power()
print('Televisão esta ligada: {}'.format('SIM' if (televisao.ligada) else 'NÃO'))

televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal)) #8 Televisão Desligada

