#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def e3(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == 'a'):
        indice+=1
        return e1(codigo,indice)
    if(codigo[indice] == 'b'):
        indice+=1
        return e2(codigo,indice)
    return False

def e2(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == 'b'):
        indice+=1
        return e2(codigo,indice)
    if(codigo[indice] == 'a'):
        indice+=1
        return e1(codigo,indice)
    return False

def e1(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == 'b'):
        indice+=1
        return e3(codigo,indice)
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    print(e1(linhas[0], indice))
main(sys.argv)
