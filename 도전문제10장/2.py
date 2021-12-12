from tkinter import * 

window = Tk()


w = Button(window, text = "버튼1", bg="red", fg="white")
w.place(x=0, y=0)
w = Button(window, text = "버튼2", bg="orange", fg="white")
w.place(x=20, y=20)
w = Button(window, text = "버튼3", bg="yellow", fg="white")
w.place(x=40, y=40)
w = Button(window, text = "버튼4", bg="green", fg="white")
w.place(x=60, y=60)
w = Button(window, text = "버튼5", bg="blue", fg="white")
w.place(x=80, y=80)
window.mainloop()