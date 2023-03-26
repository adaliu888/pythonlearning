import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:

    input("")
    startime = time.time()
    print(startime)
    print(type(startime))
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - startime, 2), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - startime, 2), 'secs')
        break
