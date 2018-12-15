#coding:utf-8
import os,time

# 上传图片文件夹
work_path = '/data/project/livepic_image/destination_image'
# 存储图片文件夹
copy_path = '/home/pi/imgs'
# 存储图片文件夹列表
img_list = os.listdir(copy_path)
# 判断上传文件夹中是否又图片
if not os.listdir(work_path):

    for img in img_list:
        # 打开上传图片文件夹复制图片
        with open(copy_path +'/'+ img, 'rb') as f1:
                # 因为是上传一次数据就删除一次数据所以一次性读取
                data = f1.read()
                with open(work_path +'/' + img, 'ab') as f2:
                    if data:
                        f2.write(data)
    # 打印复制成功日志
    print('Copy image successfully   ' + time.strftime('%Y-%m-%d %X', time.localtime()))
else:
    # 打印复制失败日志
    print('There is no duplicate image    ' + time.strftime('%Y-%m-%d %X', time.localtime()))




