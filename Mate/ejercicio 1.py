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
    print("3. Generar Clave Con Datos Randoms")
    print("4. Volver al Menu Principal")
    sel = input(": ")

    match sel:
        case "1":
            cifradoManual(M)
        case "2":
            cifradoPredeterminado(M)
        case "3":
            cifradoRandom(M)
        case "4":
            menuP()

def menuDec():
    print("Ingrese el mensaje por descifrar")
    C = input("Mensaje a desencriptar (en bloques de 4 dígitos): ")
    print("Ingrese la clave privada para descifrar")
    d = int(input("Ingrese el valor de d: "))
    n = int(input("Ingrese el valor de n: "))
    descifrar(C, d, n)

def cifradoManual(M):
    p = int(input("Ingrese el primer numero primo: "))
    q = int(input("Ingrese el segundo numero primo distinto al primero: "))
    if p==q:
        while q==p:
            q = int(input("Ingrese el segundo numero primo distinto a "+ str(p)))
    print("p",p,"q",q)
    #Usando p y q:
    n=p*q
    #calcular phi:
    phi=(p-1)*(q-1)
    print("phi: ",phi)

    #Hallar e, donde mcd(e,y) = 1
    eList = encontrar_e(phi, 50)
    #Elegir valor de e, puede ser el maximo comun divisor
    eSelect = None
    while eSelect == None :
        print("Ingresa uno de estos números para que sea el valor de e",eList)
        sel = input(": ")
        sel = int(sel)
        if sel in eList:
            eSelect = sel
    e = eSelect

    #Llamar la función de cifrar con los parámetros establecidos (e,phi)
    cifrar(M,e,n,phi)


def cifradoPredeterminado(M):
    # Clave pública (e, n)
    e, n = 13, 2537

    # Convertir el mensaje a números según la codificación dada
    numeros_mensaje = [dic3[M[i]] for i in range(len(M))]

    # Agrupar las letras en bloques de 2
    bloques = [numeros_mensaje[i:i+2] for i in range(0, len(numeros_mensaje), 2)]

    # Cifrar cada bloque
    mensaje_cifrado = [ExpMod(num[0] * 100 + num[1], e, n) for num in bloques]

    print("Mensaje cifrado:", mensaje_cifrado)

def descifrar(C, d, n):
    bloques = [C[i:i+4] for i in range(0, len(C), 4)]
    nums_descifrados = [ExpMod(int(bloque), d, n) for bloque in bloques]

    # Convertir los números descifrados a letras según la codificación dada
    mensaje_descifrado = ''.join([inverso_diccionario[num // 100] + inverso_diccionario[num % 100] for num in nums_descifrados])

    print("Mensaje descifrado:", mensaje_descifrado)

def ExpMod(base, exp, mod):
    return pow(base, exp, mod)

inverso_diccionario = {v: k for k, v in dic3.items()}


