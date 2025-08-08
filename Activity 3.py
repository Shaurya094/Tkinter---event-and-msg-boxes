from tkinter import Tk, Label, Button, Entry, Frame

def F_to_C():
    """Convert the balue for Fahrenhiet to Celsius and insert the result into lbl_result."""
    f = ent_temp.get()
    c = (5/9) * (float(f) - 32)
    lbl_result["text"] = f"{round(c, 2)} \N{DEGREE CELSIUS}"

w = Tk()
w.title("Fahrinheit to Celsius converter")

frm_entry = w.Frame(master=w)
ent_temp = w.Entry(master=frm_entry, width=10)
lbl_temp = w.Entry(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row = 0, column = 0, sticky = "e")
lbl_temp.grid(row = 0, column = 1, sticky = "w")

btn_convert = w.Button(
    master=w,
    text = "-->",
    command=F_to_C
)
lbl_result = w.Label(master=w, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

w.mainloop()