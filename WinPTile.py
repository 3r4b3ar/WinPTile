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

