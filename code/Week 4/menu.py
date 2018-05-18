# Menu

import tkinter as tk

w = tk.Tk()
w.geometry('300x300')
mb = tk.Menubutton(w, text = 'Μενού')
mb.pack()
m = tk.Menu(mb)
m.add_command(label='Επλογή 1')
m.add_command(label='Επλογή 2')
m.add_command(label='Επλογή 3')
mb.config(menu=m)
w.mainloop()
