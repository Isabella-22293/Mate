#Derek Arreaga 22537
#Isabella Miralles 22293
import random
from Mods import *
from Dic import *
from Calculos import *

def menuP():
    print("¿Qué desea hacer?")
    print("\t1. Cifrar")
    print("\t2. Descifrar")
    print("\t3. Salir")
    sel = input(": ")
    match sel:
        case "1":
            menuCif()
        case "2":
            menuDec()
        case "3":
            exit(0)

def menuCif():
    print("Ingrese el mensaje por cifrar")
    M = input("Palabra a encriptar: ")
    print("¿Cómo desea cifrar el mensaje?")
    print("1. Ingresar Clave Manual")
    print("2. Generar Clave Con Datos Predeterminados")
    sel = input(": ")

    match sel:
        case "1":
            cifradoManual(M)
        case "2":
            cifradoPredeterminado(M)

def cifradoManual(M):
    p = int(input("Ingrese el primer numero primo: "))
    q = int(input("Ingrese el segundo numero primo distinto al primero: "))
    if p==q:
        while q==p:
            q = int(input("Ingrese el segundo numero primo distinto a "+ str(p)))
    print("p",p,"q",q)
    n=p*q
    phi=(p-1)*(q-1)
    print("phi: ",phi)

    #mcd(e,y) = 1
    eList = encontrar_e(phi, 50)
    eSelect = None
    while eSelect == None :
        print("Ingresa uno de estos números para que sea el valor de e",eList)
        sel = input(": ")
        sel = int(sel)
        if sel in eList:
            eSelect = sel
    e = eSelect

    #Llamar la función de cifrar (e,phi)
    cifrar(M,e,n,phi)


def cifradoPredeterminado(M):
    # Clave pública (e, n)
    e, n = 13, 2537

    # Convertir el mensaje a números 
    numeros_mensaje = [dic3[M[i]] for i in range(len(M))]

    # Agrupar las letras en bloques de 2
    bloques = [numeros_mensaje[i:i+2] for i in range(0, len(numeros_mensaje), 2)]

    # Cifrar cada bloque
    mensaje_cifrado = [ExpMod(num[0] * 100 + num[1], e, n) for num in bloques]

    print("Mensaje cifrado:", mensaje_cifrado)

def descifrar(C, d, n):
    bloques = [C[i:i+4] for i in range(0, len(C), 4)]
    nums_descifrados = [ExpMod(int(bloque), d, n) for bloque in bloques]

def ExpMod(base, exp, mod):
    return pow(base, exp, mod)

def menuDec():
    print("Ingrese el mensaje por descifrar")
    C = input("Mensaje a desencriptar (en bloques de 4 dígitos): ")
    print("Ingrese la clave privada para descifrar")
    e = int("Ingrese el valor de e: ")
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





