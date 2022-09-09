'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = [[], [], []]
cont = 0
while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite nota 1: '))
    nota2 = int(input('Digite nota 2: '))
    if aluno not in lista:
        lista[0].append(aluno)
        lista[1].append(nota1)
        lista[2].append(nota2)
        cont += 1
    continua = str(input('Deseja continuar? [S/N]'))
    if continua in 'Nn':
        break
print(lista)
print(cont)
