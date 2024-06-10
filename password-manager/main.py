import tkinter as tk
from tkinter import messagebox
from combinations import letters, numbers, symbols
import random

window = tk.Tk()
window.title("Password Manager")


def generatePassword():
    """Generates a random password from letters, symbols and numbers"""

    password_entry.delete(0, tk.END)

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_combination = [random.choice(letters)  for _ in range(nr_letters)]
    number_combination = [random.choice(numbers)  for _ in range(nr_numbers)]
    symbol_combination = [random.choice(symbols)  for _ in range(nr_symbols)]

    password_list = letter_combination + number_combination + symbol_combination
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)


def saveData():
    """Saves the data into the text file"""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    #input validation
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid input", message="Some of the fields are empty")
        return

    response = messagebox.askokcancel(title="Verify!", message=f"Below are the details you mentioned: \n Email: {username}\n Password: {password}\n Is it OK to contiue?")
    if response:
        with open("data.txt", 'a') as f_ptr:
            f_ptr.write(f"{website}, {username}, {password}\n")
        
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)




#-------------------------GUI------------------------------------------#
#Grid layout design
window.rowconfigure(0, weight=5, uniform='a')
window.rowconfigure((1,2,3,4,5), weight=1, uniform='a')
window.columnconfigure((0,1,2) , weight=1, uniform='a')


#Creating widgets
canvas = tk.Canvas(window, height=200, width=200)
logo = tk.PhotoImage(file='images/logo.png')
canvas.create_image(100, 100, image=logo)

website_label = tk.Label(window , text= "Website:")
website_entry = tk.Entry(window, width=35)
website_entry.focus()

username_label = tk.Label(window, text="Email/Username:")
username_entry = tk.Entry(window, width=35)

password_label = tk.Label(window, text="Password:")
password_entry = tk.Entry(window, width=35)

generate_password_button = tk.Button(window, text="Generate Password", width=36, command=generatePassword)
add_to_file_button = tk.Button(window, text="Add", width=36, command=saveData)


#putting widgets on the window
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0, sticky='e')
website_entry.grid(row=1, column=1, columnspan=2)
username_label.grid(row=2, column=0, sticky='e')
username_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0, sticky='e')
password_entry.grid(row=3, column=1, columnspan=2)
generate_password_button.grid(row=4, column=1, columnspan=2)
add_to_file_button.grid(row=5, column=1, columnspan=2)


window.mainloop()