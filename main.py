#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from ERparaAFND.ERparaAFND import ERparaAFND
#from desenhaGrafo.desenhaGrafo import desenhaGrafo
from AFNDparaAFD.AFNDparaAFD import AFNDparaAFD
from MinimizaAuto.minimiza_auto import minimiza_auto
from AFDparaCodigo.AFDparaCodigo import AFDparaCodigo
from Minimiza.Minimiza import Minimiza
if __name__ == '__main__':
    ERparaAFND(["testes/ER/" + sys.argv[1], "testes/AFND/arquivos/" + sys.argv[2] + "-AFND"])
    argsDesenha = ["testes/AFND/arquivos/" + sys.argv[2] + "-AFND", "testes/AFND/grafos/" + sys.argv[2] + "-grafo"]
    print("EU THUZA")
    #desenhaGrafo(argsDesenha)
    print("EU DESENHO THUZA")
    argsAFND = ["testes/AFND/arquivos/" + sys.argv[2] + "-AFND", "testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD"]
    AFNDparaAFD(argsAFND)
    print("EU SIL") 
    argsDesenha2 = ["testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD", "testes/AFD/NaoMinimizado/grafos/" + sys.argv[2] + "-grafo"]
    #desenhaGrafo(argsDesenha2)
    print("EU DESENHO SILSIL")
    argsMin = ["testes/AFD/NaoMinimizado/arquivos/" + sys.argv[2] + "-AFD",
              "testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min"]
    Minimiza(argsMin)
    print("EU BRENEX")
    argsDesenha3 = ["testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min", "testes/AFD/Minimizado/grafos/" + sys.argv[2] + "-grafo"]
    #desenhaGrafo(argsDesenha3)
    print("EU DESENHO BRENEX")
    argGeraCodigo = ["testes/AFD/Minimizado/arquivos/" + sys.argv[2] + "-min", "testes/Codigo/" + sys.argv[2] + ".py"]
    AFDparaCodigo(argGeraCodigo)
    print("EU JOBEL")
    
