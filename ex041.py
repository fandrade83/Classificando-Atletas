from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O Atleta tem {idade} anos. ')
if idade <= 9:
    print('Classificação: MIRIN')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
else:
    print('Classificação: MASTER')
