#coding:utf-8
import os,time


work_path = '/data/project/livepic_image/destination_image'

copy_path = '/home/pi/imgs'

img_list = os.listdir(copy_path)

if not os.listdir(work_path):

    for img in img_list:

        with open(copy_path +'/'+ img, 'rb') as f1:

                data = f1.read()
                with open(work_path +'/' + img, 'ab') as f2:
                    if data:
                        f2.write(data)

    print('Copy image successfully   ' + time.strftime('%Y-%m-%d %X', time.localtime()))
else:

    print('There is no duplicate image    ' + time.strftime('%Y-%m-%d %X', time.localtime()))




