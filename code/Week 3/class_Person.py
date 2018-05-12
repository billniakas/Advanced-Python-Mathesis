class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Άτομο: %r, μισθός: %r]' % (self.name, self.pay)

    def __str__(self):
        return self.name+' '+str(self.pay)