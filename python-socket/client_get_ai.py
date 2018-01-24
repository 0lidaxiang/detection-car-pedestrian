#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
import time
 

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口好

host = "192.168.1.179"
#host = "tegra-ubuntu"
print(host, port)
s.connect((host, port))
while 1:
	print s.recv(1024)
	time.sleep(0.5 )
s.close()  
