from tkinter import *

window = Tk()
label1 = Label(window, text="로그인 하세요!!!", font=("Helvetica", 20))
label1.pack()
label2 = Label(window, text="아이디")
label2.pack()
entry1 = Entry(window)
entry1.pack()
label2 = Label(window, text="패스워드")
label2.pack()
entry2 = Entry(window)
entry2.pack()
button1 = Button(window, text="로그인")
button1.pack()
window.mainloop()