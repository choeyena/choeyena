import pickle
from tkinter import *

phone_book = { }
current = 0
name = ""
phone = ""

window = Tk() 

frame1 = Frame(window)
frame1.pack()
Label(frame1, text = "이름 ").grid(row = 1, column = 1, sticky = W)
nameEntry = Entry(frame1, textvariable = name, width = 30)
nameEntry.grid(row = 1, column = 2)

frame2 = Frame(window)
frame2.pack()
Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)
phoneEntry = Entry(frame2, textvariable = phone, width = 30)
phoneEntry.grid(row = 1, column = 2)

frame3 = Frame(window)
frame3.pack()

def save():
     outfile = open("phonebook.dat", "wb")
     pickle.dump(phone_book, outfile)
     print("주소들이 파일에 저장되었습니다")
     outfile.close()
     
def load():
     infile = open("phonebook.dat", "rb")
     phone_book = pickle.load(infile)
     infile.close()
     print("파일에서 주소를 읽었습니다.")
     go_first()
     
def add():
     phone_book[nameEntry.get()] = phoneEntry.get()
     print(phone_book)
     save()
     
def go_first():
     global current
     current = 0
     ks = list(phone_book)
     print(phone_book)
     nameEntry.delete(0, END)
     nameEntry.insert(0, ks[current])
     phoneEntry.delete(0, END)
     phoneEntry.insert(0, phone_book[ks[current]])
     
def go_next():
     global current
     current += 1
     ks = list(phone_book)
     nameEntry.delete(0, END)
     nameEntry.insert(0, ks[current])
     phoneEntry.delete(0, END)
     phoneEntry.insert(0, phone_book[ks[current]])
     
def go_previous():
     print("구현되지 않았음")
     
def go_last():
     print("구현되지 않았음")
b1 = Button(frame3, text = "추가", command = add).grid(row = 1, column = 1)
b2 = Button(frame3, text = "처음", command = go_first).grid(row = 1, column = 2)
b3 = Button(frame3, text = "다음", command = go_next).grid(row = 1, column = 3)
b4 = Button(frame3, text = "이전", command =go_previous).grid(row = 1, column = 4)
b5 = Button(frame3, text = "마지막", command = go_last).grid(row = 1, column = 5)
b6 = Button(frame3, text = "파일 읽기", command = load).grid(row = 1, column = 6)

window.mainloop()