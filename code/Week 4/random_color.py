#Απλό παράδειγμα με random color

import tkinter as tk
import random

class App():
    def __init__(self, root):
        self.root = root
        self.font = 'Arial 40'
        self.root.title('Παράδειγμα 1')
        self.widgets()
    def widgets(self):
        # τυχαίο χρώμα
        r = lambda : random.randint(0,255)
        color = '#{:02X}{:02X}{:02X}'.format(r(), r(), r())
        self.l = tk.Label(self.root, text='Καλημέρα σας!', font =self.font, bg=color)
        print(color)
        self.l.pack()

root = tk.Tk() # αρχικό παράθυρο
App(root)
root.mainloop()

