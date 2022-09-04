'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temporaria = []
principal = []
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'nN':
        break




print(f'A quantidade de pessoas cadastradas foi {len(principal)}')
