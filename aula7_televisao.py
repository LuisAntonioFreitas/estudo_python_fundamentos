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

if __name__ == "__main__":
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

