def pot (x, n):
    if n == 0 or x == 1: return 1
    return x * pot(x, n-1)
print (pot(2, 3))