from screen.capture import Capture
from channel import videoserver
import websocket
import base64
import time
import json
import hashlib
import time
import mson


buffer_size = 1024

capture = Capture()

md5 = hashlib.md5()


def on_message(ws: websocket.WebSocketApp, message: str):
    # 发送本机信息后，响应是否绑定成功
    # 如果绑定成功的话，回显给用户查看。（已连接到服务器，用户名，密码）
    # 考虑粘包的情况
    # 如：{"size": {"width": 0, "height": 0}, "action": "capture", "debug": 1}{"size": {"width": 0, "height": 0}, "action": "capture", "debug": 1}
    # try:
    #     obj = json.loads(message)   # type: dict
    # except Exception as e:
    #     print(message)
    #     print("连接已关闭！")
    #     ws.close()

    # if obj.get("action") == "capture":
    messages = mson.parse(message)
    print(messages)
    for item in messages:
        if item.get("action") == "capture":

            if item.get("emit") == "full":
                capture.remove_last_image()

            img_bytes = capture.get_capture_bytes()
            ws.send(img_bytes, opcode=websocket.ABNF.OPCODE_BINARY)

        elif item.get("action") == "capture":
            print("暂停采集....")

    # img_bytes = capture.get_capture_base64()
    #
    # md5.update(img_bytes)
    #
    # str_md5 = md5.hexdigest()
    #
    # print(time.time())
    #
    # print(str_md5)
    #
    # ws.send(img_bytes, opcode=websocket.ABNF.OPCODE_BINARY)
    #
    # time.sleep(1)

    # print(message)




def on_error(ws, error):
    print(error)


def on_close(ws):
    # 重新连接
    print("### closed ###")
    print("2秒后，尝试重新连接")
    time.sleep(5)
    init()


def on_open(ws):
    # 发送本机信息
    print("已发送账号信息")
    ws.send('{"xid":"1001","pwd":"123456"}')
    capture.remove_last_image()
    # 如果是首次安装的话，这个xid和密码应该是空的
    # ws.send('{xid":"","pass":""}')



def init():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8890",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


init()
