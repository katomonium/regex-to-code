# -*- coding: UTF-8 -*-
# GRUPO: Arthur Henrique, Pedro Silveira, João Pedro
# MODO DE EXECUCAO:
# python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>
from MinimizacaoAFD.Estruturas import Automato
import sys
def main():
    if(len(sys.argv) != 4):
        print("Modo de execucao: ")
        print("python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>")
    else:
        entrada= sys.argv[1]
        tabela = sys.argv[2]
        minimizado = sys.argv[3]
        
        #~ minimizado = sys.argv[3]
        a = Automato(entrada)
        a.completaAutomato()

        # a.minimiza(tabela, minimizado)
        # print("Arquivo de entrada: " + sys.argv[1])
        # print("Arquivo com a tabela de minimizacao: " + sys.argv[2])
        # print("Arquivo com o automato minimizado: " + sys.argv[3])
        a.novoAutomato()


main()
