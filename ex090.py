'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input(f'Digite a média do {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['situação'] = 'Aprovado(a)'
elif 5 <= aluno['Media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado(a)'
print('*-' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v} ')
print('*-' * 20)
