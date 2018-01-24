#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket               # 导入 socket 模块
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # 创建 socket 对象
s.bind(('', 12345))        # 绑定端口
s.listen(1)                 # 等待客户端连接
print('The server is ready to receive')
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print '连接地址：', addr
    c.send('欢迎访问菜鸟教程！')
    c.close()                # 关闭连接
