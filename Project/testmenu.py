from tkinter import *

s = 0

def main() :
    global s
    s += 1

root = Tk()
root.title('---| Project Thai Map |---')
Label(root ,text = "Welcome To Count Map").pack()
Button(root, text='start', command=main()).pack()

def start() :
    global s
    if s >= 1 :
        Label(root, text='How many place you want to go ?? ').pack()
        Button(root, text="1").pack()
        Button(root, text="2").pack()
        Button(root, text="3").pack()
root.mainloop()