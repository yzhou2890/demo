# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:07:12 2019
@author: yzhou11
see: demo_pdf_editor.py
"""



from tkinter import *
#from tkinter import ttk
 
window = Tk() 
window.title("PDF Editor - extract & combine")
window.geometry('450x300')



#### get all pdf files from a given folder/path
 
from mod_pdf_editor import  pdf_editor_extract_continuous_page  # see mod_pdf_editor.py

import glob

# get all pdf files from a local folder
lpath = "file/"
s = glob.glob(lpath + "*.pdf")
fls = []
print("files in " + lpath + ":" )
for p in s:
    tmp = p.split('\\')
    print(tmp[-1])
    fls.append(  tmp[-1] )

##########################  extract continuous pages   ###################

n = 1
Label(window, text=" ").grid(column=0, row=n) 
Label(window, text=" ").grid(column=0, row=n+1)
Label(window, text=" ").grid(column=0, row=n+2) 

from tkinter.ttk import *
n += 4

# label
Label(window, text="List of pdf files:" ).grid(column=0,row=n)
# combo-box 
combo = Combobox(window, values = fls )
combo.current(0)    
combo.grid(column=1, row=n)

# callback func to trigger extracting pages  
def callback_func_01(): 
    print("\n Extracting pages from " + combo.get() + ":\n")
    x0 = int(input("put a page num to start: \t"))
    x1 = int(input("put a page num to finish: \t"))
    fn = input("put a file name to output: \t")
    
    #print(combo.get()[:-4])
    pdf_editor_extract_continuous_page( pdfpath = lpath, pdfname=combo.get()[:-4], Fstpg=x0, Lstpg=x1, pdfname_out=fn )
    

btn = Button(window, text="Extract continuous pages", command=callback_func_01)
btn.grid(column=2, row=n)


##########################  extract disjoint pages   ###################

from mod_pdf_editor import pdf_editor_extract_multi_page

n += 5
Label(window, text=" ").grid(column=0, row=n) 
Label(window, text=" ").grid(column=0, row=n+1)
Label(window, text=" ").grid(column=0, row=n+2) 

from tkinter.ttk import *
n += 4

# label
Label(window, text="List of pdf files:" ).grid(column=0,row=n)
# combo-box 
cmb = Combobox(window, values = fls )
cmb.current(0)    
cmb.grid(column=1, row=n)

# callback func to trigger extracting pages  
def callback_func_02(): 
    print("\n Extracting disjoint pages from " + cmb.get() + ":\n")
    
    tmp = []
    while(1):
        try:
            x0 = int(input("Enter a page number to extract [start from 1]: \t"))
            tmp.append(x0)    
        except:
            break            

    pdf_editor_extract_multi_page( pdfpath=lpath, pdfname=cmb.get()[:-4], pagelist=tmp, pdfname_out="" )
    print("\t Extract disjoint pages completed.")
    

btn = Button(window, text="Extract disjoint pages", command=callback_func_02)
btn.grid(column=2, row=n)



###################### combine multi files ##############################
n+=4
Label(window, text=" ").grid(column=0, row=n) 
Label(window, text=" ").grid(column=0, row=n+1)
Label(window, text=" ").grid(column=0, row=n+2) 


from mod_pdf_editor import pdf_editor_combine_multi_file
n += 4

# label
lbl = Label(window, text="Combine multi files:")
lbl.grid(column=0, row=n)

txb = Entry(window, width=30 )    # textbox to enter start/stop page numbers of a pdf file
txb.grid(column=1, row = n)
 
def callback_combine(): 
    #lbl.configure(text="1st button clicked !!")
    print("\n Combining pdf files from " + lpath + ":\n")
    
    tmp = txb.get()
    print(tmp)
    
    fls = []
    if(tmp==[]):
    
        while(1):
            x0 = input("\t Enter a pdf file ['q' to stop]: \t")
            
            if( x0 == 'q' ):            
                break
            else:
                fls.append(x0[:-4])                       
    else:
        tmp = tmp.split(',')
        for i in tmp:
            fls.append(i[:-4])
            print(fls)
        
    print("Files to combine:")
    print(fls)    
    

    fn = input("\t Enter name of output: \t")
    
    pdf_editor_combine_multi_file( pdfpath=lpath, pdfname= fls, pdfname_out= fn )
    print("\t Combination completed.")

        
btn = Button(window, text="Combine", command=callback_combine)
btn.grid(column=2, row=n)




############################################################################

window.mainloop()






