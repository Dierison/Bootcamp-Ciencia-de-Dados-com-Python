nome = 'Dierison'
idade = 27
profissao = 'Programador'
linguagem = 'Python'
saldo = 45.534

dados = {'nome': 'Dierison', 'idade': 27}

print('Nome: %s Idade: %d' % (nome, idade))

print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))
print('Nome: {name} Idade: {age}'.format(name=nome, age=idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}')