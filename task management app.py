def task():
    tasks = []  # empty list
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")

    # how many tasks to add initially
    total_task = int(input("Enter how many tasks you want to add: "))

    # add initial tasks
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    # display tasks
    print("\nToday's tasks are:")
    for t in tasks:
        print("-", t)

    while True:
        print("\nChoose Operation:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task updated to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("\nCurrent Tasks:")
            for t in tasks:
                print("-", t)

        elif operation == 5:
            print("Closing the program. Goodbye 👋")
            break

        else:
            print("Invalid input. Please try again.")


#  function call 
task()