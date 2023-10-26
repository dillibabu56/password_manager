from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
               , "a","b","c","d","e","f","g", "h", "i", "j","k","l"	,"m","n","o","p","q","r","s","t","u", "v" ,"w","x","y","z"]
    number=["1","2","3","4","5",'6','7','8','9','0']
    symbols=["@","&","!","$","#","%","^","*","(",")"]

    generate_alphabets = [random.choice(alphabets) for _ in range(random.randint(8,10))]
    generate_numbers = [random.choice(number) for _ in range(random.randint(2, 4))]
    generate_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password=generate_alphabets + generate_numbers + generate_symbols
    random.shuffle(password)
    generated_password="".join(password)
    input_password.insert(0,generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website=input_website.get()
    email = input_email.get()
    password= input_password.get()
    json_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Empty websiteand password",message=f"You entered empty message: \n"
                                                 f"email: {email} \n password: {password} \n "
                                                 f"is that ok to save this details?")
    try:
        with open ("data.json","r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        with open("data.json","w") as data_file:
            json.dump(json_data,data_file,indent=4)
    else:
        data.update(json_data)
        with open("data.json","w") as data_file:
            json.dump(data,data_file,indent=4)
    finally:
        input_website.delete(first=0,last=50)
        input_password.delete(first=0,last=32)


# -----------------------------------------------SEARCH---------------------------------------------------#
def search():
    website = input_website.get()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="error", message="no file is exist")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="Searched_data",message=f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="error",message=f"the search file {website} is not exist")

# ---------------------------- UI SETUP ------------------------------- #

windows=Tk()
windows.config(padx=50,pady=50)
windows.minsize(height=500,width=700)
windows.title("password Manager")

label_website=Label(text="Web Site name: ",font=("arial",24,"bold"))
label_website.grid(column=1,row=1)

input_website=Entry(width=32)
input_website.grid(column=2,row=1)
input_website.focus()

label_email=Label(text="Email/UserName : ",font=("arial",24,"bold"))
label_email.grid(column=1,row=2)

input_email=Entry(width=52)
input_email.grid(column=2,row=2,columnspan=2)
input_email.insert(0,"mdillibabu563@gmail.com")

label_password=Label(text="Pass Word : ",font=("arial",24,"bold"))
label_password.grid(column=1,row=3)

input_password=Entry(width=32)
input_password.grid(column=2,row=3)

button_generate=Button(text="Generate Password", command=generate_password)
button_generate.grid(column=3,row=3)

button_add=Button(text="ADD", width=45, command=save_password)
button_add.grid(column=2,row=4,columnspan=2)

button_search=Button(text="Search",width=15,command=search)
button_search.grid(column=3,row=1)

canvas=Canvas(height=200,width=200,highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100,110,image=img)
canvas.grid(column=2,row=0)



windows.mainloop()