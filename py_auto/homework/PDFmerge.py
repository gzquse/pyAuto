# pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileMerger
import os

merger = PdfFileMerger()

for file in os.listdir('pdfs'):
    f = open('pdfs/'+file, 'rb')
    file_reader = PdfFileReader(f)
    merger.append(file_reader, bookmark=file.split('.')[0], import_bookmarks=True)
    f.close()

merger.write('一年三班.pdf')
merger.close()