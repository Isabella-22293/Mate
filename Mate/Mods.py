from decimal import Decimal, getcontext

getcontext().prec = 500


def ExpMod(base,exp,mod):

    numerador = base**exp
    mod

    resultado = numerador % mod



    print("Resultado del módulo:")
    print(resultado)
    return resultado


