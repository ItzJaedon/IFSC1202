class Employee:
    def __init__(self, first_name, last_name, id_number, wage):
        self.FirstName = first_name
        self.LastName = last_name
        self.IDNumber = id_number
        self.HoursWorked = 0
        self.Wage = wage
    def WeeklyPay(self):
        if self.HoursWorked <= 40:
            return self.Wage * self.HoursWorked
        else:
            return 40 * self.Wage + (self.HoursWorked - 40) * 1.5 * self.Wage
def find_employee(employee_list, employee_id):
    for i, employee in enumerate(employee_list):
        if employee.IDNumber == employee_id:
            return i
    return -1
employee_list = []
with open('11.02 Employees.txt', 'r') as f:
    for line in f:
        data = line.strip().split()
        employee = Employee(data[0], data[1], data[2], float(data[3]))
        employee_list.append(employee)
with open('11.02 Hours.txt', 'r') as f:
    for line in f:
        data = line.strip().split()
        employee_id = data[0]
        hours_worked = float(data[1])
        i = find_employee(employee_list, employee_id)
        if i != -1:
            employee_list[i].HoursWorked = hours_worked
print("{:<7}{:<8}{:<8}{:<9}{:<9}{:<9}".format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
for employee in employee_list:
    print("{:<7}{:<8}{:<8}{:<9.2f}{:<9.2f}{:<9.2f}".format(employee.FirstName, employee.LastName, employee.IDNumber, employee.HoursWorked, employee.Wage, employee.WeeklyPay()))