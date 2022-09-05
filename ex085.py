'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
 única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lista = [[], []]
valores = 0
for l in range(0, 7):
    valores = int(input(f'Digite o {l + 1}° numero: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares digitados são: {lista[0]}')
print(f'Os nuemros impares digitados são: {lista[1]}')
