from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = eu_entry.get()
    password = pw_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure the pw/website fields are not left empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\n Password:"
                                               f" {password} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Courier", 12, "bold"))
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_label = Label(text="Email/Username:", font=("Courier", 12, "bold"))
email_username_label.grid(column=0, row=2)

eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)
eu_entry.insert(0, "abrar.ali75@gmail.com")

pw_label = Label(text="Password:", font=("Courier", 12, "bold"))
pw_label.grid(column=0, row=3)

pw_entry = Entry(width=25)
pw_entry.grid(column=1, row=3)

generate_but = Button(text="Generate Password", font=("Courier", 10, "bold"), command=generate_password)
generate_but.grid(column=2, row=3)

add_but = Button(text="Add", font=("Courier", 10, "bold"), width=36, command=save)
add_but.grid(column=1, row=4, columnspan=2)

window.mainloop()
