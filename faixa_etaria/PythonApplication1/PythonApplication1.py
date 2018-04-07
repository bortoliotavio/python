idade = int(input('Digite sua idade: '))

if idade < 14:
    print('Voce e uma criança')
elif  idade < 25 :
    print('voce e um jovem')
elif idade < 65:
    print('voce e adulto')
else :
    print('voce e idoso')