# -*- coding: UTF-8 -*-
# GRUPO: Arthur Henrique, Pedro Silveira, João Pedro
# MODO DE EXECUCAO:
# python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>
from MinimizaicaoAFD.Estruturas import Automato
from MinimizaicaoAFD.LeituraEscrita import Arquivo
import sys
def Minimiza(args):
        entrada= args[1]
        saida = args[2]
        
        # minimizado = sys.argv[3]
        
        a = Automato(entrada)
        le = Arquivo(saida + "1", "w")
        le.imprimeAut(a)
        print("AQUI")
        # a.novoAutomato()
        tab = "tabela.txt"
        a.minimiza(tab, saida)
        le.imprimeAut(a.novoAutomato())
        # print("Arquivo de entrada: " + sys.argv[1])
        # print("Arquivo com a tabela de minimizacao: " + sys.argv[2])
        # le.escreveMinimizado(a)
        
        
        

Minimiza(sys.argv)
