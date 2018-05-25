# παράδειγμα listbox (απαιτεί το αρχείο fruit.txt)

import tkinter as tk
class App():
    def __init__(self, root):
        self.root = root
        self.fnt = 'Arial 30'
        self.root.title("Παράδειγμα listbox")
        self.f1 =tk.Frame(self.root)
        self.f1.pack(side='top', expand=True, fill='both')
        # δημιουργία listbox και συνδεδεμένης μπάρας κύλλησης
        self.sbar = tk.Scrollbar(self.f1)
        self.list = tk.Listbox(self.f1, width=30, height=10, font=self.fnt)
        self.list.config(yscrollcommand=self.sbar.set) # σύνδεσε λίστα με μπάρα κύλλησης sbar
        self.sbar.config(command=self.list.yview) # σύνδεσε μπάρα κύλλησης με λίστα list
        self.sbar.pack(side='right', expand=True, fill='y')
        self.list.pack(expand=True, fill='both')
        # δημιουργία entry box
        self.entry = tk.Entry(self.root, width=30, bg='yellow', font = self.fnt)
        self.entry.config(fg='grey50')
        self.entry.pack(side='bottom', expand=True, fill='both')
        # επιλογή
        self.list.bind('', self.get_list)
        # γέμισε το Listbox
        self.fill_box()
    def fill_box(self):
        # γέμισε το listbox με δεδομένα
        self.entry.insert(0, 'Επιλέξτε από τη λίστα')
        for line in open('fruit.txt', 'r', encoding='utf-8'):
            if line[0] == '\t':
                self.list.insert('end', line.strip())
    def get_list(self, event):
    # Διάβασε την επιλογή από το listbox και βάλε το αποτέλεσμα σε Entry
        index = self.list.curselection()[0] # get selected line index
        seltext = self.list.get(index) # η επιλογή του δείκτη index
        self.entry['fg'] = 'black'
        self.entry.delete(0, 50) # διάγραψε κείμενο του entry
        self.entry.insert(0, seltext) # εμφάνισε το επιλεγμένο

root = tk.Tk()
app =App(root)
root.mainloop()
