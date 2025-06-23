def todolist():
    tasks = []
    while True:
        print("Options: ")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display tasks")
        print("4. Mark as complete")
        print("5. Exit")
        option = input("Enter an option: ")
        if option == "1":
            task = input("Enter task name: ")
            tasks.append({"task":task,"state":"incomplete"})
            print(f"'{task}' added into the list")
        elif option == "2":
            task = input("Enter task name: ")
            for tsk in tasks:
                if tsk["task"] == task:
                    tasks.remove(tsk)
                    print(f"'{task}' deleted from the list")
                    break
            else:
                print(f"Task not found")
        elif option == "3":
            if tasks:
                print("Tasks: ")
                for tsk in tasks:
                    print(f"{tsk['task']} - {tsk['state']}")
            else:
                print("No tasks")
        elif option == "4":
            task = input("Enter task name: ")
            for tsk in tasks:
                if tsk["task"] == task:
                    tsk["state"] = "complete"
                    print(f"'{task}' marked as complete")
                    break
            else:
                print("Task not found")
        elif option == "5":
            print("Exit successful")
            break
        else:
            print("Invalid option")
todolist()
