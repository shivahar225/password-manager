from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',' I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbol = ['!','@','#','$','%','^','&','*','(',')''_']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbol) for _ in range(randint(2, 4))]

    password_list = password_letters +password_numbers +password_symbols
    shuffle(password_list)

    password = "".join((password_list))
    password_entry.insert(0, password)

    print(password)


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title=" type ", message="please make sure you havent'n left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the datails entered: \n email: {email}" f"\n password:{password}\n is it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)

window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
#logo_img = PhotoImage(file="image.png")
#canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="website:")
website_label.grid(row=1, column=0)
email_label = Label(text="email/username:")
email_label.grid(row=2 ,column=0 )
passward_label = Label(text="password:")
passward_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1)
email_entry.insert(0,"shivahar225@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
