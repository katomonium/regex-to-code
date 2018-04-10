from AFNDparaAFD.Automato import Automato
from AFNDparaAFD.LeituraEscrita import Arquivo


def AFNDparaAFD(args):
        entrada = args[0]

        a = Automato(entrada)

        for i in a.finais:
            print(i)

        for estado in a.estados:
            a.getAlcancaveis(estado)
            estado.printEstado()
        AFD = a.tranformaEmAFD()
        
        nomeArq = args[1]
        arquivo = Arquivo(nomeArq, "w")
        arquivo.escreveAFD(AFD)
        
        print(AFD)

