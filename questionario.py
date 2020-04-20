#!/usr/bin/python
# -*- coding: utf-8 -*-
# Vermelho e branco -> ('\033[0;30;41m'+' o texto'+'\033[0;0m] ])

import os
os.system('clear') or None

altura0 = 1.73
print ('\033[0;30;43m'+'Seja bem-vindo, precisamos coletar Algumas informações'+'\033[0;0m')
nome = input("qual o seu nome: ")
print('seja bem vindo ' + nome)
idade = input('Agora, informe a Sua idade:  ')
altura = float(input('Digite a Sua Altura:  '))
if altura < altura0:
    print ('\033[0;30;41m'+'Fato interessante: O homem brasileiro tem, em média, 1,73m, e a mulher, 1,60m. Ambos registraram o mesmo crescimento desde 1914: 8,6 cm'+'\033[0;0m')
else:
    print ('\033[0;30;41m'+'Fato curioso: Sabia que Sultan Kosen, é o homem mais alto do mundo, medindo 2,51 metros de altura.'+'\033[0;0m')
peso = float(input('Seu peso:  '))
imc = peso / (altura ** 2)
print ('\033[0;30;41m'+'Fato curioso: Você sabia que o seu IMC é de {:.1f}'.format(imc)+'\033[0;0m')
esporte = input('Você pratica esporte:  ')
if esporte == "sim":
    definicao = input('Qual o seu esporte: ')
    if definicao == "corrida":
        distancia = float(input('Qual a distancia (KM) você pecorre: '))
        tempo = float(input('tempo você leva pra precorrer: '))
else:
    print('O Conselho Nacional de Saúde, Adverte: informa que é necessario um exercico em sua vida')