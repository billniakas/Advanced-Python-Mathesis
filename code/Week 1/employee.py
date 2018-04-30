# employee example
class Employee():
    ''' Ο εργαζόμενος σε μια επιχείρηση '''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# main program
the_employees = []
while True:
    name = input('Όνομα:')
    if not name: break
    salary = input('Μισθός:')
    the_employees.append(Employee(name, salary))

# print the employees
print('\nΟι υπάλληλοι είναι:')
for employee in sorted(the_employees, key=lambda x: x.name):
    print(employee.name, employee.salary, sep='\t')