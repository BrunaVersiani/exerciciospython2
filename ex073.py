'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
 Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
print('\033[35m~*' * 40)
times = ('Dedos sem Unha', 'Drible Torto', 'Dyslexia', 'Chapecoense', 'Falência', 'Fanfarrões', 'Fim de Carreira',
         'Fora da lei ', 'Galo Frito', 'Inacreditável', 'Insano', 'Kapenga', 'Largados', 'Leões Sem Juba', 'Limitados',
         'Madruguinha', 'Meia Alta', 'Mosca Morta', 'Nada Consta', 'Neymala')

print(f'Colocação dos 5 primeiros Time: {times[0: 5]}')
print(f'Os últimos 4 collocados: {times[-4:]}')
print('Colocação do time Chapecoense: ', end='')
print(times.index('Chapecoense')+1)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('~*' * 40)

