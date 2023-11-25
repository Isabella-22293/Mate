
def PrimosAlAzar(x, y):
    lista_primos = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            lista_primos.append(n)

    return lista_primos


from math import gcd

def encontrar_e(y, cantidad):
    es = []
    e = 2
    while len(es) < cantidad:
        if gcd(e, y) == 1:
            es.append(e)
        e += 1
    return es