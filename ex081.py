'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? ')).strip()
    if resposta in 'nN':
        break
print('=-' * 30)
print(f'Foram digitados {len(valores)} Valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('Sim, o número 5 faz parte da lista.')
else:
    print('Não encontrei o número 5. ')
