# employee example
class Employee():
    ''' Ο εργαζόμενος σε μια επιχείρηση '''
    the_employees = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.the_employees.append(self)

# main program

while True:
    name = input('Όνομα:')
    if not name: break
    salary = input('Μισθός:')
    Employee(name, salary)

# print the employees
print('\nΟι υπάλληλοι είναι:')
for employee in sorted(Employee.the_employees, key=lambda x: x.name):
    print(employee.name, employee.salary, sep='\t')