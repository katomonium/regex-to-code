from Transicao import Transicao

class PseudoEstado:
    estados = None
    verificado = None
    transicoes = None
    transicaoReal = None

    def __init__(self):
        self.estados = []
        self.verificado = False
        self.transicoes = []
        self.transicaoReal = []


    def setTransicoes(self):
        for estado in self.estados:
            for transicao in estado.transicoes:
                self.transicoes.append(transicao)

    def criarTransicaoReal(self, letra, destino):
        t = Transicao(self, letra, destino)
        self.transicaoReal.append(t)

    def contem(self, estado):
        for e in self.estados:
            if(e == estado):
                return True

    def printPE(self):
        s = "\nID do pseudoEstado: \n"
        for estado in self.estados:
            s += "q" + estado.idEstado

        s += "\nTransições: \n"
        if(self.transicaoReal is not None):
            for transicao in self.transicaoReal:
                for estado in transicao.origem.estados:
                    s += "q" + estado.idEstado
                s += "--"
                s += transicao.letra + "->"
                for estado in transicao.destino.estados:
                    s += "q" + estado.idEstado
                s += "\n"

        # for transicao in self.transicoes:
        #     s += transicao.origem.idEstado + "--" + transicao.letra + "->" + transicao.destino.idEstado + "\n"
        # s += "\n"
        print(s)
