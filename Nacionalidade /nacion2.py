#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:01:54 2023

@author: lmos
"""


#1 Pergunte qual país o usuário nasceu
#2 Pergunta qual país a mãe do usuário
#3 Pergunte qual país o pai do usuário nasceu
#4 Verifique se alguma das resposta é Brasil
#5 Verfique se os país são diplomatas
#6 Se sim, diga: brasileiro
#7 Se não, diga: estrangeiro


user = input("Qual país você nasceu? ")
user = user.strip().title()

mae = input ("Qual país sua mãe nasceu? ")
mae = mae.strip().title()

pai = input ("Qual país seu pai nasceu? ")
pai = pai.strip().title()

dip = input ("No momento do seu nascimento, seu país eram agentes estrangeiros a serviço de outro país? ")
dip =  dip.strip().title()

nacionalidade = [user, mae, pai, dip]

print(nacionalidade)


if "Brasil" in nacionalidade and "Sim" not in nacionalidade:
    print("você é brasileiro ")
    
else:
    print("você é estrangeiro")


    

    
    