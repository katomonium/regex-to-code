#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
            "-" : "-"
        }

        self.variaveis = {}
        self.expressao = ""

    def lerArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        linhas = arquivo.read().splitlines()
        self.lerVariaveis(linhas)
        self.lerExpressao(linhas)


    def lerVariaveis(self, linhas):
        posLinha = 0
        while(linhas[posLinha] != "{"):
            linha = linhas[posLinha]
            indice = ""

            posCaractere = 0
            while(linha[posCaractere] != " "):
                indice += linha[posCaractere]
                posCaractere += 1

            while(linha[posCaractere] == " "):
                posCaractere += 1

            posCaractere += 1
            while (linha[posCaractere] == " "):
                posCaractere += 1

            valor = ""
            while (posCaractere < len(linha)):
                valor += linha[posCaractere]
                posCaractere += 1
            self.variaveis[indice] = valor

            posLinha += 1

    def lerExpressao(self, linhas):
        posLinha = 0
        while (linhas[posLinha] != "{"):
            posLinha += 1

        posLinha += 1

        while(linhas[posLinha] != "}"):
            i = 0
            while(linhas[posLinha][i] == " " or linhas[posLinha][i] == "\t"):
                i += 1
            cont = 0
            while (i < len(linhas[posLinha])):
                if(linhas[posLinha][i] != " " and linhas[posLinha][i] != "\t"):
                    cont = 0
                else:
                    cont += 1
                if(cont < 2):
                    self.expressao += linhas[posLinha][i]
                i += 1
            posLinha += 1

        print(self.variaveis)
        print(self.expressao)

