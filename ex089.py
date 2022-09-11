'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = list()
cont = 0
print('\033[36m*=' * 17)
while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite nota 1: '))
    nota2 = int(input('Digite nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([aluno, [nota1, nota2], media])
    continua = str(input('Deseja continuar? [S/N] ')).strip()
    if continua in 'Nn':
        break
print('*=' * 17)
print(f'{"N°":<5}{"Nome":<10}{"Média":>5}')
print('-' * 34)
for i, a in enumerate(lista):
    print(f'{i:<5}{a[0]:<10}{a[2]:>5.1f}')
while True:
    print('-' * 34)
    opção = int(input('Deseja ver notas de qual aluno? (Digite 999 para sair): '))
    if opção == 999:
        print('>>> FINALISANDO... <<<')
        break
    if opção <= len(lista) - 1:
        print(f'Notas de {lista[opção][0]} são {lista[opção][1]}')
print('*** VOLTE SEMPRE! ***')
