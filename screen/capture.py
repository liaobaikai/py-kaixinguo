import pyautogui
from io import BytesIO
import base64
import socket
from PIL import Image
import time

import itertools


# import sys
# sys.platform == 'win32':



    # time.sleep(5)





class Capture:

    def __init__(self):
        self.last_img = None  # type: Image
        self.last_img_px = None

    def remove_last_image(self):
        self.last_img = None

    # 截图后并返回二进制图像数据
    def get_capture_bytes(self, width=0, height=0):

        img = self.compare(pyautogui.screenshot())
        # img = pyautogui.screenshot()

        output_buffer = BytesIO()
        # img.save(output_buffer, format="png")
        img.save(output_buffer, format="png")
        # img.save("{}.jpg".format(str(time.time())), format="png")
        return output_buffer.getvalue()

    def get_capture(self, fp):

        img = self.compare(pyautogui.screenshot())

        # output_buffer = BytesIO()
        # img.save(output_buffer, format="png")
        # img.save(output_buffer, format="png")
        img.save(fp, format="png")

    # 获取截图后的base64
    def get_capture_base64_bytes(self, width=0, height=0):
        return base64.b64encode(self.get_capture_bytes(width, height))

    def get_capture_base64(self, width=0, height=0):
        return self.get_capture_base64_bytes(width, height).decode()

    # 和上一次输出的图片进行比较
    def compare(self, img: Image):

        if self.last_img is None:
            self.last_img = img
            return img

        if self.last_img_px is None:
            # 前一个图片
            self.last_img = self.last_img.convert("RGBA")
            self.last_img_px = self.last_img.load()
            self.last_img.close()

        size = img.size

        output_image = Image.new("RGBA", size=size, )

        # 当前图片
        b1 = time.time()
        curr_img = img.convert("RGBA")   # type: Image.Image
        curr_img_px = curr_img.load()   # type: PIL.PixelAccess

        print("convert.load::::", time.time() - b1)

        b2 = time.time()

        s1 = range(size[0])
        s2 = range(size[1])

        # items = [x for x in s1]

        # def process(x):
        #     for y in s2:
        #         px1 = self.last_img_px[x, y]
        #         px2 = curr_img_px[x, y]
        #         if px1 != px2:
        #             # 两个像素点不同
        #             output_image.putpixel((x, y), px2)

        # with ThreadPoolExecutor(100) as executor:
        #     executor.map(process, items)

        # for p in itertools.product(s1, s2):
        #     x = p[0]
        #     y = p[1]
        #     px1 = self.last_img_px[x, y]
        #     px2 = curr_img_px[x, y]
        #     if px1 != px2:
        #         # 两个像素点不同
        #         output_image.putpixel((x, y), px2)
        print("s1:", s1)
        print("s2:", s2)
        for x in s1:
            for y in s2:
                px1 = self.last_img_px[x, y]
                px2 = curr_img_px[x, y]
                if px1 != px2:
                    # 两个像素点不同
                    output_image.putpixel((x, y), px2)

        print("convert.load::::for::::", time.time() - b2)

        self.last_img = img
        self.last_img_px = curr_img_px

        curr_img.close()

        return output_image


if __name__ == "__main__":

    # cap = Capture()
    # cap.get_capture("111.png")
    # cap.get_capture("222.png")
    # cap.get_capture("222.png")
    import numpy
    for i in range(100):
        t1 = time.time()
        img1 = Image.open("111.png")
        img2 = Image.open("111.jpg")
        a1 = numpy.array(img1)
        a2 = numpy.array(img2)

        a3 = a2 - a1

        Image.fromarray(a3).save("444.png")

        print(time.time() - t1)

    # b1 = time.time()
    # import numpy as np
    #
    # a = np.array(Image.open("111.png"))
    # b = np.array(Image.open("222.png"))
    #
    # Image.fromarray(a).save("333.png")

    # cap.get_capture("111.png")
    # print(time.time() - b1)
    # for i in range(10):
    #     b2 = time.time()
    #     cap.get_capture("222.png")
    #     print("b2:", time.time() - b2)
    # import time
    # import win32gui
    # import win32ui
    # import win32con
    # import win32api
    #
    # # while True:
    #     # divice context
    # win_dc = win32gui.GetWindowDC(0)
    #
    # mfc_dc = win32ui.CreateDCFromHandle(win_dc)
    #
    # save_dc = mfc_dc.CreateCompatibleDC()
    #
    # save_bitmap = win32ui.CreateBitmap()
    #
    # # monitors = win32api.EnumDisplayMonitors()   # type: list
    #
    # # for monitor in monitors:
    # #     # {'Monitor': (0, 0, 1440, 900), 'Work': (0, 0, 1440, 860), 'Flags': 1, 'Device': '\\\\.\\DISPLAY1'}
    # #     monitor_info = win32api.GetMonitorInfo(monitor[0])  # type: dict
    # #     display_monitor = monitor_info.get("Monitor")
    # #     width = display_monitor[2]
    # #     height = display_monitor[3]
    #
    # width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    # height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    #
    # print(width, height)
    #
    # save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
    #
    # save_dc.SelectObject(save_bitmap)
    #
    # save_dc.BitBlt((0, 0), (width, height), mfc_dc, (0, 0), win32con.SRCCOPY)
    #
    # file_name = "E:\\www\\{}.jpg".format(str(time.time()))
    #
    # save_bitmap.SaveBitmapFile(save_dc, file_name)
    #
    # win32gui.DeleteObject(save_bitmap.GetHandle())
    # save_dc.DeleteDC()
    # mfc_dc.DeleteDC()
    # win32gui.ReleaseDC(win_dc)