from tkinter import *

def do_convert():
    inch_val = float(cvt_from.get())
    centimeters_val = inch_val * 2.54
    cvt_to.set('%s 센티미터' % centimeters_val)
    
root = Tk()
cvt_from = StringVar() 
cvt_to = StringVar()

lbl = Label(root, text='인치를 센티미디로 변환하는 프로그램:') 
lbl.grid(row=0, column=0, columnspan=2)
from_lbl = Label(root, text='인치를 입력하시오:')
from_lbl.grid(row=1, column=0) 
from_entry = Entry(root, textvariable=cvt_from)
from_entry.grid(row=1, column=1)

to_lbl = Label(root, text='변환결과:')
to_lbl.grid(row=2, column=0)
result_lbl = Label(root,
                   textvariable=cvt_to)
result_lbl.grid(row=2, column=1)

convert_btn = Button(root,
                     text='변환!', command=do_convert)
convert_btn.grid(row=3, column=1)
root.mainloop()