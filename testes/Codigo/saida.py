#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    if(codigo[indice] == "U"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "W"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "D"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "s"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "M"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "z"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "p"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Z"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "K"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "e"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "c"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "d"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "F"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "$"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "R"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "t"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "r"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "y"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "P"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "G"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "I"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "u"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "_"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "V"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "A"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "C"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "E"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "L"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "O"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Q"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "T"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "X"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "v"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "f"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "N"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "x"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "J"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "q"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "H"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Y"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "w"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "b"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "B"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "S"):
        indice+=1
        return q1(codigo,indice)
    return False

def q1(codigo, indice):
    if(indice == len(codigo)):
        return True
    if(codigo[indice] == "U"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "W"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "D"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "j"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "s"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "M"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "0"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "z"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "l"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "p"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Z"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "K"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "e"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "c"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "d"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "F"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "i"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "$"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "R"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "t"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "r"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "a"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "y"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "P"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "G"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "n"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "I"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "u"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "o"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "1"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "m"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "6"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "_"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "4"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "5"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "V"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "g"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "A"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "C"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "3"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "E"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "9"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "L"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "8"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "7"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "O"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "h"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Q"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "T"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "k"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "X"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "v"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "f"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "N"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "x"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "J"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "q"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "H"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "Y"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "w"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "b"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "B"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "2"):
        indice+=1
        return q1(codigo,indice)
    if(codigo[indice] == "S"):
        indice+=1
        return q1(codigo,indice)
    return False

def preProcessamento(linhas):
    dic = {
        "=" : "=",
        ">" : ">",
        "+" : "+",
        "&" : "&",
        "<" : "<",
        "!" : "!",
        "-" : "-",
        "*" : "*",
        "," : ",",
        "." : ".",
        "[" : "[",
        "{" : "{",
        "(" : "(",
        ")" : ")",
        "}" : "}",
        "]" : "]",
        ";" : ";"
        
    }
    for i in range(len(linhas)):
        nova = []
        j = 0
        while(j < len(linhas[i])):
            if(linhas[i][j] in dic):
                if(j < (len(linhas[i]) - 1) and linhas[i][j + 1] in dic):
                    nova.append(" ")
                    nova.append(linhas[i][j])
                    nova.append(linhas[i][j + 1])
                    nova.append(" ")
                    j += 1
                else:
                    nova.append(" ")
                    nova.append(linhas[i][j])
                    nova.append(" ")
            else:
                nova.append(linhas[i][j])
            j += 1
        linhas[i] = ''.join(nova)
    return linhas

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().strip().splitlines()
    linhas = preProcessamento(linhas)
    print(linhas)
    for lin in linhas:
        lin = lin.strip().split()
        print(lin)
        for item in lin:
            print(q0(item, indice))
        
main(sys.argv)