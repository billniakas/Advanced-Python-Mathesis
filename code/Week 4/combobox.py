
import tkinter as tk
from tkinter import ttk
# Παράδειγμα combobox

class MyApp(tk.Frame):
    def __init__(self, root):
        self.root = root
        root.title('Παράδειγμα combo')
        self.label = tk.ttk.Label(self.root, text='Διάλεξε πιάτο:')
        self.label.pack(expand=1, fill='both')
        self.combo()
    def combo(self):
        self.box_value = tk.StringVar()
        self.box = ttk.Combobox(self.root, textvariable=self.box_value, state = 'readonly',
                                values = ('Πίτσα', 'Μακαρονάδα', 'Ριζότο', "Μπιφτέκι"))
        self.box.bind("<<ComboboxSelected>>", self.newselection)
        self.box.current(0)
        self.box.pack(expand=1, fill='both')
    def newselection(self,event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)

root = tk.Tk()
MyApp(root)
root.mainloop()


