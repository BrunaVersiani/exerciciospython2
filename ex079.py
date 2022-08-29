'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('\033[32mNúmero adicionado com sucesso...\033[m')
    else:
        print('\033[31mNúmero duplicado, não posso adicionar...\033[m')
    continua = str(input('Deseja continuar? ')).upper().strip()[0]
    if continua == 'N':
        break
numeros.sort()
print(f'\033[34mOs números adicionados foram: {numeros}')
