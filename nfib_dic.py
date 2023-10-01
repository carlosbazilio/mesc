# Função ineficiente para armazenagem dos
# n primeiros numeros da série de Fibonnaci
# num dicionário.

from fib_iter import *
import sys

def nfib(n):
	valores = {}
	i = 1
	for x in range(1,n):
		valores[i] = fib(x)
		i = i + 1
	return valores[n-1]

print(nfib(int(sys.argv[1])))
