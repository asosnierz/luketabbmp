#!/usr/bin/python
# -*- coding: utf-8 -*-


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

import sys
import os
os.system('clear') or None

#------------------------- comece abaixo -------------------

esporte = raw_input('Você pratica esporte:  ')
if esporte.lower() == "sim":
    esporte1 = input('Seu esporte precisa percorrer distancia? ')
    if esporte.lower() == "sim":
        definicao = input('Qual o seu esporte: ')
    if definicao.lower() == "corrida":
        distancia = float(input('Qual a distancia (KM) você pecorre: '))
        tempo = float(input('Qual o tempo que você leva em media pra precorrer: '))
        media = distancia / tempo
        print(media)
    elif definicao.lower() == "bicileta":
        distancia = float(input('Qual a distancia (KM) você pecorre: '))
        tempo = float(input('Qual o tempo que você leva em media pra precorrer: '))
        media = distancia // tempo
        print(media)
    else:
        print('É um Otimo esporte!')
else:
    print ('\033[0;30;47m'+'O Conselho Nacional de Saúde, Adverte: Sedentarismo, pode matar! o ideal é pelo menos praticar um esporte do seu gosto ou praticar uma caminhada leve passos curtos por 30 minutos'+'\033[0;0m')






