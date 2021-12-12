from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 400
  
class Ball:
     def __init__(self,canvas, color,size,x,y,xspeed,yspeed):
         self.canvas = canvas # 캔버스 객체
         self.color = color # Ball의 색상
         self.size = size # Ball의 크기
         self.x = x # Ball의 x좌표
         self.y = y # Ball의 y좌표
         self.xspeed = xspeed # Ball의 수평 방향 속도
         self.yspeed = yspeed # Ball의 수직 방향 속도
         self.img = None
 
         if self.size == 0:
             if self.color == "green":
                 self.img = PhotoImage(file="spaceship.png")
                 self.id = self.canvas.create_image(x,y,anchor=NW,image=self.img)
         else:
             self.img = PhotoImage(file="spaceship2.png")
             self.id = self.canvas.create_image(x,y,anchor=NW,image=self.img)
         else:
             self.id = canvas.create_oval(x,y,x+size,y+size, fill=color)
         def move(self): # Ball을 이동시키는 함수
             self.canvas.move(self.id, self.xspeed, self.yspeed)
             if self.size==0 :
             (x1,y1) = self.canvas.coords(self.id)
             (self.x, self.y) = (x1,y1)
             x2 = x1+100
             y2 = y1+100
         else:
             (x1,y1,x2,y2) = self.canvas.coords(self.id) # 공의 현재 위치를 얻는다.
             (self.x, self.y) = (x1,y1)
 
         if x1 <= 0 or x2 >= WIDTH: # 공의 x좌표가 음수이거나, x좌표가 오른쪽 경계를 
            넘으면
             print("check1")
             self.xspeed = -self.xspeed # 속도의 부호를 반전시킨다.
         if y1 <= 0 or y2 >= HEIGHT: # 공의 y좌표가 음수이거나, y 좌표가 오른쪽 경계를 넘으면
             print("check2")
             self.yspeed = -self.yspeed # 속도의 부호를 반전시킨다.
 # 생성된 포탄을 저장하는 리스트
bullets = []
# 마우스 버튼 이벤트를 처리하는 함수
def fire(event):
         bullets.append(Ball(canvas, "red",10,150,spaceship.y+50,10,0))
# 적을 맞추면 점수가 올라가도록
def getScore(score):
 score = score + 1
 return score
# 키보드 위쪽방향키 눌림 이벤트에 함수를 연결한다. def keyPress_UP(event):
 spaceship.yspeed = -3
# 키보드 아래쪽방향키 눌림 이벤트에 함수를 연결한다. def keyPress_Down(event):
 spaceship.yspeed = +3
# 키보드를 풀어줬을 때 이벤트처리
def keyRelease(event):
 spaceship.yspeed =0
# 윈도우를 생성한다. window = Tk()
canvas = Canvas(window, width=WIDTH,height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>",fire) # 마우스 버튼 클릭 이벤트에 함수를 연결한다. canvas.bind("<KeyPress-Up>",keyPress_UP) # 키보드 위쪽방향키 눌림 이벤트에 함수
를 연결한다. canvas.bind("<KeyPress-Down>",keyPress_Down) # 키보드 아래쪽방향키 눌림 이벤트
에 함수를 연결한다. canvas.bind("<KeyRelease>",keyRelease) # 키보드를 풀어줬을 때 이벤트 처
# 키보드 포커스를 갖게 한다
canvas.focus_set()
score = 0
var = StringVar()
label = Label(window, textvariable = var, relief = RAISED)
# 우리 우주선과 외계 우주선을 생성한다. spaceship = Ball(canvas,"green",0,100,200,0,0)
enemy = Ball(canvas,"red",0,500,200,0,5)
# 리스트에 저장된 각각의 객체들을 이동시킨다. while True:
 #print(spaceship.yspeed)
 var.set("score: "+str(score))
 label.pack()
 for bullet in bullets:
 bullet.move()
 # 포탄이 화면을 벗어나면 삭제한다.
 if (bullet.x + bullet.size) >= WIDTH:
 canvas.delete(bullet.id)
 bullets.remove(bullet)
 # 적을 맞추면 점수가 올라간다
 if bullet.x > enemy.x and bullet.x < enemy.x+100 and bullet.y > enemy.y 
and bullet.y < enemy.y+100:
 score = getScore(score)
 enemy.move()
 spaceship.move()
 window.update()
 time.sleep(0.03)