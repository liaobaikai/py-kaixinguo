import win32api
import win32gui
import win32ui
import win32con

width, height = 800, 600

hwnd = 0 #Desktop
hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()
BitMap = win32ui.CreateBitmap()
BitMap.CreateCompatibleBitmap(mfcDC, width, height)
saveDC.SelectObject(BitMap)
saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
BitMap.SaveBitmapFile(saveDC, "test.png")

win32gui.DeleteObject(BitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hwndDC)