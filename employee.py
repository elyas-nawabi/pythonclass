
def employeeInfo(employee):
    def customizingEmployee():
        employee()
        print("Company Name: Tesla")
        print("Company Address: United States Of America")
        print("Company Phone: +198763412355")
    return customizingEmployee

@employeeInfo
def employee1():
    print("Employee Name is:  Mustafa")

@employeeInfo
def employee2():
    print("Employee Name is:  Ahmad")

@employeeInfo
def employee3():
    print("Employee Name is:  Modasir")

employee1()
employee2()
employee3()