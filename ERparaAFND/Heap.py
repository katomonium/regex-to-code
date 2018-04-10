#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Heap de nós com duas prioridades, sendo o a principal o maior peso e a secundária o menor índice
class Heap:
    elementos = None
        
    def __init__(self):
       self.elementos = []
    
        
    def pai(self, i):
        return ((i - 1)//2)
    def esquerda(self, i):
        return (2 * i + 1)
    def direita(self, i):
        return (2 * i + 2)
    
    # Partindo de i, encontra seu lugar na heap subindo a arvore
    def heapfy(self, i):
        if(len(self.elementos) <= 0):
            return
        if(i == 0):
            return
        maior = self.pai(i)
        if(self.elementos[i].peso > self.elementos[maior].peso or
           (self.elementos[i].peso == self.elementos[maior].peso and
            self.elementos[i].inicio < self.elementos[maior].inicio)):
            # print(self.elementos[i].getDadosNoh() + " > " + self.elementos[maior].getDadosNoh())
            maior = i
        if(i == maior):
            # print(i)
            aux = self.elementos[self.pai(i)]
            self.elementos[self.pai(i)] = self.elementos[i]
            self.elementos[i] = aux
            self.heapfy(self.pai(i))
        
    def insere(self, elemento):
        # print("INSERINDO: " + elemento.getDadosNoh())
        self.elementos.append(elemento)
        self.heapfy(len(self.elementos) - 1)
        
    # Partindo de i, ordena a si e todos seus filhos descendo a arvore
    def corrigeDescendo(self, i):
        if (len(self.elementos) <= 0):
            return
        
        esq = self.esquerda(i)
        dir = self.direita(i)
        maior = i
        if(esq < len(self.elementos) and
           (self.elementos[esq].peso > self.elementos[maior].peso or
           (self.elementos[esq].peso == self.elementos[maior].peso and
            self.elementos[esq].inicio < self.elementos[maior].inicio))):
            maior = esq
        if(dir < len(self.elementos) and
           (self.elementos[dir].peso > self.elementos[maior].peso or
           (self.elementos[dir].peso == self.elementos[maior].peso and
            self.elementos[dir].inicio < self.elementos[maior].inicio))):
            maior = dir
        if(maior != i):
            aux = self.elementos[i]
            self.elementos[i] = self.elementos[maior]
            self.elementos[maior] = aux
            self.corrigeDescendo(maior)
        
    def remove(self):
        topo = self.elementos[0]
        # print("REMOVENDO: " + topo.getDadosNoh())
        self.elementos[0] = self.elementos[len(self.elementos) - 1]
        self.elementos = self.elementos[:-1]
        self.corrigeDescendo(0)
        return topo
    
    def getDadosNohs(self):
        lista = []
        for i in range(len(self.elementos)):
            r = self.remove()
            lista.append(r)
            
        
        for i in range(len(lista)):
            # print("LISTA::")
            # print(lista[i].getDadosNoh())
            self.insere(lista[i]);
        
        saida = "{ \n"
        for i in range(len(lista)):
            saida += lista[i].getDadosNoh()
        saida += "}"
        return saida