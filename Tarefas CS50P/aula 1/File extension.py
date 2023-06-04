#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:43:34 2023

@author: lmos
"""

arq = input("Nome do arquivo: ").strip()


if arq.endswith(".gif"):
    print("image/gif")
    
elif arq.endswith(".jpg"):
    print("image/jpeg")
    
elif arq.endswith(".jpeg"):
    print("image/jpeg")
    
elif arq.endswith(".png"):
    print("image/png")
    
elif arq.endswith(".pdf"):
    print("application/pdf")    
    
elif arq.endswith(".txt"):
    print("text/plain")
    
elif arq.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")

                