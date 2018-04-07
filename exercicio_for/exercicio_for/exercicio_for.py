ano = ''
ano_nascimento = ''
while ano != 0:
    ano_nascimento = int(input('Digite o ano do seu nascimento:'))
    if ano_nascimento < 1982:
        ano = ano_nascimento + 18
    else:
        ano = ano_nascimento + 16
    print('O ano do seu nascimento foi {} e o ano em que voce teve direito a voto foi {}'.format(ano_nascimento, ano))
