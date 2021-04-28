import win32gui
windowTile = "" 
windowPlacement = ""
while (True): 
    newWindowTile = win32gui.GetWindowText (win32gui.GetForegroundWindow())
    newWindowPlacement = win32gui.GetWindowPlacement (win32gui.GetForegroundWindow())
    if( newWindowTile != windowTile):
        windowTile = newWindowTile  
        WindowPlacement = win32gui.GetWindowPlacement (win32gui.GetForegroundWindow())
        print( windowTile)
        print (windowPlacement)
