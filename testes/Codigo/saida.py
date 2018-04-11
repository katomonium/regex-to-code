#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def q0(codigo, indice):
    if(indice == len(codigo)):
        return False
    return False

def main(args):
    arquivo = open(args[1], 'r')
    indice = 0
    linhas = arquivo.read().splitlines()
    for lin in linhas:
        print(q0(lin, indice))
main(sys.argv)