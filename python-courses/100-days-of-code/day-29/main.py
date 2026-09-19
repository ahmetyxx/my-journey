import tkinter as tk
import csv
from tkinter import END, messagebox
import random

FONT="Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters+numbers+symbols) for _ in range(nr_letters+nr_numbers+nr_symbols)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website=website_entry.get()
    mail=mail_entry.get()
    password=password_entry.get()
    
    if len(website)!=0 and len(password)!=0:

    
        is_confirmed=messagebox.askokcancel(
            title="are you sure?",
            message=f"following information will be saved:\n"
                    f"website: {website}\n"
                    f"mail: {mail}\n"
                    f"password: {password}"
        )
        if is_confirmed:
            with open("passwords.csv",mode="a",newline="") as file:
                writer=csv.writer(file)
                writer.writerow([website,mail,password])
            
            website_entry.delete(0, 'end') 
            password_entry.delete(0, 'end') 
    else:
                messagebox.showerror(
            title="oooopss",
            message="please fill all fields!"
        )
    
    
    
# ---------------------------- UI SETUP ------------------------------- #

window= tk.Tk()
window.config(padx=4,pady=20)
window.title("pasword app")

logo=tk.PhotoImage(file="logo.png")

canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)


#labels
web_lbl=tk.Label(text="Website:")
mail_lbl=tk.Label(text="Email/Username:")
password_lbl=tk.Label(text="Password:",)

web_lbl.grid(column=0,row=1,)
mail_lbl.grid(column=0,row=2)
password_lbl.grid(column=0,row=3)

#entrys
website_entry=tk.Entry(window,width=45)
website_entry.focus()
mail_entry=tk.Entry(window,width=45)
mail_entry.insert(0,"ahmetcanisik375@gmail.com")
password_entry=tk.Entry(window,width=30)

website_entry.grid(column=1,row=1,columnspan=2,sticky="w")
mail_entry.grid(column=1,row=2,columnspan=2,sticky="w")
password_entry.grid(column=1,row=3,columnspan=1,sticky="w")

#buttons
add_button=tk.Button(text="add",width=60,command=save_pass)
generate_button=tk.Button(text="Generate Password",width=14,command=generate_password)
add_button.grid(column=0,row=4,columnspan=3,sticky="w")
generate_button.grid(column=2,row=3,sticky="w")




window.mainloop()