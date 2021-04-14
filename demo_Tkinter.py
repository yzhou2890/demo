


import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk
root = tk.Tk()
root.title("Welcome")
root.geometry('200x300')

root.title("Hello")
tk.Button(root, text="test").pack()


tk.mainloop()












