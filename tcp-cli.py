#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

target_host = 'www.baidu.com'
target_port = 80
#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接服务端
client.connect((target_host, target_port))
#向服务端发送数据
client.send('GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n')
#从服务端接收数据
response = client.recv(4096)
print response
