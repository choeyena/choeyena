from tkinter import *

def paint(event):
     global lastx, lasty
     x, y = (event.x),(event.y)
     canvas.create_line(lastx,lasty,x,y,fill = "black")
     lastx,lasty = x,y
     
def activate_paint(event):
     global lastx, lasty
     lastx, lasty = (event.x),(event.y) 
     
def release(event):
     global lastx, lasty
     
     if (lastx, lasty) == (event.x,event.y):
         canvas.create_line(lastx,lasty,lastx+1,lasty+1)
         
lastx,lasty = None, None

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind('<B1-Motion>',paint)
canvas.bind('<ButtonPress-1>', activate_paint) #B1-Press
canvas.bind('<ButtonRelease-1>',release) #B1-Release
window.mainloop()