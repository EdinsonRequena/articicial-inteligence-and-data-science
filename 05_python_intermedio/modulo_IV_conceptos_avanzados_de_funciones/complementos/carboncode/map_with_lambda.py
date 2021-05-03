class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def __str__(self):

        return f'My name is {self.name} and my salary is {self.salary}'

list_employee = [
    Employee('Andrea', 7500),
    Employee('Edinson', 3000),
    Employee('Test', 2500),
]

comision_list = map(lambda arg: arg.salary * 1.03 if arg.salary <= 3000 else arg, list_employee)
[print(i) for i in comision_list]