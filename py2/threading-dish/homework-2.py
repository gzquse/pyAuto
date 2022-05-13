import time


def shopping():
    print('下单购物 ....！')
    time.sleep(2)
    print('购物完成！')


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


def cook():
    print('开始做饭....')
    time.sleep(1)
    print('完成做饭！出锅！')


def visitor():
    print('邀请客人')
    time.sleep(1)
    print('上桌子开吃')


if __name__ == '__main__':
    start = time.time()
    shopping()
    extractor()
    boil_steak()
    veg_prepare()
    cook()
    visitor()
    print(time.time() - start)
