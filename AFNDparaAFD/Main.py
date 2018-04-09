from Automato import Automato
from Tabela import Tabela
import sys

def main():
    if(len(sys.argv) != 2):
        print("Modo de execucao: ")
        print("python Main.py <arquivoEntrada> <arquivoTabela> <arquivoNovoAutomato>")
    else:
        entrada= sys.argv[1]
        # tabela = sys.argv[2]
        # minimizado = sys.argv[3]

        #~ minimizado = sys.argv[3]
        a = Automato(entrada)
        # a.minimiza(tabela, minimizado)
        # print("Arquivo de entrada: " + sys.argv[1])
        # print("Arquivo com a tabela de minimizacao: " + sys.argv[2])
        # print("Arquivo com o automato minimizado: " + sys.argv[3])
        # a.novoAutomato()


        # tabela = Tabela(a)
        # tabela.printTabela()



        for estado in a.estados:
            estado.getAlcancaveis()
            estado.printEstado()
        #~ a.tranformaEmAFD()

main()
