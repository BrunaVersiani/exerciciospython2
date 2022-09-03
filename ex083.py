'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
 deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
expressão = str(input('Digite a sua expressão: '))
pilha = []
for simbolos in expressão:
    if simbolos == '(':
        pilha.append('(')
    elif simbolos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Ok! Sua expressão está valida!')
else:
    print('Sua expressão esta errada!')
