#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

import drawing
import fileHandler


def main():
    logging.basicConfig(level=logging.INFO)

    auto = fileHandler.lerAutomato(sys.argv[1])
    drawing.desenhaGrafo(auto, sys.argv[2])


main()
