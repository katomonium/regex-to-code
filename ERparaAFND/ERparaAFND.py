#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from ERparaAFND.ExpressaoRegular import ER


def ERparaAFND(args):
    if(len(args) != 3):
        print("Modo de uso")
        print("./{} <arquivo-entrada> <arquivo-saida>".format(args[0], ))
        sys.exit(1)

    # Ler uma ER
    er = ER()
    er.lerArquivo(args[1])
    print(er.expressao)
    afnd = er.criarAFND()
    print(afnd.getDadosAutomato())
    afnd.escreveArquivo(args[2])
    # Gerar um AFND

    # Gerar um AFD
    # Gerar código fonte
