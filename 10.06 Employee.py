class Employee:
    def __init__(self, FirstName, LastName, IDNumber, HoursWorked, Wage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage
class Employee:
    def __init__(self, FirstName, LastName, IDNumber, HoursWorked, Wage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage
    
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.HoursWorked * self.Wage
        else:
            regular_pay = 40 * self.Wage
            overtime_pay = (self.HoursWorked - 40) * self.Wage * 1.5
            return regular_pay + overtime_pay
employees = []
with open('10.06 Payroll.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        emp = Employee(data[0], data[1], data[2], int(data[3]), float(data[4]))
        employees.append(emp)
for emp in employees:
    print(f"{emp.FirstName} {emp.LastName}, ID: {emp.IDNumber}, Hours Worked: {emp.HoursWorked}, Hourly Wage: ${emp.Wage:.2f}, Weekly Pay: ${emp.WeeklyPay():.2f}")
