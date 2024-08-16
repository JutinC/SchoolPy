from tkinter import *
from tkinter import messagebox
import os

def screen2():
    frame1.destroy() # remove all the pw check stuff
    root.title("Main Page") # rename window

    Label(root, text="hello").pack()

def check_code():
    code_requestget = code_request.get()
    print(code_requestget)
    if code_requestget == code:
        screen2()
    else:
        messagebox.showwarning("Error", "Code is incorrect")

def mainscreen():
    global root, code, code_request, frame1
    code = "1234"
    root = Tk()
    root.title("Passwords")
    root.geometry("260x230")
    root.resizable("False","False")
    frame1 = Frame(root) # create a Frame to hold pw check components
    frame1.pack()

    code_request = StringVar()

    label1 = Label(frame1, text="Welcome - Enter Code", width="40", height="3", background="SpringGreen3")
    label1.pack()
    Label(frame1, text="").pack()

    enter_code = Entry(frame1, width="20", textvariable=code_request)
    enter_code.pack()
    Label(frame1, text="").pack()

    continue_button = Button(frame1, text="Continue", width="16", command=check_code)
    continue_button.pack()

    root.mainloop()

mainscreen()