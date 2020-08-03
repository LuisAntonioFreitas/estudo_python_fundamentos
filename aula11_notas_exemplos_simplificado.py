class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

def get_error(nota):
    raise InputError('Nota não pode ser maior do que 10!!!') if nota > 10 else InputError('Nota não pode ser menor do que 0!!!')

def avaliar_aluno():
    notas_input = []
    notas = ('Primeira Nota', 'Segunda Nota', 'Terceira Nota', 'Quarta Nota')
    index = 0
    
    while (len(notas_input) < len(notas)):
        try:
            nota = float(input('Digite a {}: '.format(notas[index])))
            notas_input.append(nota) if (int(nota) in range(0, 11)) else get_error(nota)
            index += 1
        except ValueError:
            print('Valor inválido. Deve-se digitar apenas números!!!')
        except InputError as ex:
            print(ex)
    
    calc_media = lambda lista_notas : (sum(lista_notas) / len(lista_notas))

    media = calc_media(notas_input)
    
    print('A sua média é: {:.2f}\n'.format(media))
    
    if media >= 7:
        print('Parabéns você foi APROVADO!!!')
    elif media >= 5:
        print('Atenção! Você ficou em RECUPERAÇÃO!!!')
    else:
        print('Infelizmente! Você REPROVOU!!!')
    

avaliar_aluno()