import sys
def fatorial_recursivo(n):
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)

try:
    print(fatorial_recursivo(1000))
except RecursionError as e:
    print("RecursionError:", e)
    print("Limite de profundidade:", sys.getrecursionlimit())
