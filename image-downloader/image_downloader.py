#!/usr/bin/env Python
# coding=utf-8
import sys
import os
import requests
import threading
import time

def downloadImg(url_list,path,start,end):
    print('thread %s is running...' % threading.current_thread().name)
    ss = requests.session()
    thread_name = threading.current_thread().name
    img_count = 0
    print(start,end)
    for img_url in url_list[start:end]:
        filename = os.path.basename(img_url)
        if os.path.exists(filename):
            pass
        else:
            #time.sleep(1)
            print("%s downloading %d/%d" % (thread_name,img_count,end - start))
            img_content = ss.get(img_url)
            name = img_url.split(".")
            # with open(os.path.join(path,thread_name + "_"+str(img_count) +"."+name[-1]),'wb') as f:
            with open(os.path.join(path, filename),'wb') as f:
                f.write(img_content.content)
        img_count = img_count + 1

    print('thread %s ended.' % threading.current_thread().name)



def download_manager(thread_sum, url_list, path):
    print("url_list length %d" % len(url_list))
    thread_count = 1
    thread = []
    interval = int(len(url_list) / int(thread_sum))
    start = 0
    end = 0
    while  thread_count <= int(thread_sum):
        if thread_count == int(thread_sum):
            end = int(len(url_list))
        else:
            end = end + interval

        print("%d\t%d" % (start,end))

        t = threading.Thread(target=downloadImg,args=(url_list,path,start,end),name="Thread" + str(thread_count))
        thread.append(t)
        start = end

        thread_count = thread_count + 1

    for t in thread:
        t.start()
    for t in thread:
        t.join()


if __name__ == '__main__':
    url_list = []
    # 读取文件
    file = open(sys.argv[2], 'r')
    line = file.readline()
    while line:
        line = line.replace('\n', "")
        url_list.append(line)
        line = file.readline()
    file.close()
    print("length  %d" % len(url_list))
    # 执行下载
    download_manager(sys.argv[1], url_list, sys.argv[3])


