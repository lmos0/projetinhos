import os
import PyPDF2
import sys

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):  
        merger.append(file)
    
merger.write("testando.pdf")




