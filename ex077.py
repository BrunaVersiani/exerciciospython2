'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.'''
print('*' * 30)
palavras = ('este', 'texto', 'sobreviveu', 'salto', 'para', 'tipografia', 'electrónica',
            'essencialmente', 'inalterada', 'popularizada', 'anos', 'disponibilização','folhas',
            'continham', 'passagens', 'recentemente', 'programas', 'publicação', 'como')
for p in palavras:
    print(f'\nNa palavra\033[36m {p.upper()}\033[m temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
