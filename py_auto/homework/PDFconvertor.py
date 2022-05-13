import os
from win32com import client
from time import sleep


def DocToPDF(doc_name, pdf_name):
    word = client.DispatchEx("Word.Application")
    if os.path.exists(pdf_name):
        os.remove(pdf_name)
    worddoc = word.Documents.Open(doc_name, ReadOnly=1)
    worddoc.SaveAs(pdf_name, FileFormat=17)
    worddoc.Close()
    word.Quit()


def pptTOPDF(PPT_name, pdf_name):
    PPT = client.DispatchEx('PowerPoint.Application')
    ppt = PPT.Presentations.Open(PPT_name)
    ppt.ExportAsFixedFormat(pdf_name, 2, PrintRange=None)
    ppt.Close()
    PPT.Quit()


def convertor():
    for file in os.listdir('files'):
        print(os.path.join(os.path.abspath('pdfs'), file.split('.')[0] + '.pdf'))
        if 'pptx' in file:
            pptTOPDF(os.path.join(os.path.abspath('files'), file),
                     os.path.join(os.path.abspath('pdfs'), file.split('.')[0] + '.pdf'))
        elif 'docx' in file:
            DocToPDF(os.path.join(os.path.abspath('files'), file),
                     os.path.join(os.path.abspath('pdfs'), file.split('.')[0] + '.pdf'))


convertor()
