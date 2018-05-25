# Διαχείριση κειμένου

import tkinter as tk

class App():
    def __init__(self, root):
        self.root = root
        search_f = tk.Frame()
        search_f.pack(fill='x')
        self.fnt ='Arial 20'
        tk.Label(search_f, text='Αναζήτηση:', font = self.fnt).pack(side = 'left',
                                                   expand=1, fill='x')
        self.term = tk.Entry(search_f, bg='lightblue', width=30, font=self.fnt)
        self.term.pack(expand=1, fill= 'x')
        self.term.bind('', self.search)
        text_f = tk.Frame()
        text_f.pack(expand = 1, fill='both')
        self.tx = tk.Text(text_f, bg='lightyellow', width=80, height=50)
        self.tx.pack(expand=True, fill='both')
        self.tx.insert('1.0', '\n')
        for line in open('varvaroi.txt', 'r', encoding='utf-8'):
            self.tx.insert('end', line)
        kavafis_image = tk.PhotoImage(file='Kavafis.gif')
        self.tx.image_create('1.0', image=kavafis_image)
        self.tx.image = kavafis_image
        self.tx.tag_configure('found', background= 'yellow', foreground='red')
    def search(self, event):
        indx = '1.0'
        term = self.term.get()
        self.tx.tag_remove('found', '1.0', 'end')
        while True:
            indx = self.tx.search(term, indx, nocase=True,
                                  stopindex= 'end')
            if not indx: break
            endindx = '{}+{}c'.format(indx, len(term))
            self.tx.tag_add('found', indx, endindx)
            indx = endindx
        print(self.tx.tag_ranges('found'))

root = tk.Tk()
App(root)
root.mainloop()
