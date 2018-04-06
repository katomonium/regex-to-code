#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Automato import Automato

class ER:
    simbolosEspeciais = None
    variaveis = None
    expressao = None

    def __init__(self):
        self.simbolosEspeciais = {
            "*" : "*",
            "+" : "+",
            "|" : "|",
            "(" : "(",
            ")" : ")",
            "[" : "[",
            "]" : "]",
            "-" : "-",
            "." : "."
        }

        self.variaveis = {}
        self.expressao = []

    #recebe o nome do arquivo com a expressao regular
    def lerArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        linhas = arquivo.read().splitlines()
        self.lerVariaveis(linhas)
        self.lerExpressao(linhas)

    #le as "variaveis" da expressao
    def lerVariaveis(self, linhas):
        posLinha = 0
        while(linhas[posLinha] != "{"):
            linha = linhas[posLinha]
            indice = ""
            posCaractere = 0
            while(posCaractere < len(linha) and linha[posCaractere] != " "):
                indice += linha[posCaractere]
                posCaractere += 1

            while(posCaractere < len(linha) and linha[posCaractere] == " "):
                posCaractere += 1

            posCaractere += 1
            while (posCaractere < len(linha) and linha[posCaractere] == " "):
                posCaractere += 1

            valor = ""
            while (posCaractere < len(linha)):
                valor += linha[posCaractere]
                posCaractere += 1
            self.variaveis[indice] = valor

            posLinha += 1

    #le a expressao em si, eliminando espacos inuteis
    def lerExpressao(self, linhas):
        posLinha = 0
        while (linhas[posLinha] != "{"):
            posLinha += 1

        posLinha += 1
        ex = ""
        while(linhas[posLinha] != "}"):
            i = 0
            while(linhas[posLinha][i] == " " or linhas[posLinha][i] == "\t"):
                i += 1
            cont = 0
            while (i < len(linhas[posLinha])):
                if (linhas[posLinha][i] == "\t"):
                    l = list(linhas[posLinha])
                    l[i] = ' '
                    linhas[posLinha] = ''.join(l)
                if(linhas[posLinha][i] != " " and linhas[posLinha][i] != "\t"):
                    cont = 0
                else:
                    cont += 1
                if(cont < 2):
                    ex += linhas[posLinha][i]
                i += 1
            if(linhas[posLinha + 1] != "}"):
                ex += " "
            posLinha += 1
            self.expressao = ex



    def criarAFND(self):
        #for i in range(len(self.expressao)):
            #self.expressao[i] = self.expressao.split(".")
        afnd = Automato(0)