#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from desenhaGrafo.drawing import drawing
from desenhaGrafo.fileHandler import lerAutomato


def desenhaGrafo(args):
    logging.basicConfig(level=logging.INFO)

    auto = lerAutomato(args[0])
    drawing(auto, args[1])

