# εφαρμογή contacts v.4 με αποθήκευση σε sqlite3 βάση δεδομένων
# χωρίς ξεχωριστή κλάση persist, πλήρης υλοποίηση CRUD
import os
import random
import sqlite3 as lite

class Contact():
    ''' κλάση επαφών με όνομα και τηλέφωνο
        μια μεταβλητή κλάσης theContacts'''
    theContacts = {}
    db ='contacts.database'
    @staticmethod
    def create_db():
        try:
            conn = lite.connect(Contact.db)
            with conn:
                curs = conn.cursor()
                sql = 'create table contact(name text primary key, number text);'
                curs.execute(sql)
                return True
        except lite.Error : return False
    @staticmethod
    def count_records():
        try:
            conn = lite.connect(Contact.db)
            with conn:
                curs = conn.cursor()
                sql = "select count (*) from contact;"
                curs.execute(sql)
                return curs.fetchone()[0]
        except lite.Error as er:
            print(er)
            return 0
    @staticmethod
    def retrieve_contacts(term = ''):
        Contact.theContacts = {}
        try:
            conn = lite.connect(Contact.db)
            with conn:
                curs = conn.cursor()
                if term: # έχει δοθεί κλειδί αναζήτησης term
                    sql = "select * from contact where name like '%{}%'; ".format(term)
                else:
                    sql = "select * from contact;"
                curs.execute(sql)
                records = curs.fetchall()
                for rec in records:
                    Contact(rec[0], rec[1])
        except lite.Error as er: print(er)
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
            try:
                conn = lite.connect(Contact.db)
                with conn:
                    curs = conn.cursor()
                    sql = "delete from contact where name = '{}';".format(id)
                    curs.execute(sql)
            except lite.Error as er:
                print(er)

    def __init__(self, name, number='', new=False): #  μέθοδος δημιουργός επαφών
        self.name = name.strip()
        self.number = number.strip()
        Contact.theContacts[self.name] = self
        if new: self.insert()
    def insert(self):
        try:
            conn = lite.connect(Contact.db)
            with conn:
                curs = conn.cursor()
                sql = "insert into contact values ('{}', '{}');"
                curs.execute(sql.format(self.name, self.number))
        except lite.Error as er:
            print(er)
    def set_number(self, number):
        self.number = number
        try:
            conn = lite.connect(Contact.db)
            with conn:
                curs = conn.cursor()
                sql = 'update contact set number = "{}" where name = "{}";'.format(self.number, self.name)
                curs.execute(sql)
        except lite.Error as er:
            print(er)
    def __repr__(self): # μέθοδος εκτύπωσης επαφών
        return self.name + ': ' + self.number

class Main():
    ''' κλάση επικοινωνίας με τον χρήστη - δημιουργία - διαγραφή επαφών'''
    Contact.create_db()
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
                            Contact.theContacts[id].set_number( contact_details.split(':')[1].strip())
                        else: # πρόκειται για νέα εισαγωγή
                            Contact(*contact_details.split(':'), new=True)
                    except IndexError:
                        print('Σφάλμα εισαγωγής επαφής')
                else: print('Προσοχή δώσε το όνομα, άνω-κάτω τελεία (:) τηλέφωνο')

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
            number = str(random.randint(6900000000,6999999999))
            Contact(contact, number, new=True)

if __name__ == '__main__': Main()