#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AFNDparaAFD.PseudoEstado import PseudoEstado

class AutomatoFD:
    PErestantes = []
    pseudoEstados = []                  #lista de estados do automato
    estadosDic = {}               #dicionario que referencia os estados
    alfabeto = []
    inicial = None
    finais = []                   #dicionario de estados finais


    def __str__(self):
        s = "(\n"

        s += "\t{"
        for i in self.pseudoEstados:
            s += "q{},".format(i.idPE)

        s = s[:-1]
        s += "},\n"

        s += "\t{"
        for i in self.alfabeto:
                s += "{},".format(i)

        s = s[:-1]
        s += "},\n\t{\n"
        
        for estado in self.pseudoEstados:
            for transicao in estado.transicaoReal:
                s += "\t\t(q{},{}->q{}),\n".format(transicao.origem.idPE, transicao.letra, transicao.destino.idPE)

        s = s[:-2]
        s += "\n\t},\n"
        s += "\tq{},\n".format(self.inicial.idPE)

        s += "\t{"
        for PE in self.pseudoEstados:
            if(PE.final == True):
                s += "q{},".format(PE.idPE)

        s = s[:-1]
        s += "}\n)"
        return s

    def renomearEstados(self):
        i = 0
        for PE in self.pseudoEstados:
            PE.idPE = i
            i += 1

    def acabou(self):
        for estado in self.pseudoEstados:
            if(estado.verificado == False):
                return False
        return True

    def adicionaPE(self,PE):
        if(PE not in self.pseudoEstados):
            self.pseudoEstados.append(PE)
            self.PErestantes.append(PE)

    def estadoJaExiste(self,estados):
        for PE in self.pseudoEstados:
            if(len(PE.estados) == len(estados)):
                if all(PE.contem(estado) for estado in estados):
                    return PE
        return None
    
    def fundirEstadosSeNaoForamFundidos(self,estados):
        if(len(estados) == 0):
            return None
        pseudoEstado = self.estadoJaExiste(estados)
        if(pseudoEstado is not None):
            return pseudoEstado
        else:
            pseudoEstado = PseudoEstado()
            pseudoEstado.setEstados(estados)
            pseudoEstado.setTransicoes()
            return pseudoEstado
