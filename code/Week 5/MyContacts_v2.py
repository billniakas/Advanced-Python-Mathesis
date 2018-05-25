# Σύνδεση επαφών με βάση δεδομένων

import tkinter as tk
import os
import shelve
import random

## κλάση Contact σύνδεση με βάση δεδομένων

class Contact():
    ''' κλάση επαφών με όνομα και τηλέφωνο
        μια μεταβλητή κλάσης theContacts'''
    theContacts = {}
    db ='contacts'
    @staticmethod
    def count_records():
        with shelve.open(Contact.db) as db:
            return len(db.keys())
    @staticmethod
    def retrieve_contacts(term = ''):
        retrieved_contacts = []
        Contact.theContacts = {}
        with shelve.open(Contact.db) as db:
            for key in db.keys():
                if not term or term.lower() in key.lower():
                    Contact(db[key].name, db[key].number)
        #print retrieved contacts
        for c in sorted(Contact.theContacts, key=lambda x : x.split()[-1]):
            if term:
                if term.lower() in c.lower():
                    #print(Contact.theContacts[c])
                    retrieved_contacts.append(Contact.theContacts[c])
            else:
                #print(Contact.theContacts[c])
                retrieved_contacts.append(Contact.theContacts[c])
        return retrieved_contacts
    @staticmethod
    def create_contacts(size):
        '''δημιουργεί τυχαίο δείγμα επαφών - καμιά σχέση με την πραγματικότητα'''
        dir = '../data'
        act_names_files = [os.path.join(dir, x) for x in ('gr_actresses.txt', 'gr_actors.txt')]
        names = []
        for f in act_names_files:
            with open(f, 'r', encoding='utf-8') as fin:
                for name in fin:
                    if len(name) > 2:
                        if len(name.split()) > 1:
                            names.append(name.strip())
        # Select class_size names from names list
        if size < len(names):
            contact_names = random.sample(names, size)
        else:
            contact_names = names
        for contact in contact_names:
            number = str(random.randint(6900000000, 6999999999))
            Contact(contact, number, new=True)
    @staticmethod
    def del_contact(id):
        if id in Contact.theContacts:
            del Contact.theContacts[id]
            with shelve.open(Contact.db) as db:
                if id in db.keys():
                    del db[id]

    def __init__(self, name, number='', new=False): #  μέθοδος δημιουργός επαφών
        self.name = name.strip()
        self.number = number.strip()
        Contact.theContacts[self.name] = self
        if new: self.insert()
    def insert(self):
        with shelve.open(Contact.db) as db:
            db[self.name] = self
    def set_number(self, number):
        self.number = number
        with shelve.open(Contact.db) as db:
            if self.name in db.keys():
                db[self.name] = self
    def __repr__(self): # μέθοδος εκτύπωσης επαφών
        return self.name + ': \t' + self.number

##
class App():
    def __init__(self, root):
        self.root = root
        self.root.title('MyContacts')
        self.fnt ='Arial 20'
        self.widgets()
        self.initialize_db()
        self.contacts = Contact.retrieve_contacts()
        self.fill_box()
    def initialize_db(self):
        if not os.path.isfile('contacts.db'):
            Contact.create_contacts(100)
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
                self.list.insert(pos, repr(cont))

root = tk.Tk()
App(root)
root.mainloop()

