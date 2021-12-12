import random
from tkinter import *

window = Tk()
secret_number = random. randint(1, 100)
guess = None
num_guesses = 0

def guess_number():
    global num_guesses
    guess = int(entry.get())
    num_guesses += 1
    if guess == secret_number:
        message = "축하합니다!!"
    elif guess < secret_number:
        message = "너무 낮아요!!"
    else:
        message = "너무 높아요!!"
    label['text']= message
    
def reset():
    global num_guesses
    entry.delete(0, END)
    secret_number = random.randint(1, 100)
    guess = 0
    num_guesses = 0
    message = "1부터 100사이의 숫자를 추측하시오"
    label['text']= message
    
message = "1부터 100사이의 숫자를 추측하시오"
label = Label(window, text=message)
entry = Entry(window)

guess_button = Button(window, text="숫자를 입력", command=guess_number)
reset_button = Button(window, text="게임을 다시 실행", command=reset)

label.grid(row=0, column=0, columnspan=2, sticky=W+E)
entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
guess_button.grid(row=2, column=0)
reset_button.grid(row=2, column=1)


window.mainloop()