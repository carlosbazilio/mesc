# Uso da biblioteca time para cálculo de 
# tempo de execução da chamadas das diferentes
# versões de fib.

import time
import sys
from fib import *

start = time.time()

x = fib(int(sys.argv[1]))

end = time.time()

print(end - start)
print(x)
