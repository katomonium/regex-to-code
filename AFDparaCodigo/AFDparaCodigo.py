#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from desenhaGrafo.fileHandler import lerAutomato

def AFDparaCodigo():
    entrada = sys.argv[1]
    saida = sys.argv[2]
    automato = lerAutomato(entrada)
    print(automato.inicial)

AFDparaCodigo()