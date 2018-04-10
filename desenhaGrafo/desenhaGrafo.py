#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from desenhaGrafo.drawing import drawing
from desenhaGrafo.fileHandler import lerAutomato


def desenhaGrafo(args):
    logging.basicConfig(level=logging.INFO)

    auto = lerAutomato(args[1])
    drawing.desenhaGrafo(auto, args[2])

