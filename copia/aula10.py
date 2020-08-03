from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
  data_atual = date.today()
  print(data_atual.strftime('%d/%m/%Y')) #02/08/2020
  print(data_atual.strftime('%d-%m-%Y')) #02-08-2020

  data_atual_str = data_atual.strftime('%A %B %Y') #Sunday August 2020
  print(type(data_atual))
  print(data_atual)
  print(type(data_atual_str))
  print(data_atual_str)

def trabalhando_com_datetime_e_time():
  horario = datetime.now()
  print(type(horario))
  print(horario)

  horario = datetime.today()
  print(type(horario))
  print(horario)
  print(horario.strftime('%H:%M:%S')) #20:41:05
  print(horario.strftime('%c')) #Sun Aug  2 20:44:51 2020
  print(horario.year) # 2020
  print(horario.weekday) #Sun
  tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
  print(tupla[horario.weekday()]) # Domingo

  horario = time(hour=15, minute=18, second=30)
  print(type(horario))
  print(horario)

  data_criada = datetime(2018, 6, 20, 15, 30, 20)
  print(data_criada)
  print(data_criada.strftime('%c'))

def converte_data(data_string):
  data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
  print(type(data_convertida))
  print(data_convertida)
  print('Dia: {}'.format(data_convertida.day))
  print('Mês: {}'.format(data_convertida.month))
  print('Ano: {}'.format(data_convertida.year))

def soma_e_subtrai_data():
  data = datetime.now()
  nova_data = data + timedelta(days=365)
  print(nova_data)

  nova_data = data - timedelta(days=365)
  print(nova_data)

  nova_data = data + timedelta(days=365 * 2, hours=2, minutes=15)
  print(nova_data)


if __name__ == "__main__":
  trabalhando_com_date()
  trabalhando_com_datetime_e_time()
  converte_data('11/11/2020')
  soma_e_subtrai_data()
    