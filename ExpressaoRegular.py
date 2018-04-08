#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Automato import Automato
from Noh import Noh
from Heap import Heap
import copy

class ER:
    simbolosEspeciais = None
    variaveis = None
    expressao = None
    indice = None

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

    # Recebe o nome do arquivo com a expressao regular
    def lerArquivo(self, nomeArquivo):
        arquivo = open(nomeArquivo, 'r')
        linhas = arquivo.read().splitlines()
        self.lerVariaveis(linhas)
        self.lerExpressao(linhas)

    # Le as "variaveis" da expressao
    def lerVariaveis(self, linhas):
        posLinha = 0
        while(posLinha < len(linhas) and "{" not in linhas[posLinha]):
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

    # Le a expressao em si, eliminando espacos inuteis
    def lerExpressao(self, linhas):
        posLinha = 0
        while ("{" not in linhas[posLinha]):
            posLinha += 1

        posLinha += 1
        ex = ""
        while("}" not in linhas[posLinha]):
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
        lista = []
        parenteses = {}
        self.inicializaListas(parenteses)
        self.iniciaEstruturas(lista, parenteses)
        saida = "{ \n"
        for noh in lista:
            saida += "indice : " + str(noh.indice) + " inicio : " + str(noh.inicio) + ", fim : " + str(noh.fim) + " peso : " + str(noh.peso) + "\n"

        print(saida + "}")
        print(parenteses)
        print("---------------")
        fila = self.gerarComponentesSimples(lista, parenteses)
        for elemento in fila:
            aut = elemento[1]
            print(aut.estados)
            print(aut.estadoInicial)
            print(aut.estadoFinal)
            print(aut.transicoes)
            print("*************")

    


    # Inicializa o dicionario de matrizes e gera a heap maxima de nos
    def iniciaEstruturas(self, lista, parenteses):
        peso = 0
        i = 0
        indiceNoh = 0
        h = Heap()
        while(i < len(self.expressao)):
            if(self.expressao[i] == "("):
                peso += 1
                parenteses[peso].append([i, -1])
            elif(self.expressao[i] == ")"):
                pos = self.buscaPrimeiroNone(parenteses, peso)
                parenteses[peso][pos][1] = i
                peso -= 1
            elif(self.expressao[i] != "." and self.expressao[i] != " " and
                 self.expressao[i] != "+" and self.expressao[i] != "*"  and
                 self.expressao[i] != "|"):
                inicio = i
                fim = self.pegaFimPalavra(inicio)
                noh = Noh(indiceNoh, inicio, fim - 1, peso)
                h.insere(noh)
                lista.append(noh)
                indiceNoh += 1
                i = fim - 1
            i += 1
        for i in range(len(lista)):
            lista[i] = h.remove()
        

    def gerarComponentesSimples(self, lista, parenteses):
        fila = []
        self.indice = 1
        for i in range(len(lista)):
            noh = lista[0]
            lista = lista[1:]
            fila.append(self.criarAutomatoSimples(noh))
            self.realizarOperacao(fila[i])
        return fila

    def realizarOperacao(self, item):
        noh = item[0]
        automato = item[1]
        if(not(noh.fim + 1 < len(self.expressao)) or
          (self.expressao[noh.fim + 1] != "+" and self.expressao[noh.fim + 1] != '*')):
            return
        pre = None
        linkAux = None
        if (self.expressao[noh.fim + 1] == "+"):
            pre = Automato()
            self.indice += 2
            temp = pre.acrescentaAutomato(self.indice, automato)
            self.indice = temp[0]
            linkAux = temp[1]
        
        exInicial = automato.estadoInicial
        automato.estadoInicial = self.indice
        automato.estados[automato.estadoInicial] = automato.estadoInicial
        self.indice += 1
        
        exFinal = automato.estadoFinal
        automato.estadoFinal = self.indice
        automato.estados[automato.estadoFinal] = automato.estadoFinal
        self.indice += 1
        
        transicao = (automato.estadoInicial, '', exInicial)
        automato.transicoes.append(transicao)
        
        transicao = (exFinal, '', automato.estadoFinal)
        automato.transicoes.append(transicao)
        
        transicao = (exFinal, '', exInicial)
        automato.transicoes.append(transicao)
        
        transicao = (automato.estadoInicial, '', automato.estadoFinal)
        automato.transicoes.append(transicao)
        if (pre != None):
            temp = automato.acrescentaAutomato(self.indice, pre)
            pre.estadoInicial = linkAux[exInicial]
            pre.estadoFinal = linkAux[exFinal]
            self.indice = temp[0]
            link = temp[1]
            alvos = []
            
            for i in range(len(automato.transicoes)):
                if(automato.transicoes[i][0] == automato.estadoInicial):
                    t = (link[pre.estadoFinal], automato.transicoes[i][1], automato.transicoes[i][2])
                    automato.transicoes.append(t)
                    alvos.append(i)
                elif(automato.transicoes[i][2] == automato.estadoInicial):
                    t = (automato.transicoes[i][0], automato.transicoes[i][1], link[pre.estadoFinal])
                    automato.transicoes.append(t)
                    alvos.append(i)
            
            j = 0
            for i in alvos:
                del automato.transicoes[i - j]
                j += 1
            automato.estados.pop(automato.estadoInicial)
            automato.estadoInicial = link[pre.estadoInicial]
    
    
    def criarAutomatoSimples(self, noh):
        automato = Automato(self.indice, self.indice + 1)
        palavra = self.pegaPalavra(noh.inicio, noh.fim)
        
        transicao = (automato.estadoInicial, palavra, automato.estadoFinal)
        automato.transicoes.append(transicao)
        self.indice += 2
        return [noh, automato]

    # Busca o primeiro parenteses nao balanceado com indice igual ao peso passado por parametro
    def buscaPrimeiroNone(self, parenteses, peso):
        lista = parenteses[peso]
        for i in range(len(lista)):
            if(lista[i][1] == -1):
                return i

    # Descobre a ultima posicao da letra de uma palavra a partir de seu indice de inicio
    def pegaFimPalavra(self, inicio):
        j = inicio
        while(j < len(self.expressao)):
            if(self.expressao[j] == "." or self.expressao[j] == " " or
               self.expressao[j] == "+" or self.expressao[j] == "*"  or
               self.expressao[j] == "|" or self.expressao[j] == "(" or
               self.expressao[j] == ")"):
                return (j)
            j += 1

        return (j)
    
    def pegaPalavra(self, inicio, fim):
        palavra = ""
        for i in range (inicio, fim + 1):
            palavra += self.expressao[i]
        if(palavra in self.variaveis):
            palavra = self.variaveis[palavra]
        return palavra
    def inicializaListas(self, parenteses):
        cont = 0
        pesoMax = 0
        for caractere in self.expressao:
            if(caractere == "("):
                cont += 1
                if(cont > pesoMax):
                    pesoMax = cont
            elif(caractere == ")"):
                cont -= 1
        for i in range(pesoMax + 1):
            parenteses[i] = []
