# Style

import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):       
        s = ttk.Style().configure('button.TButton', bg='yellow', font='Arial 30')
        root.title('Παράδειγμα 6')
        self.root = root
        self.button = ttk.Button(self.root, style='button.TButton', text='  show text  ', command=self.showText)
        self.button.pack(fill='both', expand=1)
        self.entry = tk.Entry(self.root, font='Arial 30', width=20) #το πλαίσιο εισαγωγής κειμένου
        self.entry.pack(fill='both', expand=1)
    def showText(self): # Χειριστής γεγονότος επιλογής πλήκτρου b 
        text = self.entry.get() # πάρε το κείμενο που έχει εισαχθεί στο πλαίσιο κειμένου
        print(text) # τύπωσέ το


root = tk.Tk()
MyApp(root)
root.mainloop()
