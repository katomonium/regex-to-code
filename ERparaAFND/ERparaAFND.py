#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from ERparaAFND.ExpressaoRegular import ER


def ERparaAFND(args):
    # Ler uma ER
    er = ER()
    er.lerArquivo(args[0])
    print(er.expressao)
    afnd = er.criarAFND()
    afnd.escreveArquivo(args[1])
    # Gerar um AFND

    # Gerar um AFD
    # Gerar código fonte
