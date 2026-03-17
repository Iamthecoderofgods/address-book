from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

root = Tk()
root.geometry("500x600")
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

def Update():
    name = Name_text.get()
    
    if not name:
        messagebox.showwarning("Error!!","you are a stupid idiot for putting no name in the box you stupid idoit")
    
        return

    Name_text.delete(0,END)

    Address_text.delete(0,END)

    Mobile_text.delete(0,END)

    Email_text.delete(0,END)

    Birthday_text.delete(0,END)
    


    contacts[name] = {"Address":Address_text.get(),
                      "Mobile":Mobile_text.get(),
                      "Email":Email_text.get(),
                      "Birthday":Birthday_text.get()}
    
    if name not in Output_listbox_thingy.get(0,END):
       Output_listbox_thingy.insert(END,name) 

def edit():
    selection = Output_listbox_thingy.curselection()

    if not selection:
        messagebox.showwarning("Error!!","you are a stupid idiot for not slecting. you have to select the person you stupid idiot",)
        
        return
    name = Output_listbox_thingy.get(selection[0])
    deatils = contacts[name]
    Name_text.delete(0,END)
    Name_text.insert(0,name)

    Address_text.delete(0,END)
    Address_text.insert(0,deatils["Address"])

    Mobile_text.delete(0,END)
    Mobile_text.insert(0,deatils["Mobile"])

    Email_text.delete(0,END)
    Email_text.insert(0,deatils["Email"])

    Birthday_text.delete(0,END)
    Birthday_text.insert(0,deatils["details"])

def deletes():
    selection = Output_listbox_thingy.curselection()
    
    if not selection:
        messagebox.showwarning("Error!!","you are a stupid idiot for not slecting. you have to select the person you stupid idiot",)
        
        return
    name = Output_listbox_thingy.get(selection[0])
    del contacts[name]
    Output_listbox_thingy.delete(selection[0])









    




Edit_button.config(command=edit)
Update_button.config(command=Update)
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


