# TreeView

import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self, root):
        tree = ttk.Treeview(root)
        tree["columns"]=("one","two")
        tree.column("one", width=100 )
        tree.column("two", width=100)
        tree.heading("one", text="column A")
        tree.heading("two", text="column B")
        # εισαγωγή εγγραφών
        tree.insert("", 0, text="Line 1", values=("1A", "1B"))  # εισαγωγή πρώτου επιπέδου

        id2 = tree.insert("", "end", text="Dir 2")
        tree.insert(id2, "end", text="sub dir 2", values=("2A", "2B"))

        id3 = tree.insert(id2, "end", text="sub dir 3", values=("3A", "3B"))
        tree.insert(id3, "end", text="sub dir 4", values=("4A", "4B"))

        tree.insert("", 3, iid="dir5", text="Dir 5")
        tree.insert("dir5", 3, text=" sub dir 6", values=("6A", " 6B"))

        tree.pack()

root = tk.Tk()
App(root)
root.mainloop()

