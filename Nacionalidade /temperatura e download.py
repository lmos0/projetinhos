#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:22:27 2023

@author: lmos
"""

t = int(input("Qual temperatura em F? "))

T = (t-32)*5/9
print("A temperatura em Celsius é ", T)

arq = int(input("Qual tamanho do arquivo em mb? "))
vel = int(input("Qual a velocidade da sua internet em Mbps? "))

duracao = arq/vel/8

x = divmod(duracao, 60)
print(x)