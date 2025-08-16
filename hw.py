from tkinter import Tk, Label, Button, Text, END, Entry
import tkinter as tk
screen = Tk()
screen.title = ("Inches to cm")
screen.geometry = ('400x300')
root = tk.Tk()
tb = Text(height=3)

inches = Label(text= "Inches:", fg = "red", bg = "grey", height = 1, width = 30)
inchesE = Entry()

def convert():
    tb.delete('1.0', END)
    I = float(inchesE.get())
    cm = I * 2.54
    tb.insert(END, f"{I} inches, in centimeters, is {cm} cm.")

btn = Button(text = "Calulate", command=convert, height=1, bg="#2F6438", fg = 'white')

inches.pack()
inchesE.pack()
btn.pack()
tb.pack()

screen.mainloop()