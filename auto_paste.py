import win32api,time,win32con


def cv():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)

def right():
    win32api.keybd_event(0x27, 0, 0, 0)
    win32api.keybd_event(0x27, 0, win32con.KEYEVENTF_KEYUP, 0)

time.sleep(3)
for i in range(300):
    time.sleep(0.1)
    right()
    cv()