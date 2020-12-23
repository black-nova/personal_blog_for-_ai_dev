import fitz
import glob
import os

def cool_ok(password):
    pdffile ='basic_app/pdf/'+ password
    doc = fitz.open(pdffile)
    page = doc.loadPage(0)  # number of page
    pix = page.getPixmap()
    password=password[:-4]

    output = 'basic_app/pdf/'+ password+'.jpg'
    pix.writePNG(output)