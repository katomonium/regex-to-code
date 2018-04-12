#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from MinimizaAuto.class_auto import Auto


def completa_auto(auto):
    
    for i in auto.estados:
        transisoes = [(x, y, z) for (x, y, z) in auto.trans if x == i]

        presentes = []
        for t in transisoes:

            for letra in auto.alfabeto:
                if letra == t[1]:
                    presentes.append(letra)


        ausentes = [x for x in auto.alfabeto if x not in presentes]
        for letra in ausentes:
            auto.trans.append((i, letra, 'qERRO1'))
    
    a = [(a, b, c) for (a, b, c) in auto.trans if c == 'qERRO1']
    if(not len(a)):
        return
    
    for letra in auto.alfabeto:
        auto.trans.append(('qERRO1', letra, 'qERRO1'))

    auto.estados.append('qERRO1')
