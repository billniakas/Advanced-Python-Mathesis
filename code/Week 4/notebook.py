# Notebook

import tkinter as tk
from tkinter import ttk
import random

class MyNotebook():
    def __init__(self, note, name, color):
        self.note = note
        self.f = ttk.Frame(self.note)  
        self.f.pack(expand=True, fill='both', padx=1, pady=1)
        self.l = tk.Label(self.f, text='ένα ακόμη σημειωματάριο', bg=color, font='Arial 24')
        self.l.pack(expand=True, fill='both', padx=1, pady=1)
        self.note.add(self.f, text=name)

class App():
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x800+100+100')
        self.note = ttk.Notebook(self.root)
        self.note.pack(expand=True, fill='both', padx=1, pady=1)
        r = lambda : random.randint(0,255)
        mynotebooks =[]
        for name in ['πρώτο', 'δεύτερο', 'τρίτο', 'τέταρο']:
            mynotebooks.append(MyNotebook(self.note, name, '#{:02X}{:02X}{:02X}'.format(r(),r(),r())))

root = tk.Tk()
App(root)
root.mainloop()
