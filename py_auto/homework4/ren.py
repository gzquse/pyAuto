import os
for file in os.listdir('学生照片'):

    os.rename('学生照片/%s'%file,'学生照片/%s.jpg'%file.split('.')[0])