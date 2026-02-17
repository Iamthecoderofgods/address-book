from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("The book of addresses")

Output_listbox_thingy = Listbox(root,width=20,height=10)
Update_button = Button(root,text="Update now",padx=10,pady=10)
Edit_button = Button(root,text="Edit Now",padx=10,pady=10)
Save_button = Button(root,text="Save",padx=13,pady=13)

Output_listbox_thingy.grid(row=0,column=0)
Update_button.grid(row=10,column=0)
Edit_button.grid(row=11,column=0)
Save_button.grid(row=12,column=0)
root.mainloop()


