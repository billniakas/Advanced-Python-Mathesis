# Η Οικογένεια του Κολοκοτρώνη

import tkinter as tk
from tkinter import ttk
import re

class App():
    def __init__(self, root):
        root.title('Η οικογένεια του Θ.Κολοκοτρώνη')
        root.geometry('1280x800')
        self.build_tree('kolokotronis_family_tree.txt')
        #screen_width= root.
        image = tk.Frame(root)
        image.pack(side='left', fill='y')
        kolokotronis_image = tk.PhotoImage(file='Kolokotronis.gif')
        # Lithography by Karl Krazeisen (1794-1878) από el.wikipedia.org
        root.image = kolokotronis_image
        tk.Label(image, image=kolokotronis_image).pack(side='top', pady=20)
        tk.Label(image, text= 'Γενεαλογικό Δένδρο \nτης οικογένειας\n του Θεόδωρου Κολοκοτρώνη',
                 font= 'Arial 28 italic', bg='lightblue', fg = 'blue').pack(expand=True, fill='both')
        family_view = tk.Frame(root)
        family_view.pack(expand=True, fill='both')
        Family.show_tree(family_view)
    def build_tree(self, fname):
        with open(fname, 'r', encoding='utf-8') as ftree:
            fline = 10*[None] # fline: τρέχουσα family line
            for line in ftree:
                level= line.count('\t')
                if level==0: parent = None
                else: parent = fline[level-1]
                fline[level] = Family(parent, line) # δημιουργία αντικεικένου τύπου Family
                if parent: parent.children.append(fline[level]) # ενημέρωσε τον πατέρα για νέο παιδί
                #print(level,line)

class Family():
    root = None
    @staticmethod
    def show_tree(viewer):
        root = Family.root
        s = ttk.Style()
        s.configure('Treeview', font = 'Arial 14', rowheight=35 )
        if not root: return False
        tree = ttk.Treeview(viewer, style = 'Treeview')
        tree["columns"]=("cv","kids")
        tree.column("cv", width=300, stretch = True )
        tree.column("kids", width=80, anchor='e', stretch = False)
        tree.heading("cv", text="Η ζωή του")
        tree.heading("kids", text="Τέκνα")
        # εισαγωγή ρίζας (Θ.Κ.)
        Family.add_tree_entry(tree, root)
        tree.pack(expand=True, fill='both')
    @staticmethod
    def add_tree_entry(tree, member):
        if member == Family.root:
            item = tree.insert("" , 0, text= member.name, values = (member.cv,
                                                                    str(len(member.children))))
        else:
            item = tree.insert(member.tree_parent_id, "end", text= member.name,
                               values = (member.cv, str(len(member.children))))
        for kid in member.children:
            kid.tree_parent_id = item
            Family.add_tree_entry(tree, kid)
    @staticmethod
    def show_tree_print(root):
        print(root)
        for kid in root.children: Family.show_tree(kid)
    def __init__(self, parent, description):
        description = re.sub("\[.+?\]",'', description) #αγνόησε παραπομπές πχ [2]
        self.parent = parent
        if not parent: Family.root = self
        self.children = []
        self.name = description.split(',')[0].strip()
        self.relation = re.findall("και ((εξώγαμος γιος|γιος|κόρη).+)", description, re.I)[0][0] # εξαγωγή σχέσης με γονέα
        self.cv = description.replace(self.name, '').replace('και '+self.relation, '').strip().strip(',').strip('και')
        self.cv = self.cv.strip()[0].upper()+ self.cv.strip()[1:]
        self.tree_parent_id = None # item id
        print(self)
    def __repr__(self):
        if self.parent == None: parent= 'Κωνσταντής Κολοκοτρώνης' # ρίζα του δένδρου ο πατέρας του Θ.Κ.
        else: parent = self.parent.name
        return 'ONOMA:'+self.name +'\n' + '(τέκνο..'+parent+')\n' \
    + 'ΣΧΕΣΗ ΜΕ γονέα:'+self.relation+'\n' + 'Βιογραφία:'+ self.cv

root = tk.Tk()
App(root)
root.mainloop()

