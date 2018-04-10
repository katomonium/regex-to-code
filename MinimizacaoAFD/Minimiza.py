# -*- coding: UTF-8 -*-
# GRUPO: Arthur Henrique, Pedro Silveira, João Pedro
# MODO DE EXECUCAO:
# python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>
from MinimizacaoAFD.Estruturas import Automato
from MinimizacaoAFD.LeituraEscrita import Arquivo
import sys
def Minimiza(args):
        entrada= args[0]
        saida = args[1]
        
        #~ minimizado = sys.argv[3]
        
        a = Automato(entrada)
        a.completaAutomato()
        le = Arquivo(saida + "1", "w")
        le.imprimeAut(a)
        a.novoAutomato()
        # tab = "testes/AFD/Minimizado/tabela.txt"
        a.minimiza(tab, saida)
        # print("Arquivo de entrada: " + sys.argv[1])
        # print("Arquivo com a tabela de minimizacao: " + sys.argv[2])
        le.escreveMinimizado(a)
        
        
        

