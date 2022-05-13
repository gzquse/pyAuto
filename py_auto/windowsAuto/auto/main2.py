import time, random
ran_number = random.randint(1000, 9999)
with open(r'C:\Users\MartinLovesFey\Documents\myworkbook\my_task.txt', 'a+') as w:
    w.write(str(ran_number) + ' ' + str(time.ctime() + '\n'))
exit()