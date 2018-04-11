#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q00(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "f"):
        indice+=1
        return q02(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q01(codigo,indice)
    return False

def q01(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q12(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "f"):
        indice+=1
        return q06(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q05(codigo,indice)
    return False

def q02(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "f"):
        indice+=1
        return q04(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q03(codigo,indice)
    return False

def q03(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q15(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "r"):
        indice+=1
        return q06(codigo,indice)
    return False

def q04(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "f"):
        indice+=1
        return q04(codigo,indice)
    return False

def q05(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q19(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q07(codigo,indice)
    return False

def q06(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q09(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q16(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q20(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q21(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False

def q29(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "f"):
        indice+=1
        return q13(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q01(codigo,indice)
    return False

def q07(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q22(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "t"):
        indice+=1
        return q08(codigo,indice)
    return False

def q08(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q23(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q10(codigo,indice)
    return False

def q10(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q24(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "n"):
        indice+=1
        return q11(codigo,indice)
    return False

def q11(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q25(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "c"):
        indice+=1
        return q14(codigo,indice)
    return False

def q13(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "o"):
        indice+=1
        return q03(codigo,indice)
    return False

def q14(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q26(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q17(codigo,indice)
    return False

def q17(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q27(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "O"):
        indice+=1
        return q18(codigo,indice)
    return False

def q18(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def q28(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "f"):
        indice+=1
        return q06(codigo,indice)
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    print(00(linhas[0], indice))
