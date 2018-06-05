#!/usr/bin/env python
#-*- coding:utf-8 -*-   
 
from include import *
############################
# 启动后台



# Socket后台
serverSocket = ServerSocket("39.107.26.100", 8092)
serverSocket.start()
sleep(1)
# ServiceHttp 处理http请求
# serverHttp = ServerHttp(8086)
# serverHttp.start()

# 线程 Opencv监控摄像头 识别图像 调用socket推送消息
serverCamera = ServerCamera(serverSocket)
serverCamera.start()

# 线程 各种传感器监控 轮循监控
# serverSensor = ServerSensor(serverSocket)
# serverSensor.start()

while 1:
    pass

















