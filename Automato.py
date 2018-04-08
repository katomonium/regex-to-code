#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Automato:
    estados = None
    alfabeto = None
    transicoes = None
    estadoInicial = None
    estadoFinal = None

    def __init__(self, estadoInicial = None, estadoFinal = None, alfabeto = {}):
        self.alfabeto = alfabeto
        self.estados = {}
        self.alfabeto = {}
        self.transicoes = []
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        if(self.estadoInicial != None):
            self.estados[self.estadoInicial] = self.estadoInicial
        if(self.estadoFinal != None):
            self.estados[self.estadoFinal] = self.estadoFinal
        
    def acrescentaAutomato(self, indice, acrescentado):
        link = {}
        for estado in acrescentado.estados:
            link[estado] = indice
            self.estados[indice] = indice
            indice += 1
        for transicao in acrescentado.transicoes:
            for estado in acrescentado.estados:
                if(estado == transicao[0]):
                    t = (link[estado], transicao[1], link[transicao[2]])
                    self.transicoes.append(t)
        if(self.estadoInicial == None and self.estadoFinal == None):
            self.estadoInicial = link[acrescentado.estadoInicial]
            self.estadoFinal = link[acrescentado.estadoFinal]
        return [indice, link]
    
    def getDadosAutomato(self):
        saida = "{\n"
        saida += "q0: " + str(self.estadoInicial) + " qf: " + str(self.estadoFinal) + "\n"
        for estado in self.estados:
            saida += str(estado) + " - "
        
        saida += "\n"
        saida += "Transicoes:\n  [\n"
        for t in self.transicoes:
            saida += "    " + str(t) + "\n"
        saida += "  ]\n}\n"
        return saida
        
    def escreveArquivo(self, nomeArq):
        saida = "(\n\t"
        
        listaEstados = []
        for key in self.estados:
            listaEstados.append(key)
        
        saida += "{"
        for i in range(len(listaEstados) - 1):
            saida += "q" + str(listaEstados[i]) + ","
        
        saida += "q" + str(listaEstados[len(listaEstados) - 1])
        saida += "},\n"
        
        listaAlfabeto = []
        for key in self.alfabeto:
            listaAlfabeto.append(key)
        
        saida += "\t{"
        for i in range(len(listaAlfabeto) - 1):
            saida += listaAlfabeto[i] + ","
        
        if(len(self.alfabeto) > 0):
            saida += listaAlfabeto[len(listaAlfabeto) - 1]
        saida += "},\n"
        saida += "\t{\n\t\t"
        for i in range(len(self.transicoes) - 1):
            t = self.transicoes[i]
            if(t[1] == ''):
                aux = "''"
            else:
                aux = t[1]
            saida += "(q" + str(t[0]) + "," + \
                     aux + "->" + "q" + str(t[2]) + "),\n\t\t"

        t = self.transicoes[len(self.transicoes) - 1]
        if (t[1] == ''):
            aux = "''"
        else:
            aux = t[1]
        saida += "(q" + str(t[0]) + "," + \
                 aux + "->" + "q" + str(t[2]) + ")\n\t},\n"
        
        saida += "\tq" + str(self.estadoInicial) + ",\n"
        saida += "\t{q" + str(self.estadoFinal) + "}\n)"
        
        
        
        arquivo = open(nomeArq, "w")
        arquivo.write(saida)
        arquivo.close()
        
        