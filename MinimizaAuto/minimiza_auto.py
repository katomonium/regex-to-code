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

    fl = open(args[1], 'w')
    fl.write(novo_auto.__str__())

    # print(gen_dot(novo_auto))

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