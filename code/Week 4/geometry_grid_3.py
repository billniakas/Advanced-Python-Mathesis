
# grid παράδειγμα 3

import tkinter as tk
w = tk.Tk()
f = 'Consolas 30'
for i in range(3):
    l=tk.Label(text=str(i), font=f, width=10, height=5, borderwidth=1, relief='sunken')
    l.grid(row=0,column=i)
for i in range(3):
    l=tk.Label(text=str(i), font=f, width=10, height=5, borderwidth=1, relief='sunken')
    l.grid(row=1,column=i)
l=tk.Label(text='5', bg='yellow', font=f, width=10, height=5, borderwidth=1, relief='sunken')
l.grid(row=0,column=5, rowspan=2)
w.mainloop()


