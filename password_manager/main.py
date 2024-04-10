from tkinter import *
from tkinter import ttk, messagebox
import pandas
import random
import pyperclip
import json
import os
option = ""


# ---------------------------- SEARCH PASSWORD ------------------------------- #
# enter website, and search which emails are logged in within the website, along with the passw
def search_password():
    # READING FROM A CSV FILE
    # data = pandas.read_csv("password_manager_data.csv")       # if you are saving data in a csv file
    msg = ""
    website = website_entry.get()
    if website == "":
        messagebox.showinfo(message="Please enter website, before searching")

    else:
        with open("data.json", "r") as f:
            data = json.load(f)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            msg += f"Email: {email}, Password: {password}"
        else:
            messagebox.showinfo(message="No emails found registered with the website")
        search_results.config(text=msg)

    # FOR SEARCHING IN A CSV FILE
    # for (index, row) in data.iterrows():    # loop through the dataframes
    #     if row.website == website_entry.get():          # if website found, add to 'msg'
    #         found = True
    #         msg += f"Email: {row.email}, Password: {row.password}\n"
    #
    # if not found:                           # if website doesn't exist, show message 'msg'
    #     messagebox.showinfo(message="No emails found registered with the website")    # dialog
    #
    # search_results.config(text=msg)         # at last display the search results in label


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generate a random password
def generate_password():
    pass_entry.delete(0, END)           # deletes the text in the entry from index 0 to END
    password = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list[:])
    pass_entry.insert(END, string=password)
    pyperclip.copy(password)                # copied to clipboard as soon as the password gets generated


# ---------------------------- SAVE PASSWORD ------------------------------- #
# saves entered details into a csv file whenever "ADD PASSWORD" button is clicked
def save_password():
    global option

    if website_entry.get() == "":
        messagebox.showinfo(message="Website Field Empty!")
    elif email_list_combo.get() == "":
        messagebox.showinfo(message="Email not Selected!")
    elif pass_entry.get() == "":
        messagebox.showinfo(message="Password Field Empty!")
    else:
        decision = messagebox.askyesno(title="Details entered", message=f"These are the details entered:\nWebsite: {website_entry.get()}\nEmail: {option}\nPassword: {pass_entry.get()}\nIs it OK to save these details?")
        if decision:
            # FOR SAVING IN A CSV FILE
            # with open("password_manager_data.csv", "a") as f:
            #     f.write(f"{website_entry.get()},{option},{pass_entry.get()}\n")
            new_data = {
                website_entry.get(): {
                    "email": email_list_combo.get(),
                    "password": pass_entry.get()
                }
            }

            path_to_file = 'data.json'
            if not os.path.exists(path_to_file):            # if file does not exist, create it
                f = open("data.json", "w")
                f.close()

            try:
                with open("data.json", "r") as data_file:   # after file creation read,update,write starts
                    data = json.load(data_file)             # read the old data
                    data.update(new_data)                   # update the old data with new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)    # save the new data

            except json.decoder.JSONDecodeError:            # Occurs when the starting json file is empty
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)        # so we just dump the data

            website_entry.delete(0, END)           # after password saved, empty the fields
            pass_entry.delete(0, END)              # to enable user re-entry

            messagebox.showinfo(message="Password Saved Successfully!")      # DIALOG


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, padx=20, pady=20, bg="white")

# lock image in the middle
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text="Website:", bg="white", pady=10)             # website label
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white", pady=10)        # email label
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:", bg="white", pady=14)               # password label
pass_label.grid(row=3, column=0)
search_results = Label(text="", bg="white", pady=10)                      # search results label
search_results.grid(row=6, column=0, columnspan=3)

# ENTRIES - SINGLE LINE TEXT INPUT
website_entry = Entry(width=40)                                         # website input
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
pass_entry = Entry(width=22)                                            # password input
pass_entry.grid(row=3, column=1)

# ------------------------------------ # ENTER YOUR EMAILS IN THE LIST HERE ----------------------------------------------------------
# COMBOBOX - email list                                               
emails = ["abc@gmail.com", "def@gmail.com"]
# ------------------------------------ # ENTER YOUR EMAILS IN THE LIST HERE ----------------------------------------------------------
email_list_combo = ttk.Combobox(window, values=emails, width=38)
email_list_combo.grid(row=2, column=1, columnspan=2)


def selected_option(event):
    global option
    option = email_list_combo.get()
    # print(option)

email_list_combo.bind("<<ComboboxSelected>>", selected_option)

# BUTTONS
gen_pass_btn = Button(text="Generate Password", width=16, command=generate_password)  # generate password
gen_pass_btn.grid(row=3, column=2)
add_btn = Button(text="Add Password", width=40, command=save_password)                # add password
add_btn.grid(row=4, column=1, columnspan=2)
search_pass_btn = Button(text="Search Password", width=40, command=search_password)   # search password
search_pass_btn.grid(row=5, column=1, columnspan=2)

window.mainloop()
