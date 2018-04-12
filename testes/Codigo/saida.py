#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "."):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "6"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "b"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "c"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "d"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "e"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "f"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "p"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "q"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "r"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "s"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "t"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "u"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "v"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "w"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "x"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "y"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == "z"):
        indice+=1
        return q0(codigo,indice)
    if(codigo[indice] == " "):
        indice+=1
        return q0(codigo,indice)
    return False


def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().strip().splitlines()
    for lin in linhas:
        print(q0(lin, indice))
        
main(sys.argv)