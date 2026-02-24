from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("500x500")
root.title("The book of addresses")

contacts = {}

Output_listbox_thingy = Listbox(root,width=30,height=20)
Update_button = Button(root,text="Update now",padx=15,pady=15)
Edit_button = Button(root,text="Edit Now",padx=15,pady=15)
Save_button = Button(root,text="Save",padx=15,pady=15)
Delete = Button(root,text="Delete",padx=15,pady=15)
Name = Label(root,text="Name:",pady=1)
Address = Label(root,text="Address:",pady=1)
Mobile = Label(root, text="Mobile:")
Email = Label(root,text="Email:")
Birthday = Label(root,text="Birthday:",pady=1)
Name_text = Entry(root)
Address_text = Entry(root)
Mobile_text = Entry(root)
Email_text = Entry(root)
Birthday_text = Entry(root)

def Save():
    contacts[Name]



Save_button.config(command=Save)

Output_listbox_thingy.grid(row=0,column=0,rowspan=10)
Name.grid(row=0,column=1)
Name_text.grid(row=0,column=2)
Address.grid(row=1,column=1)
Address_text.grid(row=1,column=2)
Mobile.grid(row=2,column=1)
Mobile_text.grid(row=2,column=2)
Email.grid(row=3,column=1)
Email_text.grid(row=3,column=2)
Birthday.grid(row=4,column=1)
Birthday_text.grid(row=4,column=2)
Update_button.grid(row=10,column=3)
Edit_button.grid(row=12,column=0)
Save_button.grid(row=13,column=0)
Delete.grid(row=11,column=0)


root.mainloop()


