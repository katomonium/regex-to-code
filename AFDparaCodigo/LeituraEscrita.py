#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from AFDparaCodigo.Estado import Estado
from AFDparaCodigo.Transicao import Transicao
# from Automato import Automato


#classe que gerencia arquivo
class Arquivo:
    arq = None
    linhas = None

    def __init__(self, nomeArq, modo):
        self.arq = open(nomeArq, modo)              #Abre o arquivo no modo desejado ('w' - escrita, 'r' - leitura)
        if(modo == 'r'):                            #Se for estado de leitura, le o arquivo dividindo-o por linhas
            self.linhas = self.arq.read().splitlines()

    def leEstados(self):
        estadosRetorno = []
        aux = re.compile("q(\d+)")                  #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        estados = aux.findall(self.linhas[1])       #Procura esse padrao na linha 2 do arquivo, retornando uma lista com os digitos que satisfazem o padrao

        #Cria uma instancia de Estado para cada item da lista
        for i in range(len(estados)):
            novo =  Estado()
            novo.idEstado = estados[i]
            estadosRetorno.append(novo)
        return estadosRetorno


    def leAlfabeto(self): #alfabeto é uma lista
        #simbolos = re.compile("\w")                     #Define simbolos como um padrao que encontra qualquer palavra (nao inclui carateres especiais)
        #alfabeto = simbolos.findall(self.linhas[2])     #Procura esse padrao na linha 3 do arquivo, retornando uma lista que é o alfabeto

        i = 2
        aux = []
        while(i < len(self.linhas[2]) - 2):
            aux.append(self.linhas[2][i])
            i += 1
        aux = ''.join(aux)
        alfabeto = aux.split(",")

        return alfabeto

    def leTransicoes(self, automato):
        self.arq.seek(0)                                #Volta ao inicio do arquivo
        texto = self.arq.read()                         #Le o arquivo completo
        aux = re.compile("q(\d+),(.+)->q(\d+)")         #Define aux como o seguinte padrao "q(\d+),(\w)->q(\d+)",
                                                        #onde (\d+) é um ou mais digitos e (\w) é uma palavra qualquer
        transicoes = aux.findall(texto)                 #Procura em "texto" esse padrao e retorna uma lista de tuplas

        #Para cada tupla da lista "transicoes", cria-se um objeto da classe Transicao e armazena-a no estado de origem
        for item in transicoes:
            i = item[0]
            estadoOrigem = automato.estadosDic[i]

            letra = item[1]

            i = item[2]
            estadoDestino = automato.estadosDic[i]

            transicao = Transicao(estadoOrigem, letra, estadoDestino)

            estadoOrigem.transicoes.append(transicao)

        return

    def leInicial(self):
        ini = re.compile("q(\d+)")                      #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        inicial = ini.findall(self.linhas[-3])          #Encontra esse padrao na antepenultima linha do arquivo
        inicial = inicial[0]
        return inicial

    def leFinais(self):
        fin = re.compile("q(\d+)")                      #Define aux como um padrao de forma que ele é um ou mais digitos apos um caracter "q"
        finais = fin.findall(self.linhas[-2])           #Encontra esse padrao na penultima linha do arquivo
        dicionario = {}                                 #Cria um dicionario para armazenar os estados finais
        for i in range (len(finais)):
            if(not(finais[i] in dicionario)):
                f = finais[i]
                dicionario[f] = f
        return dicionario

    #Formata o texto para escrever no arquivo
    def escreveAFD(self, AFD):
        self.arq.write(AFD.__str__())
