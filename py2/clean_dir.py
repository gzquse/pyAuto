import os, shutil

# 1.使用os shutil 和 zipfile完成该任务
# 2.要求对文件进行判断，大于10MB（兆）
# 3.满足文件大小，然后复制文件到统一的目录
# 4.把该目录下的文件进行zip压缩保存
# 特别注意 因为涉及到多级目录 需要使用绝对路径

folder = 'C:\\pythonClass\\家庭作业\\files'


# 归递算法，自己调用自己
def find_files(path):
    dirs = []
    # 先去找目录
    for file in os.listdir(path):
        # 如果是 目录添加到dirs列表中
        if os.path.isdir(os.path.join(path, file)):
            print(file)
            dirs.append(os.path.join(path, file))
        else:  # 如果不是目录 即文件，那么我们再处理下边的判断
            file_size_MB = os.path.getsize(os.path.join(path, file)) / 1024 / 1024
            if file_size_MB > 10:
                shutil.copy(os.path.join(path, file), 'myNewFiles')
    # 从dirs遍历文件/文件夹，再调用自己
    for i in dirs:
        find_files(i)


# find_files(folder)

# ------------------
import zipfile

with zipfile.ZipFile('NEW.zip', 'w') as w:
    for file in os.listdir('myNewFiles'):
        w.write(os.path.join('myNewFiles', file))
