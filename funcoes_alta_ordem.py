# Exemplos de usos de funcoes de alta ordem

from functools import reduce

valores = [1,2,3,4]

def quadrado(x):
    return x * x

print(list(map(quadrado, valores)))

def par(x):
    return (x % 2) == 0

print(list(filter(par, valores)))

def soma(x, y):
    return x + y

print(reduce(soma, valores, 0))

