import tkinter
from tkinter import*
from tkinter import messagebox

window = tkinter.Tk()
window.title('A simple GUI')
window.geometry('250x100')

def greet():
    tkinter.messagebox.showinfo(" ","Welcome to the first GUI program")

tuxt = Label(window,text='This is our first GUI!',font=('Times New Roman','12'))
tuxt.pack()

btn1 = Button(window,text='Greet',font=('Times New Roman','12'),command=greet)
btn1.pack()

btn2 = Button(window,text='Close',font=('Times New Roman','12'))
btn2.pack()

window.mainloop()