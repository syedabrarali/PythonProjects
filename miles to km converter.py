from tkinter import *


def km_output():
    km3 = float(input_km.get())
    km4 = km3 * 1.609
    km_label.config(text=km4)


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=250, height=125)
window.config(padx=20, pady=20)


input_km = Entry()
input_km.grid(column=1, row=0)
input_km.config(width=8)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

iseq_label = Label(text="is equal to", font=("Arial", 12, "bold"))
iseq_label.grid(column=0, row=1)
iseq_label.config(padx=5, pady=5)

km_label = Label(text="0", font=("Arial", 12, "bold"))
km_label.grid(column=1, row=1)
km_label.config(padx=5, pady=5)

km2_label = Label(text="Km", font=("Arial", 12, "bold"))
km2_label.grid(column=2, row=1)
km2_label.config(padx=5, pady=5)

calc_button = Button(text="Calculate", command=km_output, font=("Arial", 12, "bold"))
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)

window.mainloop()