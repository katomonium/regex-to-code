#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "0"):
        indice+=1
        return q2(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q1(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "0"):
        indice+=1
        return q3(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q3(codigo,indice)
    return False

def q2(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "a"):
        indice+=1
        return q3(codigo,indice)
    return False

def q3(codigo, indice):
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