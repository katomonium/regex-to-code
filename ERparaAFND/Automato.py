#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Automato:
    caminhoEscrita = ""
    estados = None
    alfabeto = None
    transicoes = None
    estadoInicial = None
    estadosFinais = None

    def __init__(self, estadoInicial = None, estadosFinais = {}, alfabeto = {}):
        self.alfabeto = alfabeto
        self.estados = {}
        self.transicoes = []
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais
        if(self.estadoInicial != None):
            self.estados[self.estadoInicial] = self.estadoInicial
        
        for key in self.estadosFinais:
            self.estados[key] = key
        
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
        if(self.estadoInicial == None and len(self.estadosFinais) == 0):
            self.estadoInicial = link[acrescentado.estadoInicial]
            for key in acrescentado.estadosFinais:
                self.estadosFinais[link[key]] = link[key]
        return [indice, link]
    
    def getDadosAutomato(self):
        saida = "{\n"
        saida += "q0: " + str(self.estadoInicial) + " qf: " + str(self.estadosFinais) + "\n"
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
        listaEstadosFinais = []
        for key in self.estadosFinais:
            listaEstadosFinais.append(key)
        saida += "\t{"
        for i in range(len(listaEstadosFinais) - 1):
            saida += "q" + str(listaEstadosFinais[i]) + ","
        saida += "q" + str(listaEstadosFinais[len(listaEstadosFinais) - 1]) + "}\n)"
        
        
        
        arquivo = open(self.caminhoEscrita + nomeArq, "w")
        arquivo.write(saida)
        arquivo.close()
        
        