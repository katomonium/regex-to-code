#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q1(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "a"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q1(codigo,indice)
    return False

def q2(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q2(codigo,indice)
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    for lin in linhas:
        print(q0(lin, indice))

main(sys.argv)