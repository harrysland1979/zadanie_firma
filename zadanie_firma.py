employees = []

while True:
    print("1 - Add, 2 - Edit, 3 - Delete, 4 - Display, 5 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        hire_date = input("Enter hire date: ")
        employees.append({"name": name, "surname": surname, "position": position, "salary": salary, "hire_date": hire_date})

    elif choice == "2":
        for i, employee in enumerate(employees, start=1):
            print(f"{i}. {employee['name']} {employee['surname']}, {employee['position']}, {employee['salary']}, {employee['hire_date']}")
        index = int(input("Enter the number of the employee to edit: ")) - 1
        name = input("Enter new name (leave blank to keep current): ")
        surname = input("Enter new surname (leave blank to keep current): ")
        position = input("Enter new position (leave blank to keep current): ")
        salary = input("Enter new salary (leave blank to keep current): ")
        hire_date = input("Enter new hire date (leave blank to keep current): ")
        if name:
            employees[index]["name"] = name
        if surname:
            employees[index]["surname"] = surname
        if position:
            employees[index]["position"] = position
        if salary:
            employees[index]["salary"] = salary
        if hire_date:
            employees[index]["hire_date"] = hire_date

    elif choice == "3":
        for i, employee in enumerate(employees, start=1):
            print(f"{i}. {employee['name']} {employee['surname']}, {employee['position']}, {employee['salary']}, {employee['hire_date']}")
        index = int(input("Enter the number of the employee to delete: ")) - 1
        del employees[index]

    elif choice == "4":
        for i, employee in enumerate(employees, start=1):
            print(f"{i}. {employee['name']} {employee['surname']}, {employee['position']}, {employee['salary']}, {employee['hire_date']}")

    elif choice == "5":
        break