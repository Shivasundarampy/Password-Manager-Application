from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
    pyperclip.paste()
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ENTRY ------------------------------- #


def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            new_data = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="No data found!", )
    except KeyError:
        messagebox.showinfo(title=f"Error", message="Please enter something to search!")

    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {new_data['email']} "
                                                        f"\nPassword: {new_data['password']}")
    finally:
        if messagebox.OK:
            username_entry.delete(0, END)
            username_entry.insert(0, f"{new_data['email']}")
            password_entry.insert(0, f"{new_data['password']}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "sshiva227@gmail")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

password_generate = Button(text="Generate Password", command=generate_password)
password_generate.grid(column=2, row=3)

add_button = Button(width=44, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=14, text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()
