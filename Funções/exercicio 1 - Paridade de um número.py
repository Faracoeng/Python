# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def verificaPar(num):
    return num % 2 == 0

numero = int(input('Digite um número para descobrir se é par ou ímpar: '))
if verificaPar(numero):
    print('número par')
else: 
    print('número ímpar') 
