#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from MinimizaAuto.class_auto import *
from MinimizaAuto.functions import *
from MinimizaAuto.completa_auto import *


def minimiza_auto(args):
    auto = Auto(args[0])
    completa_auto(auto)

    tabela = CriarTabela(auto)
    AcharDisj(auto, tabela)
    novo_auto = JuntaEstados(auto, tabela)
    
    renomeia_estados(novo_auto)

    fl = open(args[1], 'w')
    fl.write(novo_auto.__str__())


def renomeia_estados(auto):
    count = 0
    novos_estados = {}
    
    i = 0
    while (i < len(auto.estados)):
        if(auto.estados[i] != "qERRO1"):
            f = 'q{}'.format(count)
            novos_estados[auto.estados[i]] = f
            auto.estados[i] = f
            count += 1
        else:
            auto.estados.pop(i)
            i -= 1
        i += 1
    
    i = 0
    while(i < len(auto.trans)):
        t = list(auto.trans[i])
        if(t[0] != "qERRO1" and t[2] != "qERRO1"):
            t[0] = novos_estados[t[0]]
            t[2] = novos_estados[t[2]]
            
            auto.trans[i] = tuple(t)
        else:
            auto.trans.pop(i)
            i -= 1
        i += 1

    for i in range(len(auto.finais)):
        auto.finais[i] = novos_estados[auto.finais[i]]
        
    auto.inicial = novos_estados[auto.inicial]


def junta_transicoes(trans):
    t = []

    for i in trans:
        li = [(a, b, c) for (a, b, c) in t if i[0] == a and i[2] == c]

        if not len(li) :
            t.append(i)

        else:
            for j in li:
                _j = list(t[t.index(j)])
                _j[1] = t[t.index(j)][1] + ' ' + i[1]
                t[t.index(j)] = tuple(_j)

    return t

def gen_dot(auto):
    s = "digraph \"graph\" {\n\trankdir=LR\n\tnode [shape=point]\n\tstart\n"

    s += "\tnode [shape=doublecircle]\n"
    for i in auto.finais:
        s += '\t{}\n'.format(i)

    l = [x for x in auto.estados if x not in auto.finais]

    s += '\tnode [shape=circle]\n'
    for i in l:
        s += '\t{}\n'.format(i)

    s += '\tstart -> {}\n'.format(auto.inicial)

    for i in junta_transicoes(auto.trans):
        s += '\t{} -> {} [label="{}"]\n'.format(i[0], i[2], i[1])

    s += '}'
    return s