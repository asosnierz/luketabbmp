#!/usr/bin/python
# -*- coding: utf-8 -*-
# Vermelho e branco -> ('\033[0;30;41m'+' o texto'+'\033[0;0m] ])

import os
os.system('clear') or None

altura0 = 1.73
print ('\033[0;30;43m'+'Seja bem-vindo, precisamos coletar Algumas informações'+'\033[0;0m')
nome = input("qual o seu nome: ")
print('seja bem vindo ' + nome)
idade = int(input('Agora, informe a Sua idade:  '))
altura = float(input('Digite a Sua Altura:  '))
if altura < altura0:
    print ('\033[0;30;46m'+'Fato interessante: O homem brasileiro tem, em média, 1,73m, e a mulher, 1,60m. Ambos registraram o mesmo crescimento desde 1914: 8,6 cm'+'\033[0;0m')
else:
    print ('\033[0;30;46m'+'Fato curioso: Sabia que Sultan Kosen, é o homem mais alto do mundo, medindo 2,51 metros de altura.'+'\033[0;0m')
peso = float(input('Seu peso:  '))
imc = peso / (altura ** 2)
print ('\033[0;30;46m'+'Fato curioso: Você sabia que o seu IMC é de {:.1f}'.format(imc)+'\033[0;0m')
if imc < 18.5:
    print ('\033[0;30;41m'+'você esta abaixo do peso normal pra escala da sua altura'+'\033[0;0m')
elif 18.5 <= imc < 25:
    print ('\033[0;30;42m'+'Parabéns, você esta na sua faixa de peso.'+'\033[0;0m')
elif 25 <= imc < 30:
    print ('\033[0;30;43m'+'Você esta com sobrepeso - pode ocorrer problema de saude serio'+'\033[0;0m')
elif 30 <= imc < 40:
    print ('\033[0;30;41m'+'Você esta em OBESIDADE, Cuidado'+'\033[0;0m')
elif imc >= 40:
    print ('\033[0;30;41m'+'você esta em OBESIDADE MÓRBITA'+'\033[0;0m')

esporte = input('Você pratica esporte:  ')
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
