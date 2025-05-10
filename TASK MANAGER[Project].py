def task():
    tasks = [] #empty list
    print("----WELCOME TO TASK MANAGER----")

    total_task = int(input("Enter how many task are to be done = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print("Today's tasks are => ")
    for task in tasks:
        print("-", task)

    while True:
        operation = int(input("Enter \n 1 TO ADD\n 2 TO UPDATE\n 3 TO DELETE\n 4 TO VIEW\n 5 TO EXIT\n"))
        if operation == 1:
            add = input("Enter Task That Is To Be Added = ")
            tasks.append(add)
            print(f"Task {add} Has Been Successfully Added.")

        elif operation == 2:
            updated_val = input("Enter Task You Want To Update = ")
            if updated_val in tasks:
                up = input("Enter New Task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated Task {up}")

        elif operation == 3:
            del_val = input("Which Task You Want To Delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} Has Been Deleted.")

        elif operation == 4:
            print(f"Total Tasks No. Of Tasks Are = {tasks}")

        elif operation == 5:
            print("Closing The Program. Thanks For Using TASK MANAGER")
            break

        else:
            print("Invalid Input")
            
task()


##--------------------------------------------------------------X------------------------------------------------------------
