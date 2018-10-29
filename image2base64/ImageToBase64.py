# -*- coding: utf-8 -*-
import base64
import os
import tkFileDialog

default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
file_path = tkFileDialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
with open(file_path, "rb") as f:
    base64_data = base64.b64encode(f.read());
    print(base64_data)

with open("base64.txt", "wb") as f:
    f.write(base64_data)
    f.close()
