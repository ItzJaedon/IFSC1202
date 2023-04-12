class Employee:
    def __init__(self, first_name, last_name, id_number, hours_worked, wage):
        self.FirstName = first_name
        self.LastName = last_name
        self.IDNumber = id_number
        self.HoursWorked = hours_worked
        self.Wage = wage
    
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked * self.Wage
        else:
            regular_pay = 40 * self.Wage
            overtime_pay = (self.HoursWorked - 40) * 1.5 * self.Wage
            return regular_pay + overtime_pay
with open('10.06 Payroll.txt') as f:
    for line in f:
        data = line.strip().split(',')
        first_name, last_name, id_number, hours_worked, wage = data
        employee = Employee(first_name, last_name, id_number, float(hours_worked), float(wage))
        weekly_pay = employee.WeeklyPay()
        print('{:8s} {:8s} {:7s} {:7.2f} {:7.2f} {:7.2f}'.format(first_name, last_name, id_number, float(hours_worked), float(wage), weekly_pay))