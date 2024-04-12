from datetime import date

def create_employee(name, position, base_salary):
    hiring_date = date.today()
    employee = {
        'name': name,
        'position': position,
        'base_salary': base_salary,
        'hiring_date': hiring_date
    }
    return employee

def calculate_bonus(employee, performance_rating):
    if performance_rating == 5:
        bonus = 0.2 * employee['base_salary']
    elif performance_rating == 4:
        bonus = 0.1 * employee['base_salary']
    else:
        bonus = 0
    return bonus


no_of_employees = int(input('Enter number of employees: '))
print(f'Enter the basic details below for {no_of_employees} employees.')

employees = []
for _ in range(no_of_employees):
    name = input("\nName: ")
    position = input("Position: ")
    base_salary = float(input("Base salary: "))
    employee = create_employee(name, position, base_salary)
    employees.append(employee)

print("\nAnnual Bonus:")
for employee in employees:
    performance_rating = int(input(f"Enter performance rating for {employee['name']}: "))
    bonus = calculate_bonus(employee, performance_rating)
    print(f"{employee['name']} ({employee['position']}) - Bonus: ₹{bonus:.2f}")
