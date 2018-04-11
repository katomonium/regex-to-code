#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class Auto:
    def __init__(self, arq):
        arquivo = open(arq, "r")
        linhas = arquivo.read().strip().splitlines()

        # Achar estados
        # O estados tem que conter pelo menos uma letra seguido por pelo menos um digito
        e = re.compile('\w+\d+')
        # Achando os estados no padrão do RegEx
        self.estados = e.findall(linhas[1])

        a = linhas[2].strip()[1:][:-2]
        self.alfabeto = a.split(',')
        if 'λ' in self.alfabeto:
            self.alfabeto.remove('λ')

        # Achar os estados finais
        self.finais = e.findall(linhas[-2])

        # Achar o estado inicial
        self.inicial = e.findall(linhas[-3])[0]

        # Achar as funções de transição
        d = re.compile('(\w+\d+),(.+)->(\w+\d+)')
        self.trans = []
        for i in linhas:
            self.trans += (d.findall(i))

        self.corrige_estados()


    def corrige_estados(self):
        m = ''
        for e in self.estados:
            if len(e) > len(m):
                m = e

        m = len(m)-1
        n_estados = []
        for e in self.estados:
            e_ = e[1:]

            if len(e_) < m:
                while len(e_) < m:
                    e_ = '0{}'.format(e_)

                e_ = 'q{}'.format(e_)
                n_estados.append(e_)

                for i in range(len(self.trans)):
                    if self.trans[i][0] == e:
                        t_ = list(self.trans[i])
                        t_[0] = e_
                        self.trans[i] = tuple(t_)

                for i in range(len(self.trans)):
                    if self.trans[i][2] == e:
                        t_ = list(self.trans[i])
                        t_[2] = e_
                        self.trans[i] = tuple(t_)

                if self.inicial == e:
                    self.inicial = e_

                for i in range(len(self.finais)):
                    if self.finais[i] == e:
                        self.finais[i] = e_

            else:
                n_estados.append(e)

        self.estados = n_estados


    def __str__(self):
        # Essa função faz mágica, não mexa

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
        for i in self.trans:
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
