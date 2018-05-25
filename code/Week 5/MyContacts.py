import tkinter as tk
import os

class App():
    def __init__(self, root):
        self.root = root
        self.root.title('MyContacts')
        self.fnt ='Arial 20'
        self.widgets()
        self.contacts = []
        self.fill_box()
    def widgets(self):
        self.f1 = tk.LabelFrame(self.root, text='επαφές')
        self.f1.pack(expand=True, fill='both', padx=2, pady=2)
        self.sbar = tk.Scrollbar(self.f1)
        self.sbar.pack(side='right', fill='y')
        self.list = tk.Listbox(self.f1, relief = 'sunken', font=self.fnt,
                               bg='lightyellow', height=30, width=30)
        self.list.pack(expand=True, fill='both')
        self.list.config(yscrollcommand=self.sbar.set)
        self.sbar.config(command=self.list.yview)
        # δημιουργία αναδυόμενου μενού
        self.context = tk.Menu(self.root, font=self.fnt)
        self.root.config(menu=self.context)
        self.context.add_command(label='Τροποποίηση ...', command=self.modify)
        self.context.add_command(label='Διαγραφή ...', command=self.delete)
        self.root.bind('<2>', self.post_menu)

    def post_menu(self, event):
        self.context.post(event.x_root, event.y_root)

    def modify(self): pass
    def delete(self): pass

    def fill_box(self):
        self.list.delete(0,'end')
        if self.contacts:
            for pos, cont in enumerate(self.contacts):
                self.list.insert(pos, cont)
        else: # διάβασε επαφές από το αρχείο gr_actors.txt
            pos = 0
            for contact in open('../data/gr_actors.txt', 'r', encoding='utf-8'):
                if len(contact.strip()) > 1:
                    self.list.insert(pos, contact.strip())
                    self.contacts.append(contact.strip())

root = tk.Tk()
App(root)
root.mainloop()
