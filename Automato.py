#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Automato:
    estados = None
    alfabeto = None
    transicoes = None
    estadoInicial = None
    estadoFinal = None

    def __init__(self, estadoInicial, estadoFinal):
        self.estados = {}
        self.alfabeto = {}
        self.transicoes = []
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal
        self.estados[self.estadoInicial] = self.estadoInicial