#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import logging


class Auto:
    def __init__(self, arq):
        arquivo = open(arq, "r")
        linhas = arquivo.read().splitlines()

        # Achar estados
        # O estados tem que conter pelo menos uma letra seguido por pelo menos um digito
        e = re.compile('\w+\d+')
        # Achando os estados no padrão do RegEx
        self.estados = e.findall(linhas[1])

        # Achar alfabeto
        a = re.compile('\w')
        # Achar as letras do alfabeto
        self.alfabeto = a.findall(linhas[2])

        # Achar os estados finais
        self.finais = e.findall(linhas[-2])

        # Achar o estado inicial
        self.inicial = e.findall(linhas[-3])[0]

        # Achar as funções de transição
        d = re.compile('(\w+\d+),(\w)->(\w+\d+)')
        self.trans = []
        for i in linhas:
            self.trans += (d.findall(i))

        self.corrige_estados()
        self.defEstadoTrans()

    def defEstadoTrans(self):
        self.estadoTrans = {}
        for e in self.estados:
            self.estadoTrans[e] = []

        for i in range(len(self.trans)):
            qi = self.trans[i][0]
            qj = self.trans[i][2]

            self.estadoTrans[qi] = list(set(self.estadoTrans[qi] + [i]))
            self.estadoTrans[qj] = list(set(self.estadoTrans[qj] + [i]))

    def corrige_estados(self):
        m = ''
        for e in self.estados:
            if len(e) > len(m):
                m = e

        m = len(m) - 1
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

    def minimiza(self):
        tabela = self.CriarTabela()
        self.AcharDisj(tabela)
        self.JuntaEstados(tabela)

    def CriarTabela(self):
        tabela = {}

        for i in range(len(self.estados)):
            qi = self.estados[i]
            for j in range(i + 1, len(self.estados)):
                qj = self.estados[j]
                key = (qi, qj)
                tabela[key] = {'disj': False, 'dp': []}

                if (qi in self.finais) != (qj in self.finais):
                    tabela[key]['disj'] = True

        return tabela

    def AcharDisj(self, tabela):
        logger = logging.getLogger('AcharDisj')

        for k in tabela:
            if tabela[k]['disj']:
                continue

            logger.info('Testando par {}'.format(k))

            for letra in self.alfabeto:
                if tabela[k]['disj']:
                    logger.info('par disjunto, desconsiderando')
                    continue

                # Procurar a função de transição de d(qi, s) -> qa
                for i in self.estadoTrans[k[0]]:
                    if(self.trans[i][1] == letra):
                        qa = self.trans[i][2]

                # Procurar a função de transição de d(qj, s) -> qb
                for i in self.estadoTrans[k[1]]:
                    if(self.trans[i][1] == letra):
                        qb = self.trans[i][2]

                _l = [qa, qb]
                _l.sort()
                qa = _l[0]
                qb = _l[1]
                par = (qa, qb)
                logger.info('par {} encontrado'.format(par))

                if qa == qb:
                    logger.info('os estados são iguais, pulando')
                    continue

                if tabela[par]['disj']:
                    logger.info('Os estados {} são disjuntos'.format(par))
                    tabela[k]['dis'] = True
                    self.PropagarErro(tabela, k)

                elif k != par:
                    logger.info('{} adicionado a \'dp\' de  {}'.format(k, par))
                    tabela[par]['dp'].append(k)

    def PropagarErro(self, tabela, k):
        logger = logging.getLogger('PropagarErro({})'.format(k))
        logger.info('Propagando erro de {}'.format(k))
        self.PropagarErroAux(tabela, k, None)

    def PropagarErroAux(self, tabela, k, anterior):
        logger = logging.getLogger('PropagarErroAux({})'.format(k))
        logger.info('Propagando erro de {}'.format(k))

        if k == anterior:
            logger.info('fim PropagarErroAux: {} == {}'.format(k, anterior))
            return

        for par in tabela[k]['dp']:
            logger.info('Propagando em {}'.format(par))
            tabela[par]['disj'] = True

            self.PropagarErroAux(tabela, par, k)

    def JuntaEstados(self, tabela):
        logger = logging.getLogger('JuntaEstados')

        estadosNDisj = {}
        for k in tabela:
            if not tabela[k]['disj']:
                estadosNDisj[k[0]] = []
                estadosNDisj[k[1]] = []

        for k in tabela:
            if not tabela[k]['disj']:
                logger.info('par {} não disjunto encontrado'.format(k))
                estadosNDisj[k[0]].append(k[1])
                estadosNDisj[k[1]].append(k[0])

        novosEstados = set([])
        for e in estadosNDisj:
            estadoNovo = [e] + estadosNDisj[e]
            estadoNovo.sort()

            nome = ''.join(estadoNovo)

            novosEstados.add((nome, tuple(estadoNovo)))

        novosEstados = list(novosEstados)
        logger.info('Lista de novos estados contruida')

        for i in novosEstados:
            final = False
            self.estados.append(i[0])

            if self.inicial in i[1]:
                self.inicial = i[0]

            for j in i[1]:
                logger.info('Subistituindo estado {} por {}'.format(j, i[0]))

                self.estados.remove(j)

                if j in self.finais:
                    self.finais.remove(j)
                    final = True

                for k in self.estadoTrans[j]:
                    t = list(self.trans[k])
                    if t[0] == j:
                        t[0] = i[0]

                    if t[2] == j:
                        t[2] = i[0]

                    self.trans[k] = tuple(t)

            if final:
                self.finais.append(i[0])

        self.trans = list(set(self.trans))

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
