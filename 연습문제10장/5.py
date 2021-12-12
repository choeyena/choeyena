from tkinter import *
fields = '이름', '직업', '국적'

def fetch(entries):
 for entry in entries:
     field = entry[0]
     text = entry[1].get()
     print('%s: "%s"' % (field, text)) 
 
def makeform(root, fields):
 entries = []
 for field in fields:
     row = Frame(root)
     lab = Label(row, width=15, text=field)
     ent = Entry(row)
     row.pack(side=TOP, fill=X)
     lab.pack(side=LEFT)
     ent.pack(side=RIGHT, expand=YES, fill=X)
     entries.append((field, ent))
 return entries

root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
b1 = Button(root, text='보여주기',
 command=(lambda e=ents: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='종료하기', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)
root.mainloop()