'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
print('\033[36m+'*40)
maior = menor = 0
listagem = []
for c in range(0, 5):
    listagem.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listagem[c]
    else:
        if listagem[c] > maior:
            maior = listagem[c]
        if listagem[c] < menor:
            menor = listagem[c]
print('+'*40)
print(f'Os valores digitados foram: {listagem}')
print(f'O MAIOR valor digitado foi {maior} nas posições: ', end='')
for indice, valor in enumerate(listagem):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'E o MENOR valor digitado foi {menor} nas posições: ', end='')
for indice, valor in enumerate(listagem):
    if valor == menor:
        print(f'{indice}...', end='')
print()
