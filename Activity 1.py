from tkinter import Tk, Label, Button

window = Tk()
window.title("Event")
window.geometry("100x100")

def key(event):
    """Print the character associated to the key pressed"""
    print(event.char)

window.bind("<Key>", key)

def click(event):
    print("\nThe button was clicked")

button = Button(text = "Click me")
button.pack()

button.bind("<Button - 1>", click)

window.mainloop()