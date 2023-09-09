class Employee:
    def __init__(self, Id=None, name=None, salary=None, dept=None):
        self.Id = Id
        self.name = name
        self.salary = salary
        self.dept = dept

    def takeValues(self):
        self.Id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter salary: "))
        self.dept = input("Enter Department: ")


def main():
    employee_list = []

    n = int(input("Enter the number of employees: "))

    for _ in range(n):
        emp = Employee()
        emp.takeValues()
        employee_list.append(emp)
        print("Employee added successfully!")

    while True:
        print("\nMenu:")
        print("1. Display Employees")
        print("2. Search an Employee")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nEmployee List:")
            for emp in employee_list:
                print(f"ID: {emp.Id}, Name: {emp.name}, Salary: {emp.salary}, Department: {emp.dept}")
            print("-------------")
        elif choice == 2:
            ch = int(input("Enter ID of the employee to search: "))
            found = False
            for emp in employee_list:
                if emp.Id == ch:
                    print(
                        f"Employee found - ID: {emp.Id}, Name: {emp.name}, Salary: {emp.salary}, Department: {emp.dept}")
                    found = True
                    break
            if not found:
                print("Employee not found.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
