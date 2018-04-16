#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
from class_auto import Auto


def junta_transicoes(trans):
    t = []

    for i in trans:
        li = [(a, b, c) for (a, b, c) in t if i[0] == a and i[2] == c]

        if not len(li):
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

    nao_finais = [x for x in auto.estados if x not in auto.finais]

    s += '\tnode [shape=circle]\n'
    for i in nao_finais:
        s += '\t{}\n'.format(i)

    s += '\tstart -> {}\n'.format(auto.inicial)

    for i in junta_transicoes(auto.trans):
        s += '\t{} -> {} [label="{}"]\n'.format(i[0], i[2], i[1])

    s += '}'
    return s


def minimiza_auto(args):
    # Criar automato apartir do arquivo
    auto = Auto(args[0])
    auto.minimiza()
    print(auto, file = open(args[1], "w"))

