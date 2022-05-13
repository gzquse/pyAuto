# pip install win32com

import os
from win32com import client


def DocToPDF(doc_name, pdf_name):
    word = client.DispatchEx("Word.Application")
    if os.path.exists(pdf_name):
        os.remove(pdf_name)
    worddoc = word.Documents.Open(doc_name,ReadOnly=1)
    worddoc.SaveAs(pdf_name,FileFormat=17)
    worddoc.Close()
    word.Quit()


# 注意是全路径 abspath
# print(os.path.abspath('.'))
# DocToPDF(os.path.join(os.path.abspath('.'),'letter.docx'),os.path.join(os.path.abspath('.'),'abbbc.pdf'))

def ExcelToPDF(Excel_name,pdf_name):
    Excel = client.DispatchEx("Excel.Application")
    if os.path.exists(pdf_name):
        os.remove(pdf_name)
    excel = Excel.Workbooks.Open(Excel_name,ReadOnly=1)
    excel.ExportAsFixedFormat(0,pdf_name)
    excel.Close()
    Excel.Quit()


#
# ExcelToPDF(os.path.join(os.path.abspath('.'),'VIPLIST.xlsx'),os.path.join(os.path.abspath('.'),'VIP.pdf'))


def pptTOPDF(PPT_name,pdf_name):
    PPT = client.DispatchEx('PowerPoint.Application')
    ppt = PPT.Presentations.Open(PPT_name)
    ppt.ExportAsFixedFormat(pdf_name,2,PrintRange=None)
    ppt.Close()
    PPT.Quit()


#
pptTOPDF(os.path.join(os.path.abspath('..'),'myFurniture.pptx'),os.path.join(os.path.abspath('..'),
                                                                             'newFurniture.pdf'))
