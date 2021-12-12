from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None

# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def open():
     global im, tk_img
     fname = fd.askopenfilename()
     im = Image.open(fname)
     tk_img = ImageTk.PhotoImage(im)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 파일 메뉴에서 "종료"를 선택하였을 때 호출되는 함수
def quit():
     window.quit()
     
# 영상처리 메뉴에서 "영상회전"을 선택하였을 때 호출되는 함수
def image_rotate():
     global im, tk_img
     out = im.rotate(45)
     tk_img = ImageTk.PhotoImage(out)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 영상처리 메뉴에서 "영상흐리기"를 선택하였을 때 호출되는 함수
def image_blur():
     global im, tk_img
     out = im.filter(ImageFilter.BLUR)
     tk_img = ImageTk.PhotoImage(out)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 영상처리 메뉴에서 "흑백영상"를 선택하였을 때 호출되는 함수
def image_grayscale():
     global im, tk_img
     im1 =im.convert('L')
     tk_img = ImageTk.PhotoImage(im1)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 영상처리 메뉴에서 "이진화"를 선택하였을 때 호출되는 함수
def image_bin():
     global im, tk_img
     im1 =im.convert('1')
     tk_img = ImageTk.PhotoImage(im1)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 영상처리 메뉴에서 "영상뚜렷하게"를 선택하였을 때 호출되는 함수
def image_sharp():
     global im, tk_img
     out = im.filter(ImageFilter.SHARPEN)
     tk_img = ImageTk.PhotoImage(out)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 영상처리 메뉴에서 "엠보스"를 선택하였을 때 호출되는 함수
def image_emboss():
     global im, tk_img
     out = im.filter(ImageFilter.EMBOSS)
     tk_img = ImageTk.PhotoImage(out)
     canvas.create_image(250,250,image=tk_img)
     window.update()
     
# 윈도우를 생성한다. 
window = tk.Tk()
canvas = tk.Canvas(window,width=500,height=500)
canvas.pack()

# 메뉴를 생성한다. 
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label="열기", command = open)
filemenu.add_command(label="종료", command = quit)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
ipmenu.add_command(label="흑백영상", command=image_grayscale)
ipmenu.add_command(label="이진화", command=image_bin)
ipmenu.add_command(label="영상뚜렷하게", command=image_sharp)
ipmenu.add_command(label="엠보스", command=image_emboss)
menubar.add_cascade(label="파일",menu=filemenu)
menubar.add_cascade(label="영상처리",menu=ipmenu)
window.config(menu=menubar)
window.mainloop()