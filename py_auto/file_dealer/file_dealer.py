import os
import shutil
import time

# src_files = 'files'
# for file in os.listdir(src_files):
#     if 'jpg' in file:#files/aaa.jpg
#         shutil.copy(src=src_files+'/'+file,dst='newWorld_1/images')
#
#     elif 'mp4' in file:
#         shutil.copy(src=src_files+'/'+file,dst='newWorld_1/videos') #os.path.join(a,b,c)

src_files = 'files'
for file in os.listdir(src_files):  # 遍历目标文件夹
    if 'jpg' in file:
        m_time = os.path.getmtime(os.path.join(src_files, file))
        real_time = time.localtime(m_time)
        dt = time.strftime("%Y-%m-%d", real_time)
        year, month, day = dt.split('-')  # 把时间split切分 2020-11-20 ['2020','11','20']
        if os.path.exists(os.path.join('newWorld_2', 'images', year)):  # 判断是否有年目录
            if os.path.exists(os.path.join('newWorld_2', 'images', year, month)):  # 判断是否有月目录
                # 把文件复制进去
                shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'images', year, month))
            else:  # 如果月目录不存在则创建 并复制 mkdir c:/zz/zz/zz/
                os.makedirs(os.path.join('newWorld_2', 'images', year, month))  # 特别注意mkdir/makedirs
                shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'images', year, month))
        else:  # 这种情况是年目录不存在 那么就 一口气创建年/月目录再复制
            os.makedirs(os.path.join('newWorld_2', 'images', year, month))
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'images', year, month))

    elif 'mp4' in file:
        m_time = os.path.getmtime(os.path.join(src_files, file))
        real_time = time.localtime(m_time)
        dt = time.strftime("%Y-%m-%d", real_time)
        year, month, day = dt.split('-')
        if os.path.exists(os.path.join('newWorld_2', 'videos', year)):  # 判断是否有年目录
            if os.path.exists(os.path.join('newWorld_2', 'videos', year, month)):  # 判断是否有月目录
                # 把文件复制进去
                shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'videos', year, month))
            else:  # 如果月目录不存在则创建 并复制
                os.makedirs(os.path.join('newWorld_2', 'videos', year, month))
                shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'videos', year, month))
        else:  # 这种情况是年目录不存在 那么就 一口气创建年/月目录再复制
            os.makedirs(os.path.join('newWorld_2', 'videos', year, month))
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', 'videos', year, month))
