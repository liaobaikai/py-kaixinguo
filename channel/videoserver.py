import socket
import os
import socketserver
from screen import capture

buffer_size = 1024

if hasattr(os, "fork"):
    from socketserver import ForkingTCPServer

    _TCPServer = ForkingTCPServer
else:
    from socketserver import ThreadingTCPServer

    _TCPServer = ThreadingTCPServer


# 图像服务器，有客户端连接来的话，就开始抓取图像
class VideoServer(_TCPServer):
    allow_reuse_address = True

    def __init__(self, server_address, handler):
        super().__init__(server_address, handler)


# 请求处理
# 当有客户端请求进来的话，就开始抓取图片
class VideoServerRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.keep_alive = True
        super().__init__(request, client_address, server)

    def handle(self):
        req = self.request  # type: socket.socket
        while self.keep_alive:
            # 获取图像数据
            img_bytes = capture.get_capture_bytes()

            begin = 0
            next_it = True
            while next_it:
                sub_img_bytes = img_bytes[begin: buffer_size]
                if len(sub_img_bytes) < buffer_size:
                    # 没有数据了
                    next_it = False
                # 需要不断的发送数据
                req.send(sub_img_bytes)

    def finish(self):
        self.keep_alive = False
