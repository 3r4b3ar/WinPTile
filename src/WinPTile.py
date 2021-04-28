import pygetwindow
import pyautogui

#WinPTile

# Take screen size

width, height = pyautogui.size()


print(
        width, height)

# Variables importantes

borders = 10

widthbor = width - (borders*2)
heigthbor = height - (borders*2)

print(
        widthbor)

Titulos = pygetwindow.getAllTitles()


numWin=1

for i in Titulos:
    numWin = numWin + 1

print(
        numWin)

def __init__(self, window_name=None, exe_file=None, exclude_border=True):
    hwnd = 0
    
    # first check window_name
    if window_name is not None:
        hwnd = win32gui.FindWindow(None, window_name)
        if hwnd == 0:
            def callback(h, extra):
                if window_name in win32gui.GetWindowText(h):
                    extra.append(h)
                return True
            extra = []
            win32gui.EnumWindows(callback, extra)
            if extra: hwnd = extra[0]
        if hwnd == 0:
            raise WindowsAppNotFoundError("Windows Application <%s> not found!" % window_name)

    # check exe_file by checking all processes current running.
    elif exe_file is not None:
        pid = find_process_id(exe_file)
        if pid is not None:
            def callback(h, extra):
                if win32gui.IsWindowVisible(h) and win32gui.IsWindowEnabled(h):
                    _, p = win32process.GetWindowThreadProcessId(h)
                    if p == pid:
                        extra.append(h)
                    return True
                return True
            extra = []
            win32gui.EnumWindows(callback, extra)
            #TODO: get main window from all windows.
            if extra: hwnd = extra[0]
        if hwnd == 0:
            raise WindowsAppNotFoundError("Windows Application <%s> is not running!" % exe_file)
    
    # if window_name & exe_file both are None, use the screen.
    if hwnd == 0:
        hwnd = win32gui.GetDesktopWindow()

    self.hwnd = hwnd
    self.exclude_border = exclude_border


print (__init__)
