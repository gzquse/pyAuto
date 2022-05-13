# pip install pdfminer3k
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def parsePDF(pdf_path):
    pdf = open(pdf_path, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    parser = PDFParser(pdf)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF 资源器 方便共享资源
        resource_manager = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(resource_manager, laparams=laparams)

        interpreter = PDFPageInterpreter(resource_manager, device)

        # 用来计数页面，水平文本框等对象的数量
        num_page, num_Text = 0, 0

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            num_page += 1  # 页面增一
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                    num_Text += 1  # 水平文本框对象增一
                    # 保存文本内容
                    with open(r'test.txt', 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + '\n')
        print('页面数：%s\n ' % num_page, '水平文本框：%s\n' % num_Text)


pdf_path = r'abbbc.pdf'
parsePDF(pdf_path)
