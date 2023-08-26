nome = str(input(print('Informe o seu nome: ')))
idade = int(input(print('Informe a sua idade: ')))

print(f'O seu nome é: {nome} e tem {idade}', end='...\n')
print(f'O seu nome é: {nome} e tem {idade}', sep='#')
print(f'O seu nome é: {nome} e tem {idade}', end='...\n', sep='#')