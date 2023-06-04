#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:05:22 2022

@author: lmos
"""

def shortcut():
    mensagem = "puta"; vowels = ['a', 'e', 'i', 'o', 'u']; result = "";

    for char in mensagem:
              if char not in vowels:
                result = result + char

    print(result)
    
shortcut()
