#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from MinimizaAuto.class_auto import *

# Função utilitária
def xor(a, b):
    return ((a and not b) or (not a and b))

def CriarTabela(auto):
    # Criar uma tabela vazia
    tabela = []

    for i in range(0, len(auto.estados)):
        # Pegar o estado 'qi'
        qi = auto.estados[i]
        for j in range(i+1, len(auto.estados)):
            # Pegar o estado 'qj'
            qj = auto.estados[j]
            # Criar a linha da tabela
            tabela.append({"index":(qi, qj), "disj":False, "dp":[], "motivo":""})
            # Se apenas um deles for final
            if(xor(qi in auto.finais, qj in auto.finais)):
                # Marcar linha como inválida
                tabela[-1]["disj"] = True
                tabela[-1]["motivo"] = "final/nao-final"

    return tabela

def AcharDisj(auto, tabela):
    # Para cada conjunto (qi, qj)
    for i in tabela:
        # Não considerar os Final/Não-Final
        if(not i["disj"]):
            # Para cada simbolo do alfabeto
            for s in auto.alfabeto:
                # Pular i se ele ja foi marcado como disjunto
                if(i["disj"]):
                    continue

                # Procurar a função de transição de d(qi, s) -> qa
                qa = [(x,y,z) for (x,y,z) in auto.trans if(x==i["index"][0] and y==s)][0][2]
                # Procurar a função de transição de d(qj, s) -> qb
                qb = [(x,y,z) for (x,y,z) in auto.trans if(x==i["index"][1] and y==s)][0][2]

                # Ordenar para manter o padrão
                _a = min(qa, qb)
                _b = max(qa, qb)
                qa = _a
                qb = _b

                # Se as funções forem para estados diferentes, qa != qb
                if(qa != qb):
                    # Achar a linha de (qa, qb)
                    l=[tabela.index(item) for item in tabela if(item["index"]==(qa, qb))][0]

                    # Verificar se (qa, qb) é disjunto
                    if(tabela[l]["disj"]):
                        # Marcar como disjunto
                        i["disj"] = True
                        # Colocar o motivo
                        i["motivo"] = "{}[{},{}]".format(s, qa, qb)
                        # Propagar erro
                        PropagarErro(tabela, tabela.index(i))
                    else:
                        # Se (qa, qb) != (qi, qj)
                        if(i["index"] != (qa, qb)):
                            # colocar na depedencia de (qa, qb)
                            tabela[l]["dp"].append(i["index"])
    return tabela


def PropagarErro(tabela, i):
    # Para cada dependente na linha
    for j in tabela[i]["dp"]:
        # Achar a linha dos estados dependentes
        l = [tabela.index(item) for item in tabela if item["index"]==j][0]
        # Marcar como disjunto
        tabela[l]["disj"] = True
        # Colocar o motivo
        tabela[l]["motivo"] = "prop[{},{}]".format(tabela[i]["index"][0], tabela[i]["index"][1])
        # Propagar para os dependentes
        PropagarErro(tabela, l)


def JuntaEstados(auto, tabela):
    # Copiar o automato
    novoAuto = deepcopy(auto)
    # Pegar os não disjuntos
    nDisj = []
    for i in tabela:
        if(not i["disj"]):
            nDisj.append(i["index"])

    # Criar lista de novosEstados
    nvEstados = []
    for i in nDisj:
        # Nome do novo estado é a concatenação dos nomes dos antigos estados
        n = (("{}{}".format(i[0], i[1]), i))

        # Para cada item em nDisj
        for j in nDisj:
            if(i != j):
                # Substituir onde aparece qualquer um dos antigos estados pelo novo
                _j = list(j)

                qa = i[0]
                qb = i[1]
                if((j[0] == qa) or (j[0] == qb)):
                    _j[0] = n[0]

                if((j[1] == qa) or (j[1] == qb)):
                    _j[1] = n[0]

                nDisj[nDisj.index(j)] = tuple(_j)

        nvEstados.append(n)

    # Remover duplicata
    l = list(set(nDisj))
    # Ordenar a lista
    l.sort()
    # Mudar a lista de não Disjuntos
    nDisj = l[:]

    # Remover duplicata
    l = list(set(nvEstados))
    # Ordenar a lista
    l.sort()
    # Mudar a lista de não Disjuntos
    nvEstados = l[:]

    # Subistituir antigos estados pelos novos no novo automato
    for i in nvEstados:
        SubstituirNovoEstado(novoAuto, i)

    return novoAuto

def SubstituirNovoEstado(auto, nvEstado):
    # nvEstado = (qaqb, (qa, qb))
    qa = nvEstado[1][0]
    qb = nvEstado[1][1]

    # Se o i contém um dos estados antigos, substituir pelo novo
    for i in auto.estados:
        if(i == qa or i == qb):
            # Indice i
            _i = auto.estados.index(i)
            # atualizar i
            auto.estados[_i] = nvEstado[0]

    # Remover duplicata
    l = list(set(auto.estados))
    # Ordenar a lista
    l.sort()
    # Mudar a lista no automato
    auto.estados = l[:]


    # Substituir novo estado nas funções de transição
    for i in auto.trans:
        _i = list(i)

        # Se a origem for igual a qa ou qb
        if((i[0] == qa) or (i[0] == qb)):
            _i[0] = nvEstado[0]

        # Se o destino for igual a qa ou qb
        if((i[2] == qa) or (i[2] == qb)):
            _i[2] = nvEstado[0]

        index_i = auto.trans.index(i)
        auto.trans[index_i] = tuple(_i)

    # Remover duplicata
    l = list(set(auto.trans))
    # Ordenar a lista
    l.sort()
    # Mudar a lista no automato
    auto.trans = l[:]

    # Substituir novo estado nos finais
    for i in auto.finais:
        if((i == qa) or (i == qb)):
            _i = auto.finais.index(i)
            auto.finais[_i] = nvEstado[0]

    # Remover duplicata
    l = list(set(auto.finais))
    # Ordenar a lista
    l.sort()
    # Mudar a lista no automato
    auto.finais = l[:]

    # Subtituir no estado inicial
    if((auto.inicial == qa) or (auto.inicial == qa)):
        auto.inicial = nvEstado[0]


def ImprimeTabela(tabela):
    # Função para debugging
    for i in tabela:
        print("{}\t{}\t{}\t{}".format(i["index"], i["disj"], i["dp"], i["motivo"]))

