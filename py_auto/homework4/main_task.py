#负责统筹所有的功能模块
import os,zipfile
from basic_data import data
from word_template import letter_template
from ppt_template import ppt_template

#读取学生数据 PART1
student_info = data()
print(student_info)
#
'''
    :param parent_name: 父母姓名
    :param parent_title: 爸爸/妈妈
    :param student_name: 学生姓名
    :param score:  得分
    :param rank: 排名
    :return:
    '''
#这个部分是完成 word 和 ppt的制作 PART2
for key,value in student_info.items():
    #执行word
    letter_template(parent_name=value[2],parent_title=value[3],student_name=key,score=value[0],rank=value[1])
    #执行ppt student_name,image参数
    ppt_template(student_name=key,image='学生照片/%s.jpg'%key)

#最后的部分是完成zip打包的工作 PART3
for docfile in os.listdir('letters'):
    for pptfile in os.listdir('ppts'):
        if docfile.split('.')[0] == pptfile.split('.')[0]:
            z = zipfile.ZipFile( 'zips/%s.zip'%docfile.split('.')[0],'w' )
            for file in [ 'letters/'+docfile,'ppts/'+pptfile]:
                z.write(file)
            z.close()






