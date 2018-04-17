#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "s"):
        indice+=1
        return q1(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "e"):
        indice+=1
        return q2(codigo,indice)
    return False

def q2(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "n"):
        indice+=1
        return q3(codigo,indice)
    return False

def q3(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q4(codigo,indice)
    return False

def q4(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "o"):
        indice+=1
        return q5(codigo,indice)
    return False

def q5(codigo, indice):
    if(indice == len(codigo)):
        return True
    return False


def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().strip().splitlines()
    for lin in linhas:
        print(q0(lin, indice))
        
main(sys.argv)