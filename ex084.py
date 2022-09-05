'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'nN':
        break
print('=*' * 30)
print(f'A quantidade de pessoas cadastradas foi {len(principal)}')
print(f'O maior peso cadastrado foi {maior}, peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado foi {menor}, peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
