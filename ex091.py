'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('\033[36m*-' * 20)
placar = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou nº {v} no dado.')
    sleep(1)
print('*-' * 20)
placar = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('--->  PLACAR DO JOGO  <---')
for i, v in enumerate(placar):
    print(f' {i+1}° Lugar: {v}')
    sleep(1)
