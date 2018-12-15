#coding:utf-8
import os, time, threading

# many thread work copy img
work_path = '/data/project/livepic_image/destination_image'
copy_path = '/home/pi/imgs'

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
     print("How many pieces of + %s + ok  %s" % (n, time.strftime('%Y-%m-%d %X', time.localtime())))


if __name__ == '__main__':
     if not os.listdir(work_path):
         for i in range(num_thread):
              copy_thread = threading.Thread(target=copy_img, args=(i,))
              copy_thread.start()
     else:
          print('There is no duplicate image    ' + time.strftime('%Y-%m-%d %X', time.localtime()))