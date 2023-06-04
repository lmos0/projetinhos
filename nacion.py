#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 07:48:29 2022

@author: lmos
"""

n1 = None
n2 = input

local = input("País de Nacimento ")
print(local)

if local != "Brasil":
    print("estrangeiro");

if local != "Brasil":
    n1 = "estrangeiro";
    
if n1 == "estrangeiro":
    print("Qual a nacionalidade do seu pai?")
input = n2


nacionalidade = ['nato', 'naturalizado', 'estrangeiro']
nacionalidade.sort()
#print(nacionalidade)

local_nascimento = ['Brasil', 'outro país']
#print(local_nascimento)

