# 家庭作业
import threading
import time


# LOCK
# 一号子线程   #1购买原材料  需要运行 2秒  需要一个lock 一切从这里开始 他必须要先做  实际消耗2

# LOCK        # 2.控制油烟机 开启油烟机 *需要运行 8秒 守护线程    实际消耗 3
# 二子线程     # 3.煮排骨      *需要运行 3秒
# 4. 排骨配菜    *需要运行1秒

# LOCK
# 三号子线程   # 5.下锅制作 *需要运行1秒   实际消耗1

# **主线程**
# 6.邀请客人上桌吃饭 *需要运行1秒   实际消耗1

def shopping(L):
    L.acquire()
    print('下单购物 ....！')
    time.sleep(2)
    print('购物完成！')
    L.release()


def prepare(L1):
    # 二级子线程
    L1.acquire()

    def extractor():  # 守护线程
        print('打开油烟机启动......')
        time.sleep(8)
        print('油烟机持续运行8秒完成！')

    def boil_steak():
        print('热水煮排骨....')
        time.sleep(3)
        print('排骨准备完毕！')

    def veg_prepare():
        print('排骨配菜....')
        time.sleep(1)
        print('配菜完成！')

    LT2_1 = threading.Thread(target=extractor, )
    LT2_2 = threading.Thread(target=boil_steak, )
    LT2_3 = threading.Thread(target=veg_prepare, )

    LT2_1.setDaemon(True)  # 抽油烟机设置为 守护线程

    LT2_1.start()
    LT2_2.start()
    LT2_3.start()
    # print(threading.activeCount())
    # LT2_1.join()
    LT2_2.join()
    LT2_3.join()

    L1.release()


def cook(L):
    with L:
        print('开始做饭....')
        time.sleep(1)
        print('完成做饭！出锅！')


# ---- 以下是主启动代码 ----
if __name__ == '__main__':

    # 做一个计时器
    start = time.time()

    # 建立锁
    L1 = threading.Lock()

    # 建立线程列表
    L1_thread = []
    # 创建线程
    LT1_1 = threading.Thread(target=shopping, args=(L1,))
    LT1_2 = threading.Thread(target=prepare, args=(L1,))
    LT1_3 = threading.Thread(target=cook, args=(L1,))
    # list添加线程
    L1_thread.append(LT1_1)
    L1_thread.append(LT1_2)
    L1_thread.append(LT1_3)

    # 启动线程
    for t in L1_thread:
        t.start()
    # 线程阻塞
    for t in L1_thread:
        t.join()

    # 最后主线程
    print('邀请客人')
    time.sleep(1)
    print('上桌子开吃')

    print(time.time() - start)
