tasks = []
while True:
    print("\n---TO DO LIST---")
    print("1. Add task")
    print("2. view task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        print("\nyour task")

        if len(tasks) == 0:
            print("no tasks found.")
        else:
            for i, task in enumerate(tasks,start=1):
                print(i,task)

    elif choice == "3":
        task_number = int(input("Enter the task number:"))
        if 1 <= task_number <=len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted!")
        else:
            print("invalid task number. please try again later.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")