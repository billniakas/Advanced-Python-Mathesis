# εφαρμογή contacts v.3b με αποθήκευση σε αρχείο shelve και πράξεις σε εγγραφές
# χωρίς ξεχωριστή κλάση persist, πλήρης υλοποίηση CRUD
import os
import random
import shelve

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
        Contact.theContacts = {}
        with shelve.open(Contact.db) as db:
            for key in db.keys():
                if not term or term.lower() in key.lower():
                    Contact(db[key].name, db[key].number)
        #print retrieved contacts
        for c in sorted(Contact.theContacts, key=lambda x : x.split()[-1]):
            if term:
                if term.lower() in c.lower():
                    print(Contact.theContacts[c])
            else: print(Contact.theContacts[c])
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
        return self.name + ': ' + self.number

class Main():
    ''' κλάση επικοινωνίας με τον χρήστη - δημιουργία - διαγραφή επαφών'''
    def __init__(self):
        while True:
            command = input('\nΕπαφές:{}. \n[+]εισαγωγή/αλλαγή [-]διαγραφή  [?]επισκόπηση [enter] Έξοδος.:'.\
                            format(Contact.count_records()))
            if command == '': break
            elif command[0] == '?':
                Contact.retrieve_contacts(command[1:])
            elif command[0] == '-':
                name = input('ΔΙΑΓΡΑΦΗ. Δώσε Όνομα επαφής >>>')
                try:
                    #del Contact.theContacts[name.strip()]
                    Contact.del_contact(name.strip())
                except KeyError : print('Επαφή με όνομα {} δεν υπάρχει'.format(name))
            elif command[0] == '+':
                contact_details = input('ΕΙΣΑΓΩΓΗ Όνομα επαφής: τηλέφωνο / πλήθος εγγραφών >>>')
                if contact_details.isdigit() and int(contact_details) < 500:
                    self.create_contacts(int(contact_details))
                elif ':' in contact_details:
                    try:
                        id = contact_details.split(':')[0].strip()
                        if id in Contact.theContacts: # πρόκειται για αλλαγή τηλεφώνου
                            Contact.theContacts[id].set_number(contact_details.split(':')[1].strip())
                        else: # πρόκειται για νέα εισαγωγή
                            Contact(*contact_details.split(':'), new=True)
                    except IndexError:
                        print('Σφάλμα εισαγωγής επαφής')
                else: print('Προσοχή δώσε το όνομα, άνω-κάτω τελεία (:) τηλέφωνο')
        #persist.store()

    def create_contacts(self, size):
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

if __name__ == '__main__': Main()