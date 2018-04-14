def fatorial():
    fatorial = 1
    n = 0
    n = int(input('Digite o numero para voltar o fatorial:'))

    while n != 1:
        fatorial = fatorial * n
        n = n - 1
        continue

    return fatorial

print(fatorial())