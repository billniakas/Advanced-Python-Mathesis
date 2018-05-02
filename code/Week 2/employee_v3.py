class Person():
    employees = []
    def __init__(self, name, job='', salary=0):
        self.name = name.strip()
        self.job = job.strip()
        self.salary = float(salary)
        Person.employees.append(self)
    def give_raise(self, percent):
        '''percent of salary increase with values between 0 and 1'''
        self.salary = float(self.salary*(1+percent))
    def __str__(self):
        sal = "{:.2f}".format(self.salary) if self.salary > 0 else ""
        return self.name+' '+self.job+ ': '+sal

class Manager(Person):
    def __init__(self, name, salary=0):
        Person.__init__(self,name, 'Διευθυντής', salary)
    def give_raise(self, percent, bonus = 0.10):
        Person.give_raise(self,percent+bonus)