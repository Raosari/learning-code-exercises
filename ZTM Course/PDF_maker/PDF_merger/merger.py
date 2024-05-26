import PyPDF2
import os
import sys

inputs = sys.argv[1:]

def merger_pdf(pdf_li):

    merger = PyPDF2.PdfMerger()

    for pdf in pdf_li:
        merger.append(pdf)
    merger.write('new_pdf')
    merger.close()


merger_pdf(inputs)