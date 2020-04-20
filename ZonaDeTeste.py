#!/usr/bin/python
# -*- coding: utf-8 -*-
# Vermelho e branco -> ('\033[0;30;41m'+' o texto'+'\033[0;0m] ])

'''
Entrada
nome
idade
altura
peso
pergunta ele se praticou corrida hoje
caso sim - distancia percorrida e o tempo
'''


'''
Saida
imc
Caso - media de velocidade praticada


Criar um repositorio no git
o codigo - publico
'''


import os


esporte = input('Você pratica esporte:  ')
if esporte == "sim":
    definicao = input('Qual o seu esporte: ')
    if definicao == "corrida":
        distancia = float(input('Qual a distancia (KM) você pecorre: '))
    elif tempo = float(input('tempo você leva pra precorrer' + distancia + 'KM': )):
else:
    print('Segundo a União de Saude, informa que é necessario um exercico em sua vida')
