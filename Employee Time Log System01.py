import time

timelog = {}

while True:
    print("\nOptions")
    print("1. Time In")
    print("2. Time Out")
    print("3. View Logs")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        employee_name = input("Enter Employee Name: ")
        if employee_name in timelog and 'in' in timelog[employee_name]:
            print("Already timed in.")
        else:
            timelog[employee_name] = {'in': time.strftime("%Y-%m-%d %H:%M:%S"), 'out': None}
            print(f"{employee_name} timed in at {timelog[employee_name]['in']}")
    elif choice == 2:
        if not timelog:
            print("No log records yet.")
        else:
            employee_name = input("Enter Employee Name: ")
            if employee_name in timelog and 'in' in timelog[employee_name] and timelog[employee_name]['out'] is None:
                timelog[employee_name]['out'] = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"{employee_name} timed out at {timelog[employee_name]['out']}")
            elif employee_name in timelog and timelog[employee_name]['out'] is not None:
                print(f"{employee_name} has already timed out.")
            else:
                print("Employee not found.")
    elif choice == 3:
        if not timelog:
            print("No records yet.")
        else:
            print("-- Time Log --")
            for i, (p, t) in enumerate(timelog.items(), 1):
                time_in = t.get('in', 'N/A')
                time_out = t.get('out', 'N/A')
                print(f"{i}. {p} | In: {time_in} | Out: {time_out}")
    elif choice == 4:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid Choice! Please select a number from 1-4")