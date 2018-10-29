#!/usr/bin/env Python
# coding=utf-8

"""
 **************************************************************************
 *
 * Copyright (c) 2018 suning.com, Inc. All Rights Reserved
 *
 *
 * @file batch_register.py
 * @author liaotuo(18070959)
 * @date 2018/09/20
 * @version V1.0.0
 * @brief 批量图片转base64
 *
 **************************************************************************
 """

import os
import sys
import base64
import glob as gb

# 读取图片转base64
def image_to_base64(file_path):
    with open(file_path, "rb") as f:
        base64_data = base64.b64encode(f.read());
        return str(base64_data.decode())


# 执行转换
def do_encode(path_list, start, end):
    thread_name = threading.current_thread().name
    count = 0
    for path in path_list[start:end]:
        # 转化
        base64 = image_to_base64(path)
        print("%s,%s" % (os.path.basename(path), base64))
        # print("thread %s complete %d/%d" % (thread_name, count, end -start))
        count = count + 1
    # print('thread %s ended.' % threading.current_thread().name)


# 编码管理器 
# thread_sum 线程总数  
# path_list 图片路径列表 
def encode_manager(thread_sum, path_list):
    thread_sum = int(thread_sum)
    image_sum = int(len(url_list))
    # print("thread_sum %d\timage_sum %d" % (thread_sum, image_sum))
    thread = [] # 存放线程的数组
    interval = image_sum / thread_sum  # 切片间距

    thread_count = 0
    start = 0
    end = 0

    # 创建线程
    while thread_count < thread_sum:
        if thread_count == thread_sum:
            end = image_sum
        else:
            end = end + interval
        
        print("%d\t%d" % (start,end))
        t = threading.Thread(target=downloadImg,args=(image_sum, start, end),name="thread" + str(thread_count))
        thread.append(t)
        start = end

        thread_count = thread_count + 1

    for t in thread:
        t.start()
    for t in thread:
        t.join()


# 遍历文件夹下所有匹配文件名的文件路径列表
def get_path_list(base_path, match = '*'):
    path_list = gb.glob("base_path" +　"\\" + match)
    return path_list


# main
if __name__ == '__main__':
    path_list = get_path_list(sys.argv[1], "*.jpg")
    encode_manager(sys.argv[2], path_list)