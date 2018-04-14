hashtag = 1
n = int(input('Digite quantas linhas voce quer que seu triangulo: (linhas <=25)  '))
n += 1
f = (n * 2) - 1
while (n != 1):
    print('{}'.format(('#' * hashtag).center(f)))
    hashtag += 2
    n -= 1
