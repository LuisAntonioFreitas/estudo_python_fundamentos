# # cria arquivo
# arquivo = open('teste.txt', 'w')
# arquivo.write('Primeira linha')
# arquivo.close

# # atualiza arquivo
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nSegunda linha')
# arquivo.close

def escrever_arquivo(nome_arquivo, texto):
  # 'w' criar o arquivo se ele não existir e 
  # coloca apenas este novo texto
  arquivo = open(nome_arquivo, 'w')
  arquivo.write(texto + '\n')
  arquivo.close

def atualizar_arquivo(nome_arquivo, texto):
  # 'a' criar o arquivo se ele não existir e 
  # adiciona o novo texto ao que já existe no arquivo
  arquivo = open(nome_arquivo, 'a')
  arquivo.write(texto + '\n')
  arquivo.close

def ler_arquivo(nome_arquivo):
  # 'r' faz a leitura do arquivo
  arquivo = open(nome_arquivo, 'r')
  texto = arquivo.read()
  arquivo.close
  print(texto)

def copia_arquivo(nome_arquivo, novo_nome_arquivo = '', novo_local = ''):
  import shutil as copiar
  import os as os
  if not nome_arquivo == '':
    if novo_nome_arquivo == '':
      novo_nome_arquivo = nome_arquivo
    local = novo_local
    if not local == '':
      local = local + '/'
    copiar.copy(nome_arquivo, local + novo_nome_arquivo)

def move_arquivo(nome_arquivo, novo_nome_arquivo = '', novo_local = ''):
  import shutil as mover
  import os as os
  if not nome_arquivo == '':
    if novo_nome_arquivo == '':
      novo_nome_arquivo = nome_arquivo
    local = novo_local
    if not local == '':
      local = local + '/'
    mover.move(nome_arquivo, local + novo_nome_arquivo)


def media_notas(nome_arquivo):
  arquivo = open(nome_arquivo, 'r')
  aluno_nota = arquivo.read()
  arquivo.close
  print(aluno_nota)
  aluno_nota = aluno_nota.split('\n')
  print(aluno_nota)
  lista_media = []
  resultado = ''
  for x in aluno_nota:
    lista_notas = x.split(',')
    print(lista_notas)
    aluno = lista_notas[0]
    lista_notas.pop(0)
    print(aluno)
    print(lista_notas)
    calcula_media = lambda notas: sum([int(i) for i in notas]) / len(lista_notas) if (len(lista_notas) > 0) else 1
    media = calcula_media(lista_notas)
    print(media)
    if not aluno == '':
      lista_media.append({aluno:media})
      resultado = resultado + 'Aluno {an} teve média {md} em suas notas {nt}.\n'.format(an=aluno, md=media, nt=lista_notas)
  print(lista_media)
  for y in lista_media:
    for an, md in y.items():
      print('Aluno {an} teve média {md}.'.format(an=an, md=md))
  print(resultado)

if __name__ == "__main__":
  escrever_arquivo('teste.txt', 'Primeira linha')
  atualizar_arquivo('teste.txt', 'Segunda linha')
  atualizar_arquivo('teste.txt', 'Terceira linha')
  ler_arquivo('teste.txt')
  atualizar_arquivo('teste.txt', 'Quarta linha')
  ler_arquivo('teste.txt')

  aluno = 'Rafael,10,10,5,5'
  escrever_arquivo('notas.txt', aluno)
  aluno = 'Felipe,7,8,5,6'
  atualizar_arquivo('notas.txt', aluno)
  aluno = 'Galleani,7,8,5,6'
  atualizar_arquivo('notas.txt', aluno)
  aluno = 'Cesar,7,9,3,8'
  atualizar_arquivo('notas.txt', aluno)
  ler_arquivo('notas.txt')

  media_notas('notas.txt')

  copia_arquivo('notas.txt', 'notas_finais.txt')
  copia_arquivo('notas.txt', 'notas_finais.txt', 'E:/DESENVOLVIMENTO/ESTUDO/Python/estudo_app_python/copia')
  move_arquivo('notas_finais.txt', 'novas_notas_finais.txt', 'E:/DESENVOLVIMENTO/ESTUDO/Python/estudo_app_python/move')