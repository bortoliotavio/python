n = int(input('Informe um numero : '))

fibonacci = [0, 1]

numero1 = 0
numero2 = 1

for n in range(3, n + 1):
    numero3 = numero1 + numero2

    fibonacci.append(numero3)

    numero1 = numero2
    numero2 = numero3

print(fibonacci[n - 1])