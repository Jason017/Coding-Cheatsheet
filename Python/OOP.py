import datetime

class Employee:
    raise_amount = 1.04
    num_of_employee = 0
    def __init__(self, firstname, lastname, pay_by_second):
        self.firstname = firstname
        self.lastname = lastname
        self.pay_by_second = pay_by_second
        self.email = firstname + '.' + lastname + "@company.com"
        Employee.num_of_employee += 1

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.pay_by_second = int(self.pay_by_second * self.raise_amount)

    
    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, pay = emp_str.split("-")
        return cls(firstname, lastname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.num_of_employee)
emp_1 = Employee('Jeff','Bezos', 367)
emp_2 = Employee('Mark','Zuckerberg', 586)
print(Employee.num_of_employee)

print(emp_1.pay_by_second)
emp_1.apply_raise()
print(emp_1.pay_by_second)

print(emp_1.__dict__)
print(Employee.__dict__)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)


new_emp_1 = Employee.from_string("test-name-1")
print(new_emp_1.email)

my_date = datetime.date(2021, 8, 1)
print(Employee.is_workday(my_date))



### Super class

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, firstname, lastname, pay_by_second, progress):
        super().__init__(firstname, lastname, pay_by_second)
        self.progress = progress


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Python', 'Awesome', 10000, 'junior')
dev_2 = Developer('Push', 'Forward', 50000, 'senior')

mgr_1 = Manager('My', 'Manager', 120000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()




