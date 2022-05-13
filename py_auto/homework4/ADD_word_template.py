from basic_data import data
from docx import Document #创建文档
#基于模板 批量生成word -俗称套模板

document = Document('给家长的一封信模板/给家长的一封信.docx')

def add_info_TOtemplate(oldtext,newtext):
    all_para = document.paragraphs
    for para in all_para:
        for run in para.runs:
            print(run.text)
            if oldtext in run.text: #判断是否存在
                run.text = run.text.replace(run.text,newtext) #替换

add_info_TOtemplate('name','zz')
add_info_TOtemplate('score','300')
add_info_TOtemplate('rank','1')

# document.save('new.docx')


#读取学生数据
# student_info = data()
# print(student_info)

#这个部分是完成 word 和 ppt的制作 PART2
# for key,value in student_info.items():
#     #执行word
#     add_info_TOtemplate()
#



