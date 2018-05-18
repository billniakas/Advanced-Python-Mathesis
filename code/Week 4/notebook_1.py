from tkinter import ttk
import tkinter as tk
mybook = {'1.Chapter':"the text of 1st chapter",  '2.Chapter':"the text of 2nd chapter"}
root=tk.Tk()
root.geometry('300x300')
nb = ttk.Notebook(root)
for i in sorted(mybook):
    l = tk.Label(nb, text=mybook[i])
    l.pack(expand=1, fill='both')
    nb.add(l, text=i)
nb.pack(expand=1, fill='both')
root.mainloop()

