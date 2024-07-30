from tkinter import *
import tkinter as tk
from tkinter import messagebox

#create a tkinter window
window=tk.Tk()
window.geometry("800x500")
window.title("PhoneBook")
window.config(bg="#d7acfa")

#create a list to store contack information
contacts=[]

#Function to add a new contact
def add_contact():
    name=name_entry.get().strip()
    phone=phone_entry.get()
    email=email_entry.get()
    if name!="":
        contacts.append((name,phone,email))
        messagebox.showinfo("Save", "Contact Saved Successfully")
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    update_listbox()

    #Function to remove a selected contact
def remove_contacts():
    selected = contacts_listbox.curselection()
    if selected:
        index=selected[0]
        del contacts[index]
        update_listbox()
        messagebox.showinfo("Deleted","Contact Deleted Successfully")

#Function to display contact details
def display_contacts():
    for contact in contacts:
        messagebox.showinfo("Details","Name  :   "+contact[0]+
                            '\n'+"Phone  :  "+contact[1]+
                            '\n'+"Email  :  "+contact[2])
        

#Function to update the contact listbox
def update_listbox():
    contacts_listbox.delete(0,tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact[0])


#Heading PHONEBOOK Label
heading_label=tk.Label(window,
                       text="PhoneBook",font=("snap itc",30,"bold", "underline"),
                       foreground="white",
                       bg="#d7acfa")
heading_label.place(x=300,y=3)

#Create labels and enter fields for name, phone and email
name_label=tk.Label(window,
                    text="Name:",
                    font=("castellar",20,"bold"),
                    foreground="white",
                    bg="#d7acfa")
name_label.grid(row=0,column=0)
name_label.place(x=80,y=70)

name_entry=tk.Entry(window,
                    font=("century",17,"bold"),width=20, fg="black", bg="#f0afcd")
name_entry.grid(row=0,column=1)
name_entry.place(x=200,y=70)

phone_label=tk.Label(window,
                    text="Phone:",
                    font=("castellar",20,"bold",),
                    foreground="white",
                    bg="#d7acfa")
phone_label.grid(row=1,column=0)
phone_label.place(x=80,y=120)

phone_entry=tk.Entry(window,
                    font=("century",17,"bold"),width=20,fg="black", bg="#f0afcd")
phone_entry.grid(row=1,column=1)
phone_entry.place(x=200,y=120)


email_label=tk.Label(window,
                    text="Email:",
                    font=("castellar",20,"bold"),
                    foreground="white",
                    bg="#d7acfa")
email_label.grid(row=2,column=0)
email_label.place(x=80,y=170)

email_entry=tk.Entry(window,
                    font=("century",17,"bold"),width=20,fg="black", bg="#f0afcd")
email_entry.grid(row=2,column=1)
email_entry.place(x=200,y=170)


#Create buttons to add a new contact, remove a selected contact and display contact details of selected contact
add_button=tk.Button(window,
                     text="ADD CONTACT",
                     command=add_contact,
                     font=("Tahoma",13,"bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activeforeground="white",
                     background="green",
                     activebackground="dark green")
add_button.grid(rowspan=1)
add_button.place(x=50,y=280)

remove_button=tk.Button(window,
                     text="REMOVE CONTACT",
                     command=remove_contacts,
                     font=("Tahoma",13,"bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activeforeground="white",
                     background="red",
                     activebackground="dark red")
remove_button.grid(rowspan=1)
remove_button.place(x=50,y=330)


display_button=tk.Button(window,
                     text="DISPLAY CONTACT",
                     command=display_contacts,
                     font=("Tahoma",13,"bold"),
                     relief="raised",
                     borderwidth=4,
                     width=18,
                     activeforeground="white",
                     background="light blue",
                     activebackground="dark blue")
display_button.grid(rowspan=1)
display_button.place(x=50,y=380)

conhead_label=tk.Label(window,
                       text="CONTACT LIST",
                       font=("ravie", 20, "bold"),
                       relief="raised",
                       foreground="white",
                       bg="#d085f2")
conhead_label.place(x=470,y=220)


#Create Listbox to display contacts
contacts_listbox=tk.Listbox(window,
                            font=("century",12),width=40)
contacts_listbox.place(x=415,y=270)



#Start the main window event
                    

window.mainloop()