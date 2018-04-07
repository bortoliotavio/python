count2 = 0
for num in range (2, 1000):
    tipo = 'multiplo2' if (num % 2 == 0) else 'count2'
    count2 = count2 + 1
    print('A quantidade de multiplos de 2 entre 2 e 1000 e {}'.format(count2))