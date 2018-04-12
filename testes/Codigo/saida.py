#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q00(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "g"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q01(codigo,indice)
    return False

def q01(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q02(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q03(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q04(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q05(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q06(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q07(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q08(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q09(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q10(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q11(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q12(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q13(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q14(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q15(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q16(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q17(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q18(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "g"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q01(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q01(codigo,indice)
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    for lin in linhas:
        print(q00(lin, indice))
main(sys.argv)