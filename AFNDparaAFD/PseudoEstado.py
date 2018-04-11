#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AFNDparaAFD.Transicao import Transicao


class PseudoEstado:
    estados = None
    verificado = None
    transicoes = None
    transicaoReal = None
    idPE = None
    final = None

    def __init__(self):
        self.estados = []
        self.verificado = False
        self.transicoes = []
        self.transicaoReal = []
        self.idPE = "null"
        self.final = False
    

    def setTransicoes(self):
        for estado in self.estados:
            for transicao in estado.transicoes:
                self.transicoes.append(transicao)
    
    def setEstados(self,estados):
        self.estados = estados
        for estado in estados:
            if(estado.final == True):
                self.final = True
                return
        return

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
                s += "q{}".format(transicao.origem.idPE)
                s += "--"
                s += transicao.letra + "->"
                s += "q{}".format(transicao.destino.idPE)
                s += "\n"

        # for transicao in self.transicoes:
        #     s += transicao.origem.idEstado + "--" + transicao.letra + "->" + transicao.destino.idEstado + "\n"
        # s += "\n"
        print(s)
