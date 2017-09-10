'''ASSIGNMENT 3'''
from ezgraphics import GraphicsWindow
import time
import random
win = GraphicsWindow(500,500)
can = win.canvas()
#asså.... ikke ta bryet i å lese dette kaoset... snakk med Franz om dette ;)
x = 0
y = 0

x2 = 500
y2=0

x3 = 250
y3 = 500

x4 = 0
y4 = 250
height = 8
width = 8

x5 = 240
y5 = 240
height5 = 30
width5 = 30

trolling = True
while trolling:
    can.setFill(255,0,0)
    can.drawOval(x, y, height, width)
    time.sleep(0.001)
    #Canvas
    can.setFill(0,255,0)
    can.drawOval(x2, y2, height, width)
    x += 1
    y+=1
    x2 -=1
    y2 +=1
    if x > 500:
        can.setFill(0,0,255)
        can.drawOval(x3, y3, height, width)
        can.setFill(20,20,255)
        can.drawOval(x4, y4, height, width)
        time.sleep(0.0001)
        x4 += 1
        y3 -= 1
        if y3 < 1:
            r1 = random.randint(0,500)
            r2 = random.randint(0,500)
            r3 = random.randint(0,255)
            r4 = random.randint(0,255)
            r5 = random.randint(0,255)
            can.setFill(255-r3,255-r4,255-r5)
            can.drawOval(r1, r2, 30, 30)
            can.setFill(0,255,0)
            can.drawOval(x5, y5, width5, height5)
            time.sleep(0.00001)
            can.setFill(0,0,255)
            can.drawOval(x5, y5, width5, height5)
            time.sleep(0.00001)
            can.setFill(255,0,0)
            can.drawOval(x5, y5, width5, height5)
            time.sleep(0.00001)
            r1 = random.randint(0,500)
            r2 = random.randint(0,500)
            r3 = random.randint(0,255)
            r4 = random.randint(0,255)
            r5 = random.randint(0,255)
            can.setFill(255-r3,255-r4,255-r5)
            can.drawOval(r1, r2, 30, 30)
            x5 -= 2
            y5 -= 2
            height5 += 4
            width5 += 4
            if height5 > 500:
                trolling = False

input("Done. Red circle achieved.")
win.wait()
