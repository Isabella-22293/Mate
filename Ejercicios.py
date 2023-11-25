#Derek Arreaga 22537
#Isabella Miralles 22293
#Diccionario de A  a Z

#Sistema RSA

#Elegir la codificación con diccionario
dic1={
     " ":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
     "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,
     "S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26, "0":27,
     "1":28,"2":29,"3":30,"4":31,"5":32,"6":33,"7":34,"8":35,"9":36
     }

#Diccionario de A  a Z
dic2={
    "A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,
    "L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,
    "U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25
}

#Diccionario de A-Z
dic3={
    "A":"00","B":"01","C":"02","D":"03","E":"04","F":"05","G":"06","H":"07","I":"08","J":"09","K":"10",
    "L":"11","M":"12","N":"13","O":"14","P":"15","Q":"16","R":"17","S":"18","T":"19",
    "U":"20","V":"21","W":"22","X":"23","Y":"24","Z":"25"
}

from decimal import Decimal, getcontext

getcontext().prec = 500

#Decimal
def ExpMod(base,exp,mod):

    numerador = base**exp
    mod

    resultado = numerador % mod



    print("Resultado del módulo:")
    print(resultado)
    return resultado


#Calculos
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

#Menu
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
    mensaje_cifrado = [ExpMod(num[0] * 100 + num[1], e, n) for num in bloques if len(num) >= 2]


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
    return pow(int(base), int(exp), int(mod))

inverso_diccionario = {v: k for k, v in dic3.items()}

menuP()