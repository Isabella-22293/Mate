import random
from Mods import *
from Dic import *
from Calculos import *
def menuDec():
    print("Ingrese el mensaje por descifrar")
    C = input("Mensaje a desencriptar (en bloques de 4 dígitos): ")
    print("Ingrese la clave privada para descifrar")
    d = encontrar_d(e, (43-1)*(59-1))    
    n = int(input("Ingrese el valor de n: "))
    descifrar(C, d, n)

def encontrar_d(e, phi):
    d = inverso_modular(e, phi)
    return d

def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def descifrar(C, d, n):
    bloques = [C[i:i+4] for i in range(0, len(C), 4)]
    nums_descifrados = [ExpMod(int(bloque), d, n) for bloque in bloques]

    # Convertir los números descifrados a letras según la codificación dada
    mensaje_descifrado = ''.join([inverso_diccionario[num // 100] + inverso_diccionario[num % 100] for num in nums_descifrados])

    print("Mensaje descifrado:", mensaje_descifrado)

def ExpMod(base, exp, mod):
    return pow(base, exp, mod)

inverso_diccionario = {v: k for k, v in dic3.items()}

