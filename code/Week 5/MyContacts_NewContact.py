# Εισαγωγή νέων επαφών

import tkinter as tk
import os
import random
import shelve

class Contact():
    ''' κλάση επαφών με όνομα και τηλέφωνο
    --> μεταβλητή κλάσης theContacts'''
    theContacts = {}
    db ='contacts'
    @staticmethod
    def count_records():
        with shelve.open(Contact.db) as db:
            return len(db.keys())
    @staticmethod
    def retrieve_contacts(term = ''):
        Contact.theContacts = {}
        with shelve.open(Contact.db) as db:
            for key in db.keys():
                if not term or term.lower() in key.lower():
                    Contact(db[key].name, db[key].number)
        #print retrieved contacts
        retrieved_contacts = []
        for c in sorted(Contact.theContacts, key=lambda x : x.split()[-1]):
            if term:
                if term.lower() in c.lower():
                    #print(Contact.theContacts[c]) # τροποποίηση για χρήση από listbox
                    retrieved_contacts.append(Contact.theContacts[c])
            else:
                #print(Contact.theContacts[c]) # # τροποποίηση για χρήση από listbox
                retrieved_contacts.append(Contact.theContacts[c])
        return retrieved_contacts  # επιστρέφει τη λίστα από τις επαφές με βάση το κριτήριο term
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
        return self.name + ':\t' + self.number

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

class ContactWindow():
    def __init__(self, root, operation, contact=None):
        self.operation = operation
        self.root = root
        self.contact = contact
        self.fnt = 'Arial 24'
        if self.contact:
            print(self.contact)
            self.name = self.contact.name
            self.number = self.contact.number
        else:
            self.name = self.number = ''
        self.create_window()
    def create_window(self):
        x,y = self.root.winfo_x(), self.root.winfo_y()
        self.window = tk.Toplevel(self.root)
        self.window.geometry('+{}+{}'.format(x,y))
        self.f0 = tk.Frame(self.window)
        self.f0.pack(side='top', expand=True, fill='both', padx=2, pady=2)
        if self.operation == 'delete': msg = 'Διαγραφή Επαφής'
        elif self.operation == 'insert': msg = 'Εισαγωγή νέας Επαφής'
        elif self.operation == 'modify': msg = 'Tροποποίηση Επαφής'
        else: msg = ''
        tk.Label(self.f0, text=msg, font=self.fnt, fg='grey60').pack(side='left', expand=True, fill='both', padx=2, pady=2)
        self.f1 = tk.Frame(self.window)
        self.f1.pack(side='top', expand=True, fill='both', padx=2, pady=2)
        tk.Label(self.f1, text='Όνομα:', font=self.fnt).pack(side='left', expand=True, fill='both', padx=2, pady=2)
        self.name_entry = tk.Entry(self.f1, font=self.fnt, relief='sunken')
        self.name_entry.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        self.f2 = tk.Frame(self.window)
        self.f2.pack(side='top', expand=True, fill='both', padx=2, pady=2)
        tk.Label(self.f2, text='Τηλέφωνο:', font=self.fnt).pack(side='left', expand=True, fill='both', padx=2, pady=2)
        self.number_entry = tk.Entry(self.f2, font=self.fnt, relief='sunken')
        self.number_entry.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        if self.operation != 'insert':
            self.name_entry.insert('end', self.name)
            self.number_entry.insert('end', self.number)
        if self.operation == 'delete':
            self.name_entry.config(state='disabled')
            self.number_entry.config(state='disabled')
        self.f3 = tk.Frame(self.window)
        self.f3.pack(side='top', expand=True, fill='both', padx=2, pady=2)
        b1 = tk.Button(self.f3, text='OK', command=self.to_act, font=self.fnt)
        b1.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        b2 = tk.Button(self.f3, text='Άκυρο', command=self.no_act, font=self.fnt)
        b2.pack(side='left', expand=True, fill='both', padx=2, pady=2)
        self.root.wait_window(self.window)

    def to_act(self):
        if self.operation == 'delete':
            self.window.destroy()
            Contact.del_contact(self.contact.name)
        else:
            new_name = self.name_entry.get().strip()
            new_number = self.number_entry.get().strip()
            self.window.destroy()
            if new_name in Contact.theContacts:
                Contact.theContacts[new_name].set_number(new_number)
            else:
                if new_name:
                    Contact(new_name, new_number, new=True)
        app.display_with_term()
    def no_act(self):
        self.window.destroy()

class App():
    def __init__(self, root):
        self.root = root
        self.root.title('MyContacts')
        self.fnt ='Arial 24'
        self.widgets()
    def widgets(self):
        self.f0 = tk.LabelFrame(self.root, text='αναζήτηση')
        self.f0.pack(side='top', expand=True, fill='both', padx=5, pady=5)
        self.search = tk.Entry(self.f0, font = self.fnt, width=40,  bg='lightyellow')
        self.search.pack(side = 'left', expand=True, fill='both')
        self.b0 = tk.Button(self.f0, font=self.fnt, text = ' + ', command=self.insert)
        self.b0.pack(side = 'left', expand=True, fill='both', padx=5, pady=5)
        self.f1 = tk.LabelFrame(self.root, text='επαφές')
        self.f1.pack(expand=True, fill='both', padx=5, pady=5)
        self.sbar = tk.Scrollbar(self.f1)
        self.list = tk.Listbox(self.f1, relief='sunken', font = self.fnt,
                               bg = 'lightyellow', height=30, width=20)
        self.sbar.config(command=self.list.yview)
        self.sbar.pack(side='right', fill='y')
        self.list.config(yscrollcommand=self.sbar.set)
        self.list.pack(expand=True, fill='both')
        self.context = tk.Menu(self.root, font = self.fnt)
        self.root.config(menu=self.context)
        self.context.add_command(label='Τροποποίηση...', command=self.modify)
        self.context.add_command(label='Διαγραφή...', command= self.delete)
        self.initialize_contacts()
        self.contacts = Contact.retrieve_contacts()
        self.current = None
        self.fill_box()
        # έλεγχος για τη διαφορά στο δεξί πλήκτρο μεταξύ λειτουργικών συστημάτων
        if (root.tk.call('tk', 'windowingsystem') == 'aqua'):
            root.bind('<2>', self.post)
        else:
            root.bind('<3>', self.post)
        self.search.bind('', self.search_handler )
    def initialize_contacts(self):
        if not os.path.isfile('contacts'):
            size = input('αρχικός αριθμός επαφών')
            try:
                Contact.create_contacts(int(size))
            except: print('δεν υπάρχουν αρχικές επαφές')

    def fill_box(self):
        if self.contacts:
            for pos, c in enumerate(self.contacts):
                self.list.insert(pos, repr(c))
        if self.current: self.list.select_set(self.current)        # να θυμάσαι την επιλογή

    def post(self, event): # αναδυόμενο μενού
        self.context.post(event.x_root, event.y_root)

    def delete(self):
        self.current = self.list.curselection()[0]
        print(type(self.contacts[self.current]))
        ContactWindow(self.root, 'delete', self.contacts[self.current])
        self.display_with_term()

    def modify(self):
        self.current = self.list.curselection()[0]
        ContactWindow(self.root, 'modify', self.contacts[self.current])
        self.display_with_term()

    def insert(self):
        ContactWindow(self.root, 'insert')
        self.display_with_term()

    def search_handler(self, event):
        self.display_with_term()

    def display_with_term(self):
        self.list.delete(0, 'end')
        txt = self.search.get()
        self.contacts = Contact.retrieve_contacts(txt)
        self.fill_box()

root = tk.Tk()
app = App(root)
root.mainloop()
