option1 = ''
while option1 != 'exit':
    option1 = str(input('JOGADOR 1: Escolha pedra papel ou tesoura: '))
    option2 = str(input('JOGADOR 2: Escolha pedra papel ou tesoura: ')) 
    if option1 ==  option2:
        print ('EMPATE')
    elif option1 == 'pedra' and option2 == 'tesoura' or option1 == 'tesoura' and option2 == 'papel' or option1 == 'papel' and option2 == 'pedra':
        print('jogador 1 ganhou')
    elif option2 == 'pedra' and option1 == 'tesoura' or option2 == 'tesoura' and option1 == 'papel' or option2 == 'papel' and option1 == 'pedra':
        print('jogador 2 ganhou')
    elif option1 == 'exit':
        print('APERTE ENTER NOVAMENTE PRA FECHAR')
    else:
        print('ERRO TENTE NOVAMENTE')