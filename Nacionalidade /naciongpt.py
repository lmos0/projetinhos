#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 03:36:34 2023

@author: lmos
"""

def get_country(prompt):
    country = input(prompt).strip().title()
    if not country:
        raise ValueError("Campo precisa ser respondido")
    return country

def is_brazilian(birth_country, mother_country, father_country, foreign_agent):
    if birth_country != "Brasil":
        return False
    if foreign_agent == "Sim":
        return False
    if mother_country != "Brasil" and father_country != "Brasil":
        return False
    return True

try:
    birth_country = get_country("Em qual país você nasceu? ")
    mother_country = get_country("Em qual país você nasceu? ")
    father_country = get_country("Em qual país você nasceu?")
    foreign_agent = input("No momento do seu nascimento, seu país eram agentes estrangeiros a serviço de outro país? (Sim/Não) ").strip().title()
    if not foreign_agent in ["Sim", "Não"]:
        raise ValueError("Resposta inválida")
    
    if is_brazilian(birth_country, mother_country, father_country, foreign_agent):
        print("Você é brasileiro.")
    else:
        print("Você é estrangeiro.")

except ValueError as error:
    print(f"Error: {error}")
