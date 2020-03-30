from django.shortcuts import render
from .models import Employee, Developer
import datetime

# Create your views here.
def kimtest(request):

    emp1 = Employee('Abc', 'Xyz', 100)

    # They are the same
    Employee.raise_amount = 1.04
    Employee.set_raise_amt(1.04)

    # example of @classmethod from_string()
    emp_str1 = 'KKK-YYY-10000'
    emp_str2 = 'AAA-BBB-22000'
    emp_str3 = 'YYY-ZZZ-33000'

    emp2 = Employee.from_string(emp_str3)
    print(f' emp2.pay: {emp2.pay}')

    # emp1.raise_amount = 1.11
    print(f' Employee.raise_amount: {Employee.raise_amount}')
    print(f' emp1.raise_amount: {emp1.raise_amount}')
    print(f' Total Employees: {Employee.total_employee}')
    print(emp1.__dict__)

    # test static method is_workday
    my_date = datetime.date(2020, 3, 30)
    # print(f' {my_date.strftime("%Y-%B-%d")}')
    print(Employee.is_workday(my_date))

    dev1 = Developer('Kim', 'Zzz', 123)
    dev1.apply_raise()
    print(f' {dev1.__dict__}')
    # print(help(dev1))



    context = {
        'test': emp1,

        'kim' : emp1.fullInfo(),
        'kim2': Employee.fullInfo(emp1),

        'example1': emp1.raise_amount,
        'example2': Employee.raise_amount,

        'dict': emp1.__dict__,
        'dict1': Employee.__dict__,
        'dict2': emp1.__dict__.items(),
        'dict3': emp1.__dict__.keys(),
        'dict4': emp1.__dict__.values(),

    }
    return render(request, 'kimtest/test.html', context)



