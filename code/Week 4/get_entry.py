# get entry

import tkinter as tk
class MyApp():
    def __init__(self, root):
        self.fnt = 'Arial 30'
        root.title('Παράδειγμα 3')
        self.root = root
        self.widgets()
    def widgets(self):
        self.button = tk.Button(self.root, text="  τύπωσε entry  ", font = self.fnt, command=self.showText)
        self.button.pack(fill='both', expand=1)
        self.entry = tk.Entry(self.root, font= self.fnt, width= 20, bg='lightgreen', fg='blue') # το πλαίσιο εισαγωγής κειμένου
        self.entry.pack(fill='both', expand=1)
    def showText(self): # χειριστής γεγονότος επιλογής πλήκτρου b
        text = self.entry.get() # πάρε το κείμενο που έχει εισαχθεί στο πλαίσιο κειμένου
        print(text) # τύπωσε το

root = tk.Tk()
myapp = MyApp(root)
root.mainloop()
