import threading
import time


def fun_timer():
    j = 1
    print('Hello Timer!' + str(j))


while True:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    timer = threading.Timer(5, fun_timer)  # 等待5s钟调用一次fun_timer() 函数
    timer.start()
    timer.join()
