#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from ERparaAFND.ERparaAFND import ERparaAFND
from desenhaGrafo.desenhaGrafo import desenhaGrafo
from AFNDparaAFD.AFNDparaAFD import AFNDparaAFD

if __name__ == '__main__':
    print("Hello")

    ERparaAFND(["testes/ER/" + sys.argv[1], "testes/AFND/arquivos/" + sys.argv[2]])
    argsDesenha = ["testes/AFND/arquivos/" + sys.argv[2], "testes/AFND/grafos/" + sys.argv[2] + "-grafo"]
    desenhaGrafo(argsDesenha)

    argsAFND = ["testes/AFND/arquivos/" + sys.argv[2], "testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-AFD"]
    AFNDparaAFD(argsAFND)
    
    argsDesenha2 = ["testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-AFD", "testes/AFD/Minimizado/grafos/" + sys.argv[2] + "-grafo"]
    desenhaGrafo(argsDesenha2)

