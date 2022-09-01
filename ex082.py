'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas lista extras que vão
 conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
valores = []
impares = []
pares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? ')).strip()
    if resposta in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'Os valores digitados foram: {valores}')
print(f'Os némeros pares registrados foram: {pares}')
print(f'Os numeros impares registrados foram: {impares}')

