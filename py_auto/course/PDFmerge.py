# pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileMerger

merger = PdfFileMerger()

for file in ['abbbc.pdf', 'newFurniture.pdf']:
    f = open(file, 'rb')
    file_reader = PdfFileReader(f)
    merger.append(file_reader, bookmark=file.split('.')[0], import_bookmarks=True)
    f.close()

merger.write('newMerged.pdf')
merger.close()