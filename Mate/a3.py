
import random
from Mods import *
from Dic import *
from Calculos import *

#Generacion de claves
#Para la generación de clave, hay 3 opciones, ingresar manualmente, con datos predeterminados o datos randoms

listaNums = []

#menu
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
            print(2)
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
            print(2)
        case "3":
            print(3)
        case "4":
            menuP()


def menuDec():
    print("")

#FUNCIONES POR OPCIONES
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

def cifrar(M,e,n,phi):
    llave_publica = (e, n)
    print ("La llave publica es ", llave_publica)
    #Diccionario de A a Z mod 26
    dicDef = getDic()
    #Se creara un arreglo para almacenar los valores del mensaje cifrado
    listaNums = []
    
    #Guarda la cadena entera en un arreglo
    for i in range(len(M)):
        #Se guarda el valor de la primera letra
        result = dicDef[M[i].upper()]
        #Se llama a la función con el resultado como parámetro
        agregarDigitos(M[i].upper(),result)
        

    if (len(listaNums))%2 != 0:
        numRandom = random.randint(0, 25)
        agregarDigitos("letra extra",numRandom)

    #Encriptación
    print (listaNums)
    #Ahora se guarda en otra lista pero se separan por parejas
    cant = len(listaNums)

    cadena_cifrada = []
    for i in range(0,cant,2):
        #Se suman las posiciones de los numeros
        cadena_cifrada.append(listaNums[i] + listaNums[i+1])
        pass

    print("Ahora los dígitos juntos: ",cadena_cifrada)

    #Elevar cada elemento al módulo:
    resultado=[]
    for i in range(len(cadena_cifrada)):
        resul = ExpMod(int(cadena_cifrada[i]),e,n)
        if len(str(resul)) == 2:
            resul = "00"+str(resul)
        elif len(str(resul))==3:
            resul = "0"+str(resul)
        resultado.append(str(resul))

    print ("Resultado final: ",str(resultado))



#PREDETERMINADOS
#p = 53
#q = 67

lista_primos = PrimosAlAzar(2, 250)

#p = lista_primos[random.randint(0, (len(lista_primos)-1))]
#q = lista_primos[random.randint(0, (len(lista_primos)-1))]


#Ahora se brinda una palabra por encriptar
#palabra = input("Palabra a encriptar: ")
M = "VIVAMIXCO"
#Encriptado RSA

#Se creara un arreglo para almacenar los valores del mensaje cifrado


#Funcion que toma el numero de la letra y lo agrega a la lista
def agregarDigitos(letra, num):
    if int(num)<10:
        listaNums.append("0"+str(num))
        print(letra + ": 0" + str(num))
    else:
        #Ya tiene dos dígitos, solo guarda el numero normal en el mismo slot
        listaNums.append(str(num))
        print(letra + ": " + str(num))



#EXE
menuP()


        


