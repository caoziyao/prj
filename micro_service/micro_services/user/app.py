# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
import time
import grpc
from concurrent import futures
from proto import user_pb2_grpc
from config import config
from .services import Greeter


class App(object):

    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
        user_pb2_grpc.add_UserServicer_to_server(Greeter(), self.server)

        ins_port = '[::]:{}'.format(config.user_port)
        self.server.add_insecure_port(ins_port)

    def delay(self):
        try:
            while True:
                time.sleep(config.day)
        except KeyboardInterrupt:
            self.server.stop(0)

    def run(self):
        # gRPC 服务器
        print('run user {}:{}'.format(str(config.user_host), str(config.user_port)))
        self.server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
        self.delay()
