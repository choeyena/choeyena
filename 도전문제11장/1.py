from tkinter import *
import random

def show(char):
     display.delete(0,END)
     display.insert(0,"단어를 추측하시오:")
     global blanked
     blanked = 0
     global guesses
 
     for char in word:
         if char in guesses:
             display.insert(END,char)
         else:
             display.insert(END,"_ ")
             blanked += 1
             
def click(char):
     show(char)
     global turns
     global label 
     global blanked
 
     if blanked == 0:
         label = Label(root, text = "사용자 승리",width = 20, height=1, fg="red", 
relief="solid")
         label.grid(row=row_index,column=col_index,columnspan=5)
         chooseWord()
         return
     
     if char not in word:
         turns -= 1
         label = Label(root,text=str(turns)+"번의 기회가 남았음!", width=20, height=1, 
fg="red", relief="solid")
         label.grid(row=row_index,column=col_index, columnspan=5)
         
     if turns <= 0:
         label = Label(root, text = "사용자 패배", width = 20, height=1, fg = "red", 
relief = "solid")
         label.grid(row=row_index, column = col_index, columnspan=5)
         chooseWord()
         return
     
def chooseWord():
     global word
     global turns
     turns = 10
     global guesses
     guesses = ""
     global label
     label = Label(root,text=str(turns)+"번의 기회가 남았음!", width=20, height=1, 
fg="red", relief="solid")
 
     infile = open("words.txt","r")
     lines = infile.readlines()
     word = random.choice(lines)
     word = word.replace(" ","")
     word = word.replace("\n","")
     
     show("")
     
     
root = Tk()
root.title("Hangman Game")
root.geometry("300x225")
display = Entry(root, width=33, bg="yellow")
display.grid(row=0,column=0,columnspan=5)

guesses = ""
turns = 10
word=""

chooseWord()

button_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
row_index=1
col_index=0

blanked = 0
display.delete(0,END)
display.insert(0,"단어를 추측하시오:")
show("")

for button_text in button_list:
     def process(guess=button_text):
         global guesses
         global turns
         guesses += guess
         click(guess)
 
Button(root,text=button_text,width=5,command=process).grid(row=row_index,column=col_index)
col_index += 1
if col_index > 4:
         row_index += 1
         col_index = 0
         
row_index += 1
        
root.mainloop()