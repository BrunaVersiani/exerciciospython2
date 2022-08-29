'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print('\033[36m-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
listagem = ('borracha', 0.50,
            'lapis', 1.00,
            'caneta', 2.00,
            'papel', 20.00,
            'caderno', 15.25,
            'estojo', 15.60,
            'tesoura', 6.80,
            'cola', 4.75,
            'apontador', 0.90,
            'clipes', 3.25)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('-' * 40)
