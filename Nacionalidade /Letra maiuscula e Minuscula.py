#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:40:11 2023

@author: lmos
"""

def text_case_conversion(text):
  upper_case = text.upper()
  lower_case = text.lower()
  return upper_case, lower_case

text = input("Enter text: ")
upper_case, lower_case = text_case_conversion(text)
print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
