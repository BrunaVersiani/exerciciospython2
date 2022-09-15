'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
 em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano nascimento: '))
dados['ctps'] = int(input('CTPS: '))



print('\033[36m*-' * 20)




print('*-' * 20)