#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import graphviz

caminhoAFNDGrafo = ""


def drawing(auto, filename):
    g = graphviz.Digraph('graph', filename=caminhoAFNDGrafo + filename)
    g.attr(rankdir='LR')

    g.attr('node', shape='point')
    g.node('start')

    g.attr('node', shape='doublecircle')
    for i in auto.finais:
        g.node(i)

    g.attr('node', shape='circle')
    a = [i for i in auto.estados if i not in auto.finais]
    for i in a:
        if(i != 'qERRO'):
            g.node(i)

    g.edge('start', auto.inicial)

    t = juntaTransicoes(auto.transicoes)
    for i in t:
        if(i[0] != 'qERRO' and i[2] != 'qERRO'):
            g.edge(i[0], i[2], i[1])

    g.format = 'png'
    g.render()


def juntaTransicoes(trans):
    t = []
    for i in trans:
        li = [(a, b, c) for (a, b, c) in t if i[0] == a and i[2] == c]

        if(not len(li)):
            t.append(i)

        else:
            for j in li:
                _j = list(t[t.index(j)])
                _j[1] = t[t.index(j)][1] + ", " + i[1]
                t[t.index(j)] = tuple(_j)

    return t
