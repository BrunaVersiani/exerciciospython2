'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
 até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
print('\033[36m{:*^40}'.format(' Escrevendo por extenso '))
cont = ('Zero', 'um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezseis', 'Dezsete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Opção Inválida! Tente novamente. ')
print(f'Você digitou o número {cont[numero]}')
print('*' * 40)
