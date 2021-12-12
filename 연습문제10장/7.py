from random import *
from tkinter import *

# 선택 하는 부분
def user_choice_rock():
 user_choice = "rock"
 turn(user_choice)
 user_image.configure(image=rock_image)
def user_choice_paper():
 user_choice = "paper"
 turn(user_choice)
 user_image.configure(image=paper_image)
def user_choice_scissors():
 user_choice = "scissors"
 turn(user_choice)
 user_image.configure(image=scissors_image)
 
# 게임부분
def turn(user_choice):
 oppo = ['rock', 'paper', 'scissors']
 oppo_choice=oppo[randint(0,2)]
 if(oppo_choice=='rock'):
     oppo_image.configure(image=rock_image)
     if(user_choice=='paper'):
         turn_result.configure(text="사용자 승!", fg="green")
         compare.configure(text=">>>>>")
     elif(user_choice=='scissors'):
         turn_result.configure(text="컴퓨터 승!", fg="red")
         compare.configure(text="<<<<<")
     else:
         turn_result.configure(text="무승부", fg="gray")
         compare.configure(text="=====")
 
 elif(oppo_choice=='paper'):
     oppo_image.configure(image=paper_image)
     if(user_choice=='scissors'):
         turn_result.configure(text="사용자 승!", fg="green")
         compare.configure(text=">>>>>")
     elif(user_choice=='rock'):
         turn_result.configure(text="컴퓨터 승!", fg="red")
         compare.configure(text="<<<<<")
     else:
         turn_result.configure(text="무승부", fg="gray")
         compare.configure(text="=====")
 
 elif(oppo_choice=='scissors'):
     oppo_image.configure(image=scissors_image)
     if(user_choice=='rock'):
         turn_result.configure(text="사용자 승!", fg="green")
         compare.configure(text=">>>>>")
     elif(user_choice=='paper'):
         turn_result.configure(text="컴퓨터 승!", fg="red")
         compare.configure(text="<<<<<")
     else:
         turn_result.configure(text="무승부", fg="gray")
         compare.configure(text="=====")
 
# 메인 프로그램
main_window = Tk()
rock_button = Button(main_window, width=20, text="바위", justify=CENTER, 
command=user_choice_rock, activebackground='black', activeforeground='white')
paper_button = Button(main_window, width=20, text="보", justify=CENTER, 
command=user_choice_paper, activebackground='black', activeforeground='white')
scissors_button = Button(main_window, width=20, text="가위", justify=CENTER, 
command=user_choice_scissors, activebackground='black', activeforeground='white')
rock_image = PhotoImage(file="d:/rock.gif")
paper_image = PhotoImage(file="d:/paper.gif")
scissors_image = PhotoImage(file="d:/scissors.gif")
user_image = Label(text="사용자", image=rock_image)
user_image.image = rock_image
compare = Label(main_window, justify=CENTER, font=("Helvetica", 30))
oppo_image = Label(text="컴퓨터",image=paper_image)
oppo_image.image = paper_image
turn_result = Label(main_window, width=20, justify=CENTER, font=("Helvetica", 20))

# 그리드 생성
rock_button.grid(row=5, column=1)
paper_button.grid(row=5, column=2)
scissors_button.grid(row=5, column=3)
user_image.grid(row=3, column=1)
compare.grid(row=3, column=2)
oppo_image.grid(row=3, column=3)
turn_result.grid(row=4, column=2)

# GUI화면 루프처리
main_window.mainloop()