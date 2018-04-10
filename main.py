#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from ERparaAFND.ERparaAFND import ERparaAFND
from desenhaGrafo.desenhaGrafo import drawing

if __name__ == '__main__':
    print("Hello")

    ERparaAFND(sys.argv)
    argsDesenha = [sys.argv[2], sys.argv[2] + "-grafo"]
    drawing(argsDesenha)
