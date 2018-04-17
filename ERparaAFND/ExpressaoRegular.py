#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ERparaAFND.Automato import Automato
from ERparaAFND.Noh import Noh
from ERparaAFND.Heap import Heap


class ER:
    lamb = 'λ'
    simbolosEspeciais = None
    variaveis = None
    expressao = None
    indice = None
    alfabeto = None
    caminho = ""

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
        self.alfabeto = {}
        self.variaveis = {}
        self.expressao = []

    # Recebe o nome do arquivo com a expressao regular
    def lerArquivo(self, nomeArquivo):
        arquivo = open(self.caminho + nomeArquivo, 'r')
        linhas = arquivo.read().splitlines()
        self.leAlfabeto(linhas)
        self.substituiPadroes(linhas)
        self.lerVariaveis(linhas)
        self.lerExpressao(linhas)
        arquivo.close()
        
    
    def leAlfabeto(self, linhas):
        if(linhas[0][0] == ":"):
            alf = linhas[0].split(",")
            alf[0] = alf[0][1:]
            for item in alf:
                self.alfabeto[item.strip()] = item.strip()
        print(self.alfabeto)
        
        novo_alfabeto = {}
        for k in self.alfabeto:
            l = self.alfabeto[k]
            # if len(l) == 6 and l[0] == '[' and l[2] == '.' and l[3] == '.' and l[5] == ']':
            if len(l) == 5 and l[0] == '[' and l[2] == '-' and l[4] == ']':
                ini = ord(l[1])
                fim = ord(l[3])
                # aux = l[1] + ".." + l[3]
                # novo_alfabeto[aux] = l[1] + ".." + l[3]
                for i in range(ini, fim+1):
                    c = chr(i)
                    novo_alfabeto[c] = c
            else:
                novo_alfabeto[l] = l
        
        self.alfabeto = novo_alfabeto
        print(self.alfabeto)
        
        print("----------------------------")
        
    def substituiPadroes(self, linhas):
        posLinha = 0
        while(posLinha < len(linhas)):
            teste = ""
            if(linhas[posLinha] == ""):
                del linhas[posLinha]
                posLinha -= 1
            else:
                for i in range(len(linhas[posLinha])):
                    if(linhas[posLinha][i] != " " and linhas[posLinha][i] != "\t"):
                        teste += linhas[posLinha][i]
                linhas[posLinha] = teste
            posLinha += 1
        posLinha= 0
        
        while(posLinha < len(linhas)):
            novo = []
            i = 0
            while(i < len(linhas[posLinha]) and (linhas[posLinha][i] == "\t" or linhas[posLinha][i] == " ")):
                i += 1
            marca1 = [False, None]
            marca2 = [False, None]
            marca3 = [False, None]
            while(i < len(linhas[posLinha])):
                if(linhas[posLinha][i] == "[" and not marca1[0]):
                    marca1[0] = True
                    marca1[1] = i
                if(marca1[0] and linhas[posLinha][i] == "-" and not marca2[0]):
                    marca2[0] = True
                    marca2[1] = i
                if(marca2[0] and linhas[posLinha][i] == "]" and not marca3[0]):
                    marca3[0] = True
                    marca3[1] = i
                if(marca1[0] and marca2[0] and marca3[0]):
                    novo[marca1[1]] = ""
                    novo[marca2[1]] = "."
                    novo.insert(marca2[1] + 1, '.')
                else:
                    novo.append(linhas[posLinha][i])
                i += 1
            linhas[posLinha] = ''.join(novo)
            print(linhas[posLinha])
            posLinha += 1
        posLinha = 0
        while(linhas[posLinha][0] != "{"):
            posLinha += 1
        posLinha += 1
        while(linhas[posLinha][0] != "}"):
            novo = []
            i = 0
            ultimoTrocou = False
            while((i + 1) < len(linhas[posLinha])):
                if(linhas[posLinha][i] == "'" and linhas[posLinha][i + 1] == "'"):
                    novo.append(self.lamb)
                    i += 1
                    ultimoTrocou = True
                else:
                    novo.append(linhas[posLinha][i])
                    ultimoTrocou = False
                i += 1
            if(not ultimoTrocou):
                novo.append(linhas[posLinha][i])
            linhas[posLinha] = ''.join(novo)
            posLinha += 1


        print("______________________-")
        
    # Le as "variaveis" da expressao
    def lerVariaveis(self, linhas):
        posLinha = 0
        while(posLinha < len(linhas) and "{" != linhas[posLinha][0]):
            linha = linhas[posLinha]
            indice = ""
            posCaractere = 0
            while(posCaractere < len(linha) and linha[posCaractere] != "="):
                indice += linha[posCaractere]
                posCaractere += 1
            posCaractere += 1
            valor = ""
            while (posCaractere < len(linha)):
                valor += linha[posCaractere]
                posCaractere += 1
            if(valor == "''"):
                valor = self.lamb
            self.variaveis[indice] = valor
                    
            posLinha += 1
        print(self.variaveis)
        print("--------------------------------")

    # Le a expressao em si, eliminando espacos inuteis
    def lerExpressao(self, linhas):
        posLinha = 0
        while(linhas[posLinha][0] != "{"):
            posLinha += 1

        posLinha += 1
        ex = ""
        while(linhas[posLinha][0] != "}"):
            ex += linhas[posLinha]
            posLinha += 1
            self.expressao = ex
        print(self.expressao)
        print("_-----------------------_")
        novoExp = self.expressao
        palavra = ""
        for i in range(len(self.expressao)):
            novo = []
            if(self.expressao[i] != "(" and self.expressao[i] != ")" and
              self.expressao[i] != "[" and self.expressao[i] != "]" and
              self.expressao[i] != "." and self.expressao[i] != " " and
              self.expressao[i] != "+" and self.expressao[i] != "*" and
              self.expressao[i] != "|" and self.expressao[i] != "-"):
                palavra += self.expressao[i]
            else:
                if palavra in self.variaveis:
                    # print("variavel: " + palavra)
                    subExp = self.variaveis[palavra]
                    if len(subExp) < 4:
                        novo.append(palavra)
                    else:
                        for j in range(len(subExp)):
                            if(subExp[j - 1] == "." and subExp[j] == "."):
                                inicio = subExp[j - 2]
                                novo.append('(')
                                fim = subExp[j + 1]
                                if(ord(inicio) <= ord(fim)):
                                    while(ord(inicio) <= (ord(fim) - 1)):
                                        novo.append(inicio)
                                        inicio = chr(ord(inicio) + 1)
                                        novo.append("|")
                                    novo.append(fim)
                                    
                                else:
                                    aux = chr(ord(inicio))
                                    inicio = chr(ord(inicio) - 1)
                                    while(ord(inicio) >= ord(fim)):
                                        novo.append(inicio)
                                        inicio = chr(ord(inicio) - 1)
                                        novo.append("|")
                                    novo.append(aux)
                                novo.append(')')
                else:
                    novo.append(palavra)
                        
                novoExp = novoExp.replace(palavra, ''.join(novo))            
                palavra = ''
        
        self.expressao = novoExp
        novo = []
        novo.append("(")
        i = 0
        while (i < len(self.expressao)):
            if (i == 0 and self.expressao[i] == "("):
                novo.append('(')
                novo.append('(')
            elif (i > 0 and self.expressao[i - 1] != "\\" and self.expressao[i] == "("):
                novo.append("(")
                novo.append("(")
            elif (i > 0 and self.expressao[i - 1] != "\\" and self.expressao[i] == ")"):
                novo.append(")")
                novo.append(")")
            elif (i > 0 and self.expressao[i - 1] != "\\" and self.expressao[i] == "|"):
                novo.append(")")
                novo.append("|")
                novo.append("(")
            else:
                novo.append(self.expressao[i])
            i += 1
        novo.append(")")
        self.expressao = (''.join(novo))
        print(self.expressao)
        print("--------------------------")

    def criarAFND(self):
        fila = Heap()
        parenteses = {}
        self.inicializaListas(parenteses)
        self.iniciaEstruturas(fila, parenteses)
        componentes = self.gerarComponentesSimples(fila, parenteses)
        resultado = self.juntarComponentes(fila, componentes, parenteses)
        resultado.alfabeto = self.alfabeto
        return resultado


    # Inicializa o dicionario de matrizes e gera a heap maxima de nos
    def iniciaEstruturas(self, lista, parenteses):
        peso = 0
        i = 0
        indiceNoh = 0
        pilhaParenteses = []
        while(i < len(self.expressao)):
            if(self.expressao[i] == "("):
                peso += 1
                parenteses[peso].append([i, -1])
                pilhaParenteses.append(len(parenteses[peso]) - 1)
            elif(self.expressao[i] == ")"):
                pos = self.buscaPrimeiroNone(parenteses, peso)
                parenteses[peso][pos][1] = i
                peso -= 1
                pilhaParenteses.pop(-1)
            elif(self.expressao[i] != "." and self.expressao[i] != " " and
                 self.expressao[i] != "+" and self.expressao[i] != "*" and
                 self.expressao[i] != "|"):
                inicio = i
                fim = self.pegaFimPalavra(inicio)
                noh = Noh(indiceNoh, inicio, fim - 1, peso, pilhaParenteses)
                lista.insere(noh)
                indiceNoh += 1
                i = fim - 1
            i += 1
        

    def gerarComponentesSimples(self, lista, parenteses):
        fila = {}
        self.indice = 1
        for i in range(len(lista.elementos)):
            noh = lista.remove()
            fila[noh] = self.criarAutomatoSimples(noh)
            self.realizarOperacao(fila[noh], noh)
        for noh in fila:
            lista.insere(noh)
        return fila
    
    
    def juntarComponentes(self, fila, componentes, parenteses):
        while(len(componentes) > 1):
            noh1 = fila.remove()
            noh2 = fila.remove()
            if(noh1.peso > noh2.peso):
                self.verificarParenteses(noh1, componentes)
                fila.insere(noh1)
                fila.insere(noh2)
            elif(noh1.peso > 0):
                if(noh1.pilhaParenteses[-1] == noh2.pilhaParenteses[-1]):
                    self.juntarPar(noh1, noh2, componentes, fila)
                elif(noh1.peso == noh2.peso):
                    self.verificarParenteses(noh1, componentes)
                    fila.insere(noh1)
                    fila.insere(noh2)
            else:
                self.juntarPar(noh1, noh2, componentes, fila)
        for noh in componentes:
            while(noh.inicio > 0 and noh.fim < (len(self.expressao) - 1)):
                self.verificarParenteses(noh, componentes)
            return componentes[noh]
    
    def juntarPar(self, noh1, noh2, componentes, fila):
        if (noh2.inicio - 2 == noh1.fim):
            if (self.expressao[noh1.fim + 1] == "."):
                self.concatena(componentes, noh1, noh2)
                fila.insere(noh1)
                
            elif (self.expressao[noh1.fim + 1] == "|"):
                self.une(componentes, noh1, noh2)
                fila.insere(noh1)
            else:
                fila.insere(noh1)
                fila.insere(noh2)
        else:
            self.verificarParenteses(noh1, componentes)
            fila.insere(noh1)
            fila.insere(noh2)
    
    
    def une(self, componentes, noh1, noh2):
        pre = componentes[noh1]
        automato = componentes[noh2]
        temp = pre.acrescentaAutomato(self.indice, automato)
        self.indice = temp[0]
        link = temp[1]
        
        pre.estados[self.indice] = self.indice
        transicao = (self.indice, self.lamb, pre.estadoInicial)
        pre.transicoes.append(transicao)
        transicao = (self.indice, self.lamb, link[automato.estadoInicial])
        pre.transicoes.append(transicao)
        pre.estadoInicial = self.indice
        self.indice += 1
        
        pre.estados[self.indice] = self.indice
        transicao = (pre.estadoFinal, self.lamb, self.indice)
        pre.transicoes.append(transicao)
        transicao = (link[automato.estadoFinal], self.lamb, self.indice)
        pre.transicoes.append(transicao)
        pre.estadosFinais.pop(pre.estadoFinal)
        # pre.estados.pop(pre.estadoFinal)
        pre.estadoFinal = self.indice
        self.indice += 1
        pre.estadosFinais[pre.estadoFinal] = pre.estadoFinal
        
        noh1.fim = noh2.fim
        componentes.pop(noh2)
    
    def concatena(self, componentes, noh1, noh2):
        pre = componentes[noh1]
        automato = componentes[noh2]
        temp = pre.acrescentaAutomato(self.indice, automato)
        self.indice = temp[0]
        link = temp[1]
        alvos = []
        for i in range(len(pre.transicoes)):
            if(pre.transicoes[i][0] == link[automato.estadoInicial]):
                t = (pre.estadoFinal, pre.transicoes[i][1], pre.transicoes[i][2])
                pre.transicoes.append(t)
                alvos.append(i)
            if(pre.transicoes[i][2] == link[automato.estadoInicial]):
                t = (pre.transicoes[i][0], pre.transicoes[i][1], pre.estadoFinal)
                pre.transicoes.append(t)
                alvos.append(i)
        j = 0
        for i in alvos:
            del pre.transicoes[i - j]
            j += 1
        del pre.estados[link[automato.estadoInicial]]
        pre.estadosFinais.pop(pre.estadoFinal)
        pre.estadoFinal = link[automato.estadoFinal]
        # pre.estados.pop(pre.estadoFinal)
        pre.estadosFinais[pre.estadoFinal] = pre.estadoFinal
        noh1.fim = noh2.fim
        componentes.pop(noh2)
        
    def verificarParenteses(self, noh, componentes):
        noh.fim += 1
        noh.inicio -= 1
        if(noh.fim + 1 < len(self.expressao) and
           (self.expressao[noh.fim + 1] == "+" or self.expressao[noh.fim + 1] == "*")):
            self.realizarOperacao(componentes[noh], noh)
        noh.peso -= 1
        noh.pilhaParenteses.pop(len(noh.pilhaParenteses) - 1)
        

    def realizarOperacao(self, automato, noh):
        if(not(noh.fim + 1 < len(self.expressao)) or
          (self.expressao[noh.fim + 1] != "+" and self.expressao[noh.fim + 1] != '*')):
            return
        pre = None
        linkAux = None
        if (self.expressao[noh.fim + 1] == "+"):
            pre = Automato(None, {}, {})
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
        automato.estadosFinais[automato.estadoFinal] = automato.estadoFinal
        self.indice += 1
        
        transicao = (automato.estadoInicial, self.lamb, exInicial)
        automato.transicoes.append(transicao)
        
        transicao = (exFinal, self.lamb, automato.estadoFinal)
        automato.transicoes.append(transicao)
        
        transicao = (exFinal, self.lamb, exInicial)
        automato.transicoes.append(transicao)
        
        transicao = (automato.estadoInicial, self.lamb, automato.estadoFinal)
        automato.transicoes.append(transicao)
        
        automato.estadosFinais.pop(exFinal)
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
        noh.fim += 1
    
    def criarAutomatoSimples(self, noh):
        automato = Automato(self.indice, {self.indice + 1 : self.indice + 1})
        automato.estadoFinal = self.indice + 1
        palavra = self.pegaPalavra(noh.inicio, noh.fim)
        
        transicao = (automato.estadoInicial, palavra, automato.estadoFinal)
        automato.transicoes.append(transicao)
        self.indice += 2
        return automato

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
