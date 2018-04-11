#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from ERparaAFND.ERparaAFND import ERparaAFND
from desenhaGrafo.desenhaGrafo import desenhaGrafo
from AFNDparaAFD.AFNDparaAFD import AFNDparaAFD
from MinimizaAuto.minimiza_auto import minimiza_auto
from AFDparaCodigo.AFDparaCodigo import AFDparaCodigo

if __name__ == '__main__':
    print("Hello")

    ERparaAFND(["testes/ER/" + sys.argv[1], "testes/AFND/arquivos/" + sys.argv[2] + "-AFND"])
    argsDesenha = ["testes/AFND/arquivos/" + sys.argv[2] + "-AFND", "testes/AFND/grafos/" + sys.argv[2] + "-grafo"]
    desenhaGrafo(argsDesenha)

    argsAFND = ["testes/AFND/arquivos/" + sys.argv[2] + "-AFND", "testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD"]
    AFNDparaAFD(argsAFND)

    argsDesenha2 = ["testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD", "testes/AFD/NaoMinimizado/grafos/" + sys.argv[2] + "-grafo"]
    desenhaGrafo(argsDesenha2)

    argsMin = ["testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD",
               "testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min"]
    minimiza_auto(argsMin)
    argsDesenha3 = ["testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min", "testes/AFD/Minimizado/grafos/" + sys.argv[2] + "-grafo"]
    desenhaGrafo(argsDesenha3)
    
    argGeraCodigo = ["testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min", "testes/Codigo/" + sys.argv[2] + ".py"]
    AFDparaCodigo(argGeraCodigo)

    
