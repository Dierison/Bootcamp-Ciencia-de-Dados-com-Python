nome = 'DiERisoN'

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '  Olá mundo!    '

print(texto.strip()  + '.')
print(texto.lstrip() + '.')
print(texto.rstrip() + '.')

menu = 'Python'

print(f'#### {menu} ####')
print(menu.center(14))
print(menu.center(14, '#'))
print('P-y-t-h-o-n')

for letra in menu:
    print(letra, end='-')
print()

print('-'.join(menu))