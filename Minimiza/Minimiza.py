#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Minimiza.Estruturas import Automato
import sys

def Minimiza(args):
    #~ if(len(sys.argv) != 4):
        #~ print("Modo de execucao: ")
        #~ print("python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>")
    #~ else:
    entrada= args[0]
    tabela = "FODACE"
    minimizado = args[1]
    
    #~ minimizado = sys.argv[3]
    a = Automato(entrada)
    a.minimiza(tabela, minimizado)
    print("Arquivo de entrada: " + entrada)
    print("Arquivo com a tabela de minimizacao: " + minimizado)
    #~ print("Arquivo com o automato minimizado: " + sys.argv[3])
    a.novoAutomato()

