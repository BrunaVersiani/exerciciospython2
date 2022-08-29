'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
núm = (int(input('Digite o 1° número: ')),
        int(input('Digite o 2° número: ')),
        int(input('Digite o 3° número: ')),
        int(input('Digite o 4° número: ')))
print(f'Você digitou os valores: {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O número 3 apareceu na posição {núm.index(3)+1}')
else:
    print('O número 3 não apareceu em nenhuma posição. ')
print('Os números pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
