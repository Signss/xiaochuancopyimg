#coding:utf-8
import os, time, gevent
from gevent import monkey
monkey.patch_all()

work_path = '/home/python/Desktop/copy_imgs'
copy_path = '/home/python/Desktop/imgs'

img_list = os.listdir(copy_path)

num_thread = len(img_list)

def copy_img(n):
    with open(copy_path + '/' + img_list[n], 'rb') as rf:
        data = rf.read()
        with open(work_path + '/' + img_list[n], 'wb') as wf:
            if data:
                wf.write(data)

            else:
                print('null')


def run():
    if not os.listdir(work_path):
        for i in range(num_thread):
            g_copy = gevent.spawn(copy_img, i)

            g_copy.join()
            print(g_copy.getcurrent(),i,time.strftime('%Y-%m-%d %X', time.localtime()))
        print('ok' + time.strftime('%Y-%m-%d %X', time.localtime()))
    else:
        print('There is no duplicate image    ' + time.strftime('%Y-%m-%d %X', time.localtime()))


if __name__ == '__main__':
    run()