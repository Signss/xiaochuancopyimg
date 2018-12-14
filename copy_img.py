#coding:utf-8
import os,time

# 上传图片文件夹
work_path = '/data/project/livepic_image/destination_image'
# 存储图片文件夹
copy_path = '/home/pi/imgs'
# 获取存储图片文件夹下图片目录
img_list = os.listdir(copy_path)
# 判断上传图片文件是否为空
if not os.listdir(work_path):
    # 为空
    for img in img_list:
        # 循环打开存储图片文件夹读取图片写入上传图片文件夹
        with open(copy_path +'/'+ img, 'rb') as f1:
                # 因为上传文件夹只要又信息就会上传删除信息所以采用一次读取一个文件
                data = f1.read()
                with open(work_path +'/' + img, 'ab') as f2:
                    if data:
                        f2.write(data)
    # 复制成功日志信息
    print('Copy image successfully   ' + time.strftime('%Y-%m-%d %X', time.localtime()))
else:
    # 暂时不用复制日志信息
    print('There is no duplicate image    ' + time.strftime('%Y-%m-%d %X', time.localtime()))




