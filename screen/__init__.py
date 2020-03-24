# 截屏实现

# 思路：
# Mac: 系统自带应用程序截图，screencapture -C -t jpg -x -r output.jpg
# Window: 使用win32api, win32gui, win32ui, win32con（官方的API）进行截图


__all__ = ["capture"]
