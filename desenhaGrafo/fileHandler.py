#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


class Automato:
    def __init__(self, es, al, tr, ei, ef):
        self.estados = es
        self.alfabeto = al
        self.transicoes = tr
        self.inicial = ei
        self.finais = ef

    def __str__(self):
        s = "(\n"

        s += "\t{"
        for i in self.estados:
                s += "{},".format(i)

        s = s[:-1]
        s += "},\n"

        s += "\t{"
        for i in self.alfabeto:
                s += "{},".format(i)

        s = s[:-1]
        s += "},\n\t{\n"
        for i in self.transicoes:
                s += "\t\t({},{}->{}),\n".format(i[0], i[1], i[2])

        s = s[:-2]
        s += "\n\t},\n"
        s += "\t{},\n".format(self.inicial)

        s += "\t{"
        for i in self.finais:
                s += "{},".format(i)

        s = s[:-1]
        s += "}\n)"

        return s


caminhoAFND = ""


def lerAutomato(arquivo):
    linhas = open(caminhoAFND + arquivo, 'r').read().splitlines()

    e = re.compile('(\w+\d+|\w+)')
    estados = e.findall(linhas[1])

    a = re.compile('\w')
    alfabeto = a.findall(linhas[2])

    estadosFinais = e.findall(linhas[-2])

    estadoInicial = e.findall(linhas[-3])[0]

    d = re.compile('(\w+\d+|\w+),(.*)->(\w+\d+|\w+)')
    transicoes = []
    for i in linhas:
        transicoes += d.findall(i)
    

    return Automato(
            estados, alfabeto, transicoes, estadoInicial, estadosFinais
    )
