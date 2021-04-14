# -*- coding: utf-8 -*-
"""
examples from: https://likegeeks.com/python-gui-examples-tkinter-tutorial/ 
"""


import numpy as np
from tkinter import *
 
window = Tk() 
window.title("Welcome")
window.geometry('400x600')

# 1st func 
n = 0
lbl = Label(window, text="Extract continuous pages")
lbl.grid(column=0, row=n)

ent = Entry(window, width=8)    # textbox to enter start/stop page numbers of a pdf file
ent.grid(column=1, row = n)
 
def clicked(): 
    #lbl.configure(text="1st button clicked !!")

    Fst = int(ent.get())    
    print(ent.get())
    print(Fst[0])
    print(Fst[2])
    n0 = int(Fst[0])
    n1 = int(Fst[2])
    for i in range(n0,n1,np.sign(n1-n0)):
        print(i)
 
btn = Button(window, text="1st button", command=clicked)
btn.grid(column=2, row=n)



# 2nd func 
n += 1
lbl_ = Label(window, text="Extract multiple selected pages")
lbl_.grid(column=0, row=n)
 
def clicked_(): 
    lbl_.configure(text="2nd button clicked !!")
 
btn_ = Button(window, text="2nd button", command=clicked_)
btn_.grid(column=1, row=n)


# 3rd func 
n += 1
lbl__ = Label(window, text="Combine multi files")
lbl__.grid(column=0, row=n)
 
def clicked__(): 
    lbl__.configure(text="3rd button clicked !!")
 
btn__ = Button(window, text="3rd button", command=clicked__)
btn__.grid(column=1, row=n)



# entry box
n += 1
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    

Label(window, 
         text="First Name").grid(row=n)
Label(window, 
         text="Last Name").grid(row=n+1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=n, column=1)
e2.grid(row=n+1, column=1)

Button(window, 
          text='Quit', 
          command= window.quit).grid(row=n+2, 
                                    column=0,
                                    pady=4)
Button(window, 
          text='Show', command=show_entry_fields).grid(row=n+2, 
                                                       column=1,                                                        
                                                       pady=4)



# combo-box
from tkinter.ttk import *
n += 4
Label(window, text="Example of Combobox:").grid(column=0,row=n)
combo = Combobox(window)
combo['values']= (1, 2, 3, 5, 8, "Text") 
combo.current(1) #set the selected item 
combo.grid(column=1, row=n)



# check-box
n += 1
Label(window, text="Example of Checkbox:").grid(column=0,row=n)
bchk = BooleanVar()
bchk.set(True) #set check state 
chk = Checkbutton(window, text='Checkbox', var= bchk ) 
chk.grid(column=1, row=n)



# radio-button
from tkinter.ttk import *
n += 1
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
 
Label(window, text="Example of radiobox:").grid(column=0,row=n)
rad1.grid(column=1, row=n) 
rad2.grid(column=1, row=n+1) 
rad3.grid(column=1, row=n+2)


# spin box
n += 3
Label(window, text="Example of spinbox:").grid(column=0,row=n)
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=1,row=n)


# progress bar
n += 1
Label(window, text="Example of progressbar:").grid(column=0,row=n)
bar = Progressbar(window, length=100, style='black.Horizontal.TProgressbar') 
bar['value'] = 30 
bar.grid(column=1, row=n)


# file dialog
n += 1
from os import path
from tkinter import filedialog
Label(window, text="Example of file dialog:").grid(column=0,row=n)
#file = filedialog.askopenfilename()
#file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
#file.grid(column = 1, row = n)



# menu

from tkinter import Menu

 
menu = Menu(window) 
new_item = Menu(menu) 
sav_item = Menu(menu)
new_item.add_command(label='New') 
sav_item.add_command(label="save_as_png")
sav_item.add_separator()
sav_item.add_command(label="save_as_jpg")
menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label="Save", menu=sav_item)
 
window.config(menu=menu)



'''
# notebook
from tkinter import ttk
n = n + 3
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First') 
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1') 
lbl1.grid(column=0, row=n)
 
lbl2 = Label(tab2, text= 'label2') 
lbl2.grid(column=1, row=n)
 
tab_control.pack(expand=1, fill='both')
'''


 
window.mainloop()

