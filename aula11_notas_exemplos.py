class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:

    try:
        nota1 = int(input(f'Digite a Primeira Nota de 0 a 10: '))
        print(nota1)
        if nota1 > 10:
            raise InputError(f'Nota não pode ser maior do que 10!!!')
        elif nota1 < 0:
            raise InputError(f'Nota não pode ser menor do que 0!!!')

        nota2 = int(input(f'Digite a Segunda Nota de 0 a 10:'))
        print(nota2)
        if nota2 > 10:
            raise InputError(f'Nota não pode ser maior do que 10!!!')
        elif nota2 < 0:
            raise InputError(f'Nota não pode ser menor do que 0!!!')

        nota3 = int(input(f'Digite a Terceira Nota de 0 a 10:'))
        print(nota3)
        if nota3 > 10:
            raise InputError(f'Nota não pode ser maior do que 10!!!')
        elif nota3 < 0:
            raise InputError(f'Nota não pode ser menor do que 0!!!')

        nota4 = int(input(f'Digite a Quarta Nota de 0 a 10: '))
        print(nota4)
        if nota4 > 10:
            raise InputError(f'Nota não pode ser maior do que 10!!!')
        elif nota4 < 0:
            raise InputError(f'Nota não pode ser menor do que 0!!!')

        media = (nota1 + nota2 + nota3 + nota4) / 4

        print(f'A Media é: {media}')

        if media >= 7:
            print('Parabéns você foi APROVADO!!!')
        elif media >= 5:
            print('Atenção! Você ficou em RECUPERAÇÃO!!!')
        else:
            print('Infelizmente! Você REPROVOU!!!')
        break

    except ValueError:
        print(f'Valor inválido. Deve-se digitar apenas números!!!')
    except InputError as ex:
        print(ex)