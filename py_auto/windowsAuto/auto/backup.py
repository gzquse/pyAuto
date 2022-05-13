import datetime, shutil, os
path = 'C:/Users/MartinLovesFey/Desktop/'
folder = datetime.datetime.today().strftime('%y-%m-%d')
os.mkdir(path+folder)

for file in os.listdir(path):
    if 'txt' in file:
        shutil.move(os.path.join(path, file), os.path.join(path+folder, file))